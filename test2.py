
#!/usr/bin/python
def sanitaze_name(name):
    if name.replace(' ', '').isalpha():
        return name

def sanitize_last_name(last_name):
    if last_name.replace(' ', '').isalpha():
        return last_name

def sanitize_address(address):
    allowed_symbols = "./\:()'"
    numbers = "1234567890"
    for symbol in address:
        if not symbol.isalpha() or symbol  not in allowed_symbols or symbol not in numbers:
#        if not address.isalpha and address not in allowed_symbols and numbers:
            print("right")
            return None
    print ("OK")
    return address
def sanitize_phone(phone):
#    i = int
#    for i in phone:
#        i = ord(i)
#    if 46 <= i <= 57:
#        print ("It works!!")
    phone_with_spaces = phone
    allowed_symbols = "./\:()'+"
    numbers = "1234567890"
    phone = phone.replace(' ', '')
    for i in phone:
        if i not in allowed_symbols:
            if i not in numbers:
                print i
                print ("not number")
                print (i + "is invalid symbol for telephone number")
                print ("'" + i + "'" + " is invalid symbol for telephone number")
                return None
    print ("good")
    return phone_with_spaces

test1 = "363hfiw886"
test2 = "234(*^$"
test3 = "13452145"
test4 = "+29384)("
test5 = "34 39"

#print sanitize_address(test1)
#print sanitize_address(test2)
#print sanitize_phone(test2)
num = "2tyuf561794"
if num.isdigit():
    print ("is digit")
else:
    print ("not")
