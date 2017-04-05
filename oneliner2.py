from itertools import groupby

def count_letters(text):
    return "".join("{}{}".format(count,label) for label, count in [(label, sum(1 for _ in group)) for label, group in groupby(text)])

gs = groupby("aaaaabbbccceeeeaaa")

for i in gs:
    print i[0] + str(sum(1 for _ in i[1]))
