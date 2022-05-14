import sys
sys.path.insert(0,"C:/Users/MohammadReza/Desktop/13_farvardin")
#--------------------------------------------------------------
from DAL.dbconect import Conecting
from DAL.product import Book
#--------------------------------------------------------------
class DataBase_manager_book:
    def __init__(self) -> None:
        self.db=Conecting()
        self.mycursor=self.db.cursor()
    ################################################## Get all book 
    def get_all_products(self):
        self.mycursor.execute("Select * From books ")
        product=self.mycursor.fetchall() 
        return product
    ################################################## insert new book
    def insert_into_type1(self,product):
        self.mycursor.execute(f"Insert INTO books(Record,Help_number,Title,Author,Publishing_Specifications) Values('{product.record_number}','{product.help_number}','{product.title}','{product.author}','{product.publishing_Specifications}')")
        self.db.commit()
    ################################################## search book
    def search_into_type1(self,record):
        self.mycursor.execute(f"select * from books where Record={record}")
        result=self.mycursor.fetchall() 
        return result
    ################################################## delete 1 book
    def delete_1_record(self,record):
        self.mycursor.execute(f"delete From books where  Record={record}")
        self.db.commit()