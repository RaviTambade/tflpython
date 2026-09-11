import mysql.connector
# Connect to MySQL
dbConnection = mysql.connector.connect(host="localhost", user="root",  password="password", database="tflstudentdb")

dbCommand = dbConnection.cursor()

def  get_students():
    dbCommand.execute("SELECT * FROM student")
    result = dbCommand.fetchall()
    for row in result:
        print(row)


# DELETE
def delete_student():
    id = int(input("Enter ID: "))
    sql = "DELETE FROM student WHERE ID=%s"   #Query
    dbCommand.execute(sql, (id,))
    dbConnection.commit()
    print("Student deleted successfully")


# CREATE
def add_student():
    id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    email = input("Enter Email: ")

    sql = "INSERT INTO student (ID, Name, Email) VALUES (%s, %s, %s)"
    values = (id, name, email)

    dbCommand.execute(sql, values)
    dbConnection.commit()
    print("Student added successfully")


# UPDATE
def update_student():
    id = int(input("Enter ID: "))
    name = input("Enter new Name: ")
    email = input("Enter new Email: ")

    sql = "UPDATE student SET Name=%s, Email=%s WHERE ID=%s"
    values = (name, email, id)

    dbCommand.execute(sql, values)
    dbConnection.commit()

    print("Student updated successfully")


#menu
while True:
    print("\n1. Add Student")
    print("2. Show Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        get_students()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        break

    else:
        print("Invalid choice")

dbCommand.close()
dbConnection.close()



# Data Layer: MySQL database connection 
#             Creating database, inerting sample data,
#             Testing database using SQL commands, Join queires and Stored procedure 
#             from the prespective of DBA

# DAL "Data Access Layer"
#            from the perspective of a developer,
#            we will create a python application to connect to the database and
#            perform CRUD operations on the database.