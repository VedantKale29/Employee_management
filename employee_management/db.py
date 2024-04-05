import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "vuk@2004"
)

cursorObj = dataBase.cursor()

cursorObj.execute("CREATE DATABASE employee")

print("All done!")