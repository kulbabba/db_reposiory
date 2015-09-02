#!/usr/bin/python

import MySQLdb
# Open database connection


    #XXX: delete commented lines if not needed, in case if needed write comment why it was commented ))
#db = MySQLdb.connect("localhost","root","vtkmybr","just_database" )

# prepare a cursor object using cursor() method
#cursor = db.cursor()

# Drop table if it already exist using execute() method.
#cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Create table as per requirement
#sql = """CREATE TABLE EMPLOYEE (
#         FIRST_NAME  CHAR(20) NOT NULL,
#         LAST_NAME  CHAR(20),
#         AGE INT,
#         INCOME FLOAT )"""

#cursor.execute(sql)


#functions

def sanitaze_name(name):
# XXX: why spaces?
    if name.replace(' ', '').isalpha():
        return name

def sanitize_last_name(last_name):
# XXX: why spaces?
    if last_name.replace(' ', '').isalpha():
        return last_name

def sanitize_address(address):
# XXX: remove backslash and semicolon (\,:) from allowed_symbols
    allowed_symbols = "./\:()'"
    numbers = "1234567890"
    # XXX: why do you need this?
    symbol = str
    # XXX: what exactly this cycle does???
    for i in address:
        symbol = i
    if symbol.isalpha() or symbol in allowed_symbols or symbol in numbers:
    #XXX: delete commented string if not needed, in case if needed write comment why it was commented ))
#        if not address.isalpha and address not in allowed_symbols and numbers:
        return address
    else:
        return None

def sanitize_phone(phone):
# XXX: why do you need this? why don't just add space to allowed_symbols?
    phone_with_spaces = phone
    allowed_symbols = "./\:()'+"
    numbers = "1234567890"
    # XXX: if to add space to allowed_symbols then you don't need this, right?
    phone = phone.replace(' ', '')
    for i in phone:
        if i not in allowed_symbols:
            # XXX: why don't use something like str(i).isdigit()?
            if i not in numbers:
                print ("'" + i + "'" + " is invalid symbol for telephone number")
                return None
    return phone_with_spaces

# In case of success return Null, in case of error return error string
# (Like "Forbidden symbols in name")
def add_person_to_db():
# XXX: do we need forbidden_symbol ?
    forbidden_symbol = "!@#$%^&*()1234567890_-+="
    name = sanitaze_name(raw_input("Please, enter person's name:  "))

    if not name:
        return "Error: forbidden symbols in name"

    #XXX: delete commented lines if not needed, in case if needed write comment why it was commented ))
#    if ";" or "$" or "!" or "%" or "*" or "^" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "0" in name:
#        name = raw_input("Your name should include only letters! Please, enter valid name:  ")
#    for i in forbidden_symbol:
#        if i in forbidden_symbol:
#        if i in name:
#    if not name.replace(' ', '').isalpha():
#            print ("Your name should include only letters!")
#            add_person_to_db()

    last_name = sanitize_last_name(raw_input("Please, enter person's last name:  "))
    if not last_name:
        return "Error: forbidden symbols in last_name"

    address = sanitize_address(raw_input("Please, enter person's address:  "))
    if not address:
        return "Error: forbidden symbols in address"

    phone = sanitize_phone(raw_input("Please, enter person's phone number:  "))
    if not phone:
        return "Error: forbidden symbols in phone"

# XXX: rename sql variable to something more appropriate
# XXX: move this closer to the beginning of a script
    sql = """INSERT INTO people(name, last_name, address, phone) VALUES ('%s', '%s', '%s', '%s');""" % (name, last_name, address, phone)

    #XXX: delete commented lines if not needed, in case if needed write comment why it was commented ))
#    print sql
# XXX: code duplication (database request). Move to separate function
    try:
        db = MySQLdb.connect("localhost","root","vtkmybr","phonebook")
        cursor = db.cursor()
        cursor.execute(sql)
        print ("A person with: \nname = %s, \nlast_name = %s, \naddress = %s, \nphone = %s is added.") % (name, last_name, address, phone)
        db.commit()
        db.close()
    except:
        print("There is a problem with the connction to database")
    #XXX: delete commented lines if not needed, in case if needed write comment why it was commented ))
 #            return None
    return None

def delete_person():
    id_to_delete = (raw_input("Please, enter id of the person, that you want to delete from database:  "))
    try:
        x = int(id_to_delete) + 1
    except:
        print ("id can't include symbols or letters.")
        delete_person()
    delete = raw_input("The person with id %s will be deleted. Are you sure you want to continue? (yes/no)  " % (id_to_delete))
    if delete == "yes":
# XXX: rename sql, sql_select variable to something more appropriate
# XXX: move this closer to the beginning of a script
        sql_select = """SELECT id  FROM people"""
        sql = """DELETE FROM people
        WHERE id = '%s';
        """ % (id_to_delete)
# XXX: code duplication (database request). Move to separate function
        try:
            db = MySQLdb.connect("localhost","root","vtkmybr","phonebook")
            cursor = db.cursor()
            cursor.execute(sql_select)
            if id_to_delete in cursor:
                cursor.execute(sql)
                print ("A person with id %s is deleted") % (id_to_delete)
            else:
                print ("there is no person with %s id") % (id_to_delete)
                delete_person()
    #XXX: delete commented lines if not needed, in case if needed write comment why it was commented ))
#            cursor.execute(sql_select)
#            for row in cursor:
#                print row
            db.commit()
            db.close()
        except:
            print ("There is a problem with the connection to database")
    else:
        delete_person()

def show_all_entries():
    print("cursor.execute(show_all_entries)")
# XXX: rename sql variable to something more appropriate
# XXX: move this closer to the beginning of a script
    sql = """
    SELECT * from people;
    """
    print sql
# XXX: code duplication (database request). Move to separate function
    try:
        db = MySQLdb.connect("localhost","root","vtkmybr","phonebook")
        cursor = db.cursor()
        cursor.execute(sql)
    #XXX: delete commented lines if not needed, in case if needed write comment why it was commented ))
    #for row in cursor.execute(sql):
     #   name, last_name, address, phone = row
    #result_set = cursor.fetchall()
    #for row in result_set:
    #    print "%s, %s, %s, %s" % (row["name"], row["last_name"], row["address"], row["phone"])
    #cursor.execute("SELECT name, last_name, address, phone FROM people")
    #row = dict(zip(cursor.column_names, cursor.fetchone()))
    #print("{name}, {last_name}".format(row))
    #cursor.execute("SELECT * FROM people")
        for row in cursor:
            print(row)
        data = cursor.fetchall()
        for row in data :
            print (row)

    #XXX: delete commented lines if not needed, in case if needed write comment why it was commented ))
#    for i in cursor:
#        maxlength = max(len(s) for s in cursor)
#        row_diff = " " * (maxlength - len(row)
#        print (row + row_diff)
        db.commit()
        db.close()
    except:
        print "There is a problem with the connectin to database!"

user_prompt = """Choose action:
1)add person's info to database;
2)delete person's info from database;
3)show all addressbook entries with all the info
""";

def take_user_input():
    user_input = int(raw_input(user_prompt))

    if user_input == 1:
        add_person_to_db();
    elif user_input == 2:
        delete_person();
    elif user_input == 3:
        show_all_entries();
    else:
        print "There is no such option."
        take_user_input()

def create_table():
# XXX: why 'phone' column name has type 'int'?
# XXX: rename sql variable to something more appropriate, like new_addr_book_table_req
# XXX: move this closer to the beginning of a script
    sql = """CREATE TABLE IF NOT EXISTS test_table
    (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    last_name varchar(255),
    address varchar(255),
    phone int(255),
    PRIMARY KEY (id)
)
"""

    #XXX: delete commented lines if not needed, in case if needed write comment why it was commented ))
#    print sql
# XXX: no try() {} except block - need to catch exceptions
# XXX: code duplication (database request). Move to separate function
    db = MySQLdb.connect("localhost","root","vtkmybr","phonebook")
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    db.close()

def main():
# XXX: create_table() should go first
    take_user_input()
    create_table()

    #XXX: delete commented lines if not needed, in case if needed write comment why it was commented ))
# disconnect from server
#db.close()

if __name__ == '__main__':
     main()

