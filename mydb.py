import mysql.connector

database = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'password123',
	)

cursorobject = database.cursor()

cursorobject.execute("CREATE DATABASE crm")

print("All Done!")