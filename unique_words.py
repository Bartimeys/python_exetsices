import string
import sys
import csv

csvFile = open('unique.csv', 'w')
csvWriter = csv.writer(csvFile, delimiter='\t')

def by_number(element):
    return element[1]

words = {}
strip = string.whitespace + string.punctuation + string.digits + "\"'"
for filename in sys.argv[1:]:
    for line in open(filename):
        for word in line.lower().split():
            word = word.strip(strip)
            words[word] = words.get(word, 0) + 1
for word, count in sorted(words.items(), key=by_number, reverse=True):
    csvWriter.writerow(["'{0}' occurs {1} times".format(word, count)])





csvFile.close()
