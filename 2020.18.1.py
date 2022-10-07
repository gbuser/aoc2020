data = [x.rstrip() for x in open('data.txt', 'r')]
import re

#remove all nested parens and replace with evaluated expression
def remove_parens(line):
    while '(' in line:
        single_parens = re.findall("\([\d\s+*]+\)", line)
        for exp in single_parens:
            trimmed = exp.replace("(", "")
            trimmed = trimmed.replace(")", "")
            result = parse(trimmed)
            line = line.replace(exp, str(result))
    return line


#start with first number, next list item is the function, do it with the next number and repeat
def parse(expression):
    items = [(lambda x: (int(x) if x.isdigit() else x))(x) for x in expression.split(' ')]
    op1 = items.pop(0)
    result = 0
    while (len(items)):
        fxn = items.pop(0)
        op2 = items.pop(0)
        if fxn == '+':
            op1 += op2
        if fxn == '*':
            op1 *= op2
    return op1
        


        
#do it one line at a time
tally = 0
for line in data:
    tally += parse(remove_parens(line))

print(tally)
