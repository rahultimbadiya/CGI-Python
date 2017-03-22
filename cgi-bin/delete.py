import cgi, cgitb
import mysql.connector

cgitb.enable()

#this function will authenticate server and then connect with the database
db = mysql.connector.connect(host="localhost", user="root", password="root@123", database="student")
cursor = db.cursor()

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
ID = int(form.getvalue('ID'))
Name = form.getvalue('Name')

#This query delete the data from the database with given id
sql = "DELETE FROM student_data WHERE student_id=(%d)"% (ID)


cursor.execute(sql) #this execute the query

row_affected=cursor.rowcount
def rowAffected():
    # this function checks whether this name is already deleted from database or not. If not then delete from database and prints
    if row_affected != 0:
        print("ID=",ID,"Deleted")
    else:
        print("ID=",ID, "is already deleted, No rows affected")

db.commit() #commit all changes
db.close() #close the connection from database

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")
rowAffected()  # calls the function for validation
print ("</body>")
print ("</html>")

