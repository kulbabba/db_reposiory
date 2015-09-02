
#!/usr/bin/python
birds = ["dove", "parrot", "hen"]
animal = ["monkey", "dolphin", "giraff"]
numbers = ["1", "5", "8"]
n = [ birds, animal, numbers]
print n
for t in n:
    num = 0
#    for i in cursor:
#        maxlength = max(len(s) for s in cursor)
#        row_diff = " " * (maxlength - len(row)
#        print (row + row_diff)
def add_person_to_db():
    forbidden_symbol = "!@#$%^&*()1234567890_-+="
    name = raw_input("Please, enter person's name:  ")
    for i in name:
        if i in forbidden_symbol:
            print "yes"
            name = raw_input("Your name should include only letters! Please, enter valid name:  ")
        else:
            print "no"
 #   if ";" or "$" or "!" or "%" or "*" or "^" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0" in name:
        print name
        last_name = raw_input("Please, enter person's last name:  ")
        address = raw_input("Please, enter person's address:  ")
        phone = raw_input("Please, enter person's phone number:  ")

    print ("name = %s, last_name = %s, address = %s, phone = %s ") % (name, last_name, address, phone)

print add_person_to_db()
