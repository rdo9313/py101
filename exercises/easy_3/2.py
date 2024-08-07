def crunch(str):
    result = ''
    current_char = ''
    for char in str:
        if char != current_char:
            current_char = char
            result += current_char
    
    return result


# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')