import mysql.connector
from mysql.connector import errorcode

def sql_connection():
    """[Make SQL data-base connection]

    Returns:
        [Object]: [Object of database connection -- mysql.connector.connect]
    """
    try:
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Dharmvir@#123",
        database = "audiofileserver"
    )
        #print("koshishmemberandattendencedetails - Database is connected")
        print("Data_base connected")
        return mydb

    except mysql.connector.Error as e:
        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                return("Somthing wrong with user name and passward")
        elif e.errno == errorcode.ER_BAD_DB_ERROR:
                return("Databases not exist")
        else:
                return(e)


                