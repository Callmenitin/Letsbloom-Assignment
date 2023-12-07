REQUIREMENTS

Operating System: Windows 10/11
Python 3.11.0
flask-3.0.0 (if not already installed use command: pip install flask)
mysql-connector-python-8.2.0, (use command if not already installed:pip install mysql-connector-python)


STEPS

1. Open MySQL command line CLI, create database with name "mydb"
2. There is a Credentials.txt file, kindly change the details accordingly matching with your database except database name.
3. Then run db.py to seed the database with mock data, this is the first file you must run. Don't proceed without running it. 
4. Run server.py: python server.py
5. Default port of server is set to 5000, if this port is not available then change the port numner on line 4 in server.py
6. If you have changed the port on above step then kindly change the value of PORT varaible in below files at line number 4
	retrieve.py
	put.py
	post.py
	server.py


VIEW BOOKS:

Run retrieve.py file
	python retrieve.py

ADDING A NEW BOOK:

If you want to add new book then follow below steps

1. Open post.py
2. Enter book name on line 6
3. Enter author name on line 7
4. Enter Publication year on line 8
5. Run post.py
	python post.py
6. Verify the addition by running retrieve.py file
7. You will the error if you enter a book which already exists.


UPDATING AN EXISTING BOOK:

If you want to modify existing book then follow below steps

1. Open put.py
2. Enter book id on line 6
2. Enter book name on line 7
3. Enter author name on line 8
4. Enter Publication year on line 9
5. Run put.py
	python put.py
6. Verify the modification by running retrieve.py file
7. You will get an error if you try to modify book that does not exist


Please go through the report that includes the output screenshots.

