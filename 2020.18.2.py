data = [x.rstrip() for x in open('data.txt', 'r')]
import re

#remove all nested parens and replace with evaluated expression
def remove_parens(line):
    while '(' in line:
        single_parens = re.findall("\([\d\s+*]+\)", line)
        for exp in single_parens:
            trimmed = exp.replace("(", "")
            trimmed = trimmed.replace(")", "")
            result = new_parse(trimmed)
            line = line.replace(exp, str(result))
    return line

#new logic: evaluate sums first then products
def new_parse(exp):
    
    while '+' in exp:
        first =re.findall("\d+\s\+\s\d+", exp)[0]
        first_parce = first.split(' ')
        result = int(first_parce[0]) + int(first_parce[2])
        exp = exp.replace(first, str(result))
    
    exp = [int(x) for x in exp.split(" ") if x.isdigit()]
    
    tally = 1
    for x in exp:
        tally *= x
    return tally
   

tally = 0
for line in data:
    tally += new_parse(remove_parens(line))

print(tally)
