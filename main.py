import sys
sys.path.insert(0,"C:/Users/MohammadReza/Desktop/13_farvardin")
#---------------------------------------------------------------
from UI.user_interface import Form
from DAL.database_manager import DataBase_manager_book
#---------------------------------------------------------------
database1=DataBase_manager_book()
form1=Form(database1.get_all_products())

