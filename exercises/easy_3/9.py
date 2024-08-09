def clean_up(str):
    result = ''

    for char in str:
        if char.isalpha():
            result += char
        else:
            if result == '' or result[-1] != " ":
                result += " "
        
    return result

print(clean_up("---what's my +*& line?") == " what s my line ")
# True