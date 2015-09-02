#!/usr/bin/python

import MySQLdb
# Open database connection

#sql commands:

sql_req_create_phonebook_table = """CREATE TABLE IF NOT EXISTS people
    (
    id int NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    last_name varchar(255),
    address varchar(255),
    phone varchar(255),
    PRIMARY KEY (id)
    )
    """
sql_req_show_people = """
    SELECT * from people;
    """
sql_req_delete_from_people = """DELETE FROM people
    WHERE id = {};
    """
sql_req_insert_into_people = """INSERT INTO people(name, last_name, address, phone) VALUES ('%s', '%s', '%s', '%s');"""

#functions

db_host = "localhost"
db_user = "root"
db_pass = "vtkmybr"
db_database = "phonebook"

# XXX: get rid of comment_on_action, and return status code from function
def actions_with_db(sql, host, user, password, database):
    try:
        db = MySQLdb.connect(host, user, password, database)
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        db.close()
    except:
        return "Some error"

    return None

# err = actions_with_db(sql)
# if err != Null:
#     print(err)
#     return 1

def sanitize_name(name):
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
    name = sanitize_name(raw_input("Please, enter person's name:  "))

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

# XXX: move this closer to the beginning of a script(!!?)

    request = sql_req_insert_into_people  % (name, last_name, address, phone)
    comment_on_action = ("A person with: \nname = %s, \nlast_name = %s, \naddress = %s, \nphone = %s is added.") % (name, last_name, address, phone)
    err = actions_with_db(request, db_host, db_user, db_pass, db_database)
    if err:
        print("Error: {}".format(err))
        return err

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
# XXX: move this closer to the beginning of a script(!!?)
        id_to_delete = int(id_to_delete)
        comment_on_action = ("A person with id %s is deleted") % (id_to_delete)
        err = actions_with_db(sql_req_delete_from_people.format(id_to_delete), db_host, db_user, db_pass, db_database)
        if err:
            print("Error: {}".format(err))
            return err
    else:
        delete_person()

def show_all_entries():
    print("cursor.execute(show_all_entries)")
# XXX: code duplication (database request). Move to separate function
#    actions_with_db(sql_req_show_people, comment_on_action)
    try:
        db = MySQLdb.connect(db_host, db_user, db_pass, db_database)
        cursor = db.cursor()
        cursor.execute(sql_req_show_people)
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

    err = actions_with_db(sql_req_create_phonebook_table, db_host, db_user, db_pass, db_database)
    if err:
        print("Error: {}".format(err))
        return err
def main():
    create_table()
    take_user_input()

if __name__ == '__main__':
     main()

