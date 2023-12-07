from flask import Flask, redirect, url_for, request,render_template
import mysql.connector

PORT=5000

app = Flask(__name__)
file=open("Credentials.txt","r")
data=[]
for line in file:
   data.append(line.strip().split("=")[1])
file.close()
hostname=data[0]
username=data[1]
password=data[2]
database=data[3]


try:
    # Establish a connection to the MySQL database
   mydb = mysql.connector.connect(
    host=hostname,
    user=username,
    password=password,
    database=database
    )

   if mydb.is_connected():
      print("Connected to MySQL!")

   mycursor=mydb.cursor()

   #Handling requests to /api/books
   @app.route('/api/books',methods = ["GET","POST"])
   def getBooks():
       if request.method=="GET":
         mycursor.execute("SELECT * FROM books")
         data=mycursor.fetchall()
         return data
       elif request.method=="POST":
         json_data=request.json
         bname = json_data['bname']
         aname = json_data['aname']
         pyear = json_data['py']
         mycursor.execute("SELECT * FROM books where title=%s and author=%s and publication_year=%s",(bname,aname,pyear))
         data=mycursor.fetchone()
         if(data):
            return "Book already exists"
         else:
            sql = "INSERT INTO books (title, author,publication_year) VALUES (%s, %s,%s)"
            mycursor.execute(sql, (bname,aname,pyear))
            mydb.commit()
            return "Book was added to the database"

   #Handling requests to /api/books/{id}
   @app.route('/api/books/<int:iid>',methods = ["PUT"])
   def updateBooks(iid):
       if request.method=="PUT":
         bid = iid
         json_data=request.json
         bname = json_data['bname']
         aname = json_data['aname']
         pyear = json_data['py']
         print(bid)
         print(json_data)
         mycursor.execute("SELECT * FROM books where id=%s",(bid,))
         data=mycursor.fetchone()
         if(data):
            sql = "UPDATE books SET title = %s, author = %s, publication_year = %s WHERE id = %s"
            mycursor.execute(sql, (bname, aname, pyear, bid))
            mydb.commit()
            return "Book was updated"
         else:
            return "Book does not exist"

   app.run(debug=True,port=PORT)

except mysql.connector.Error as err:
   print(f"Connection error: {err}")









