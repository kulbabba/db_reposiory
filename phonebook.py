#!/usr/bin/python

import MySQLdb
# Open database connection
#sql commands:

show_table_sql = """
    SELECT * from people;
    """
delete_from_table_sql = """DELETE FROM people
    WHERE id = %s;
    """

#functions
def actions_with_db(sql, comment_on_action):
    try:
        db = MySQLdb.connect("localhost","root","vtkmybr","phonebook")
        cursor = db.cursor()
        cursor.execute(sql)
        print comment_on_action
        db.commit()
        db.close()
    except:
        print ("There is a problem with the connection to database")

def sanitaze_name(name):
    if name.isalpha():
        return name

def sanitize_last_name(last_name):
    if last_name.isalpha():
        return last_name

def sanitize_address(address):
    allowed_symbols = "./()' "
    for symbol in address:
        if not symbol.isalpha():
            if symbol not in allowed_symbols:
                if not symbol.isdigit():
                    return None
    return address

def sanitize_phone(phone):
    allowed_symbols = ".()+ "
    for i in phone:
        if i not in allowed_symbols:
            if not i.isdigit():
                print ("'" + i + "'" + " is invalid symbol for telephone number")
                return None
    return phone

# In case of success return Null, in case of error return error string
# (Like "Forbidden symbols in name")
def add_person_to_db():
    name = sanitaze_name(raw_input("Please, enter person's name:  "))

    if not name:
        return "Error: forbidden symbols in name"

    last_name = sanitize_last_name(raw_input("Please, enter person's last name:  "))
    if not last_name:
        return "Error: forbidden symbols in last_name"

    address = sanitize_address(raw_input("Please, enter person's address:  "))
    if not address:
        return "Error: forbidden symbols in address"

    phone = sanitize_phone(raw_input("Please, enter person's phone number:  "))
    if not phone:
        return "Error: forbidden symbols in phone"

# XXX: move this closer to the beginning of a script

    insert_into_table_sql = """INSERT INTO people(name, last_name, address, phone) VALUES ('%s', '%s', '%s', '%s');""" % (name, last_name, address, phone)
# XXX: code duplication (database request). Move to separate function
    comment_on_action = ("A person with: \nname = %s, \nlast_name = %s, \naddress = %s, \nphone = %s is added.") % (name, last_name, address, phone)
    actions_with_db(insert_into_table_sql, comment_on_action)
#    try:
#        db = MySQLdb.connect("localhost","root","vtkmybr","phonebook")
#        cursor = db.cursor()
#        cursor.execute(insert_into_table_sql)
#        print ("A person with: \nname = %s, \nlast_name = %s, \naddress = %s, \nphone = %s is added.") % (name, last_name, address, phone)
#        db.commit()
#        db.close()
#    except:
#        print("There is a problem with the connction to database")
    return None

def delete_person():
    id_to_delete = (raw_input("Please, enter id of the person, that you want to delete from database:  "))
    id_to_deleteL = str("(" + id_to_delete + "L,)")
    try:
        x = int(id_to_delete) + 1
    except:
        print ("id can't include symbols or letters.")
        delete_person()
    delete = raw_input("The person with id %s will be deleted. Are you sure you want to continue? (yes/no)  " % (id_to_delete))
    if delete == "yes":
# XXX: move this closer to the beginning of a script
        select_id_from_table_sql = """SELECT id  FROM people"""
        print delete_from_table_sql % (id_to_delete)
# XXX: code duplication (database request). Move to separate function
        comment_on_action = ("A person with id %s is deleted") % (id_to_delete)
        actions_with_db(delete_from_table_sql, comment_on_action)
#        try:
#            db = MySQLdb.connect("localhost","root","vtkmybr","phonebook")
#            cursor = db.cursor()
#            cursor.execute(select_id_from_table_sql)
#            id_to_deleteL = str("(" + id_to_delete + "L,)")
#            for i in cursor:
#                i = str(i)
#                if  i == id_to_deleteL:
#                    cursor.execute(delete_from_table_sql)
#                    print ("A person with id %s is deleted") % (id_to_delete)
#                    return None

#            print ("there is no person with %s id") % (id_to_delete)
#            db.commit()
#            db.close()
#        except:
#            print ("There is a problem with the connection to database")
    else:
        delete_person()

def show_all_entries():
    print("cursor.execute(show_all_entries)")
# XXX: move this closer to the beginning of a script
    show_table_sql = """
    SELECT * from people;
    """
    print show_table_sql
# XXX: code duplication (database request). Move to separate function
    try:
        db = MySQLdb.connect("localhost","root","vtkmybr","phonebook")
        cursor = db.cursor()
        cursor.execute(show_table_sql)
#        for row in cursor:
#            print(row)
        data = cursor.fetchall()
        for row in data :
            print (row)

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
# XXX: move this closer to the beginning of a script
    new_phone_book_table_sql = """CREATE TABLE IF NOT EXISTS test_table
    (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    last_name varchar(255),
    address varchar(255),
    phone varchar(255),
    PRIMARY KEY (id)
)
"""

# XXX: code duplication (database request). Move to separate function
    try:
        db = MySQLdb.connect("localhost","root","vtkmybr","phonebook")
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        db.close()
    except:
        print ("There is a problem with the connection to database")

def main():
    create_table()
    take_user_input()

if __name__ == '__main__':
     main()

