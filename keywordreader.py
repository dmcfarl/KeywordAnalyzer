#!/usr/bin/python
import getopt
import sys
import re


def main(argv):
    # PARSE ARGUMENTS
    resume_file = ''
    job_file = ''
    output_file = ''

    try:
        opts, args = getopt.getopt(argv, "hr:j:o:", ["resume=", "job=", "output="])
    except getopt.GetoptError:
        print('keywordreader.py -r <resume_file> -j <job_file> -o <output_file>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-r", "-resume"):
            resume_file = arg
        elif opt in ("-j", "-job"):
            job_file = arg
        elif opt in ("-o", "-output"):
            output_file = arg

    # OPEN FILES
    with open('resources/keywords.txt', 'r') as f1, open('resources/filtered.txt', 'r') as f2, \
            open(resume_file, 'r') as f3, open(job_file, 'r') as f4:
        keyword_lines = f1.readlines()
        filter_lines = f2.readlines()
        resume_lines = f3.readlines()
        job_lines = f4.readlines()

    # FINDS KEYWORDS IN FILES
    resume_keywords = set()
    job_keywords = set()

    keywords = list()
    filters = list()

    def read_list(lines, words):
        for line in lines:
            kw = line.strip().lower()
            words.append(kw)

    def keyword_search(file, found_keywords):
        for line in file:
            line = line.lower()

            # Extract individual words
            for word in re.split('[ /]', line):
                # Exclude punctuation
                word = re.sub(r'\W+', '', word)
                if word not in filters:
                    found_keywords.add(word)
            # Extract additional keywords
            for kw in keywords:
                if kw in line:
                    found_keywords.add(kw)

    read_list(keyword_lines, keywords)
    read_list(filter_lines, filters)

    keyword_search(resume_lines, resume_keywords)  # RESUME
    keyword_search(job_lines, job_keywords)  # JOB DESCRIPTION

    # FINDS DIFFERENCE
    missing_keywords = list()
    missing_keywords.extend(job_keywords - resume_keywords)
    missing_keywords.sort()

    # EXPORTS RESULTS
    with open(output_file, 'w') as f:
        for missing in missing_keywords:
            f.write(missing)
            f.write('\n')


if __name__ == "__main__":
    main(sys.argv[1:])
