import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Mutemath966@"
)

#Cretae a database
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE firstdb")