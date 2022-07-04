import re
data = [x.rstrip() for x in open('data.txt', 'r')]

passports = []
this_passport = ''
for line in data:
    this_passport += (' ' + line)
    if len(line) == 0:
        passports.append(this_passport)
        this_passport = ''

has_all_fields = ([x for x in passports if len(x.split())== 8 or (len(x.split())== 7 and 'cid' not in x)])

passports = []
for passport in has_all_fields:
    passport_dict = {}
    for field in passport.split():
        (key, value) = (field.split(':')[0], field.split(':')[1])
        passport_dict[key] = value
    passports.append(passport_dict)

def validate_passport(passport):
    pid_pattern = re.compile('^\d{9}$')
    hcl_pattern = re.compile('^#[0-9a-f]{6}$')
    ecl_pattern = re.compile('^amb$|^blu$|^brn$|^gry$|^grn$|^hzl$|^oth$')
    hgt_pattern = re.compile('^\d{2,3}[cm$|in$]')
    
    if int(passport['byr'])  not in range (1920, 2003):
        return False
    if int(passport['iyr'])  not in range (2010, 2021):
        return False 
    if int(passport['eyr'])  not in range (2020, 2031):
        return False
    if not pid_pattern.match(passport['pid']):
        return False
    if not hcl_pattern.match(passport['hcl']):
        return False
    if not ecl_pattern.match(passport['ecl']):
        return False
    if not hgt_pattern.match(passport['hgt']):
        return False
    hgt = passport['hgt']
    if hgt[-2:] == 'cm':
        if int(hgt[:-2]) not in range(150, 194):
            return False
    if hgt[-2:] == 'in':
        if int(hgt[:-2]) not in range(59, 77):
            return False
    
    return True

len(list(filter(validate_passport, passports)))
