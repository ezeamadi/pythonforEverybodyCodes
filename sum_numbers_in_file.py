import re

fh = open('regex_sum_124084.txt')
numlist = list()
for line in fh:
    stuff = re.findall('([0-9]+)', line)
    for i in stuff:
        i = int(i)
        numlist.append(i)
print(sum(numlist))
