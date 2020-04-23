# OPEN FILES
with open('keywords.txt', 'r') as f1, open('testfile.txt', 'r') as f2, open('testfile2.txt', 'r') as f3:
    keywords = f1.readlines()
    testresume = f2.readlines()
    testjobtext = f3.readlines()

# FINDS KEYWORDS IN FILES
found = set()
found2 = set()


def keyword_search(file, found_keywords):
    for keyword in keywords:
        kw = keyword.strip()
        for line in file:
            line = line.lower()
            if kw in line:
                found_keywords.add(kw)


keyword_search(testresume, found)  # RESUME
keyword_search(testjobtext, found2)  # JOB DESCRIPTION

# FINDS DIFFERENCE
missing_keywords = (found2 - found)

# EXPORTS RESULTS
with open('outputfile.txt', 'w') as f:
    f.write(str(missing_keywords))
