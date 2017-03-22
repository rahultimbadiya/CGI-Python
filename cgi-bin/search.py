import cgi, cgitb
import mysql.connector

cgitb.enable()

db = mysql.connector.connect(host="localhost", user="root", password="root@123", database="student")

cursor = db.cursor()

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
ID = int(form.getvalue('ID'))

sql= "SELECT * FROM student_data WHERE student_id=%d" %ID

cursor.execute(sql)

row = cursor.fetchone()

db.commit()
cursor.close()

print ("Content-type:text/html\r\n\r\n")
print ("<html>")
print ("<head>")
print ("<title>Hello - Second CGI Program</title>")
print ("</head>")
print ("<body>")
print("<form action="+'"update.py"'+" method="+'"post"'+">")
#print(row[0],row[1])
print("<h4>Enter ID:<input type=text name=ID value=",row[0],"/></h4>")
print("<h4>Enter Name:<input type=text name=Name value=",row[1],"/></h4><br/>")
print("<input type=submit name=action value=Save />")
print("</form>")
print ("</body>")
print ("</html>")
