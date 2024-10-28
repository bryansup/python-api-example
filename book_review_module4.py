import os
from dotenv import load_dotenv
from pyairtable import Api

#this is from loading the .env  file, which contains our AirTable API key.
load_dotenv() 
env_path = '/Users/ottaaccount/Pyton_Class/python-api-example/.env'
load_dotenv(dotenv_path=env_path) # take environment variables from .env.
#section ends here for the dot env load

#testing_variable = os.getenv("TESTING_TOKEN")  just to test out  getting an environmental variable

#to get airtable api
#api_key = os.getenv("AIRTABLE_API_KEY")
#print(testing_variable)
#print(api_key)

api = Api(os.getenv("AIRTABLE_API_KEY"))
print(api)

#table = api.table('appExampleBaseId', 'tblExampleTableId') inside is the airtable  base ID and table ID
base_id = str("apptYkb7hxYFchrJA")
table_id = str("tblYAreTaEsBGzRdG")
table = api.table(base_id, table_id)

#print(table.all())

#to get certain section to like Rating only or Book title
print(table.all()[0]['fields']['Rating'])

class BookReview:
    def __init__(self):
        self.api=Api(os.getenv("AIRTABLE_API_KEY"))
        self.table = self.api.table(base_id ,table_id)

    def get_book_ratings(self, sort = None, max_records=10):
        """if  not sort:
            return self.table.all(max_records=max_records)"""
        if sort  == "ASC":
            rating = ["Rating"]
        elif  sort == "DESC":
            rating = ["-Rating"] #from the big to small
        else  :
            return self.table.all(max_records=max_records)
        
        table =  self.table.all(sort=rating, max_records=max_records)
        return table

    def add_book_ratings(self, book_title, book_rating, notes=None):
        fields = {"Book":book_title, "Rating":book_rating, "Notes":notes}
        self.table.create(fields=fields)

if __name__  == "__main__":
    br = BookReview()
    get_book_ratings = br.get_book_ratings()
    
    #print(br.add_book_ratings("Fantastic Beast : and what they gossiping about",2, "Al about some beasts hanging around and gossiping about their neighbour"))
    """
    print(get_book_ratings)
    get_book_ratings = br.get_book_ratings(sort= "DESC")
    print(get_book_ratings)
    """
    get_book_ratings = br.get_book_ratings(sort= "ASC",max_records = 3)
    print(get_book_ratings)