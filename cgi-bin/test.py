import cgi, cgitb
import mysql.connector

cgitb.enable()

db = mysql.connector.connect(host="localhost", user="root", password="root@123", database="student")
cursor = db.cursor()

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
_id = int(form.getvalue('_id'))
_name  = form.getvalue('_name')

sql = "INSERT INTO student_data(student_id,student_name) VALUES ('%d','%s')"%(_id,_name)
cursor.execute(sql)
db.commit()
db.close()

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")
print ("<h2>Added %s with id %s</h2>" %(_name, _id))
print ("</body>")
print ("</html>")

