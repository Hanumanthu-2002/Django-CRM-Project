import mysql.connector

dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Radhe@123'
    
)

#prepare a cursor object
cursor=dataBase.cursor()

#create a datab
cursor.execute("CREATE DATABASE elderco")
print("All Done!")