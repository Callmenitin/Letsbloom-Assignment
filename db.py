import mysql.connector

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
    mydb = mysql.connector.connect(
    host=hostname,
    user=username,
    password=password,
    database=database
    )
    if mydb.is_connected():
        print("Connection to MySQL established!")
    mycursor=mydb.cursor()
    sql = """CREATE TABLE books (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255),
        author VARCHAR(255),
        publication_year INT
    )"""
    mycursor.execute(sql)
    mydb.commit()
    book_data=[
    [1,"The C++ Programming Language","Bjarne Stroustrup",1985],
    [2,"Pride and Prejudice","Jane Austen",1813],
    [3,"The Alchemist","Bjarne Stroustrup",1988],
    [4,"Gone with the Wind"," Margaret Mitchell",1936],
    [5,"Harry Potter and the Philosopher's Stone","J.K. Rowling",1997]
    ]
    sql = "INSERT INTO books (title, author,publication_year) VALUES (%s, %s,%s)"
    for i in range(0,5):
        mycursor.execute(sql, (book_data[i][1], book_data[i][2],book_data[i][3]))
    mydb.commit()
    print("RECORDS INSERTED!!!!!!!!")
except mysql.connector.Error as err:
    print(f"Error: {err}")

