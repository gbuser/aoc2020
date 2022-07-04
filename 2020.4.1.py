data = [x.rstrip() for x in open('data.txt', 'r')]

passports = []
this_passport = ''
for line in data:
    this_passport += (' ' + line)
    if len(line) == 0:
        passports.append(this_passport)
        this_passport = ''

len([x for x in passports if len(x.split())== 8 or (len(x.split())== 7 and 'cid' not in x)])
