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

#This query insert the data intothe database with given values
sql = "INSERT INTO student_data(student_id,student_name) VALUES ('%d','%s')"%(ID, Name)
cursor.execute(sql)
'''
try:
    cursor.execute(sql) # this execute the query
except:
    print("Data already exists")
'''

db.commit() #commit all changes
db.close()  #close the connection from database

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")
print ("<h4> Name %s with ID %d inserted in database</h4>"%(Name,ID))
print ("</body>")
print ("</html>")

