def validate_pin(pin):
    if len(pin) != 4 or len(pin) != 6:
        return False

    else:
        digits = [0,1,2,3,4,5,6,7,8,9]
        for i in pin:
            if i in digits == False:
                return False

    return True

def validate_pin2(pin):
    if re.match('\d\d\d\d',pin,flags=0):
        return True
    else:
        return False



print validate_pin2('1234')
print validate_pin('123456')
print validate_pin('')
print validate_pin('12345')
print validate_pin('abcd')
print validate_pin('abcd5')
