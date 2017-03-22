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

#This query update the database with new name for given id
sql = "UPDATE student_data SET student_name=('%s') WHERE student_id=(%d)" %(Name,ID)

cursor.execute(sql) #this execute the query

row_affected=cursor.rowcount
def rowAffected():
    #this function checks whether this name is already in the database or not. If not then update the database and prints
    if row_affected != 0:
        print("ID=",ID,"Updated with Name=",Name,"in Database")
    else:
        print("ID=",ID, "is already updated with this name, No rows affected")

db.commit() #commit all changes
db.close() #close the connection from database

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")
rowAffected()   # calls the function for validation
print ("</body>")
print ("</html>")

