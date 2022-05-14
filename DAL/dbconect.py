from mysql.connector import connect,Error
#--------------------------------------------- ####### connecting to Database
def Conecting():
    try:
        return connect(host="localhost",user="root",password="rezA13751996",database="db_libray")
    except Exception as error:
        return False
