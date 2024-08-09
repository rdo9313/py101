def century_num(year):
    if year % 100 == 0:
        return year // 100
    
    return (year // 100) + 1

def suffix(num):
    special_numbers = (11, 12, 13)
    if (num % 100) not in special_numbers:
        match (num % 10):
            case 1:
                return 'st'
            case 2:
                return 'nd'
            case 3:
                return 'rd'
    return 'th'

def century(year):
    century = century_num(year)
    return str(century) + suffix(century)

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True