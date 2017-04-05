input = "aaaaabbbccceeaaa"
output = "5a3b3c2e3a"

def cc(text):
    ct =  text[0]
    count = 0
    for t in text:
        if t != ct:
            return (count,ct)
        count += 1
    return (count,ct)

def co(text):
    rslt = ""
    while text != "":
        r = cc(text)
        rslt += str(r[0]) + str(r[1])
        text = text[r[0]:]
    return rslt

print co(input) == output
