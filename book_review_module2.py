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
#table = api.table('apptYkb7hxYFchrJA', 'tblYAreTaEsBGzRdG')

#print(table.all())

#to get certain section to like Rating only or Book title
#print(table.all()[0]['fields']['Rating'])

class BookReview:
    def __init__(self):
        self.api=Api(os.getenv("AIRTABLE_API_KEY"))
        self.table = self.api.table('apptYkb7hxYFchrJA','tblYAreTaEsBGzRdG')

    def get_book_ratings(self):
        table =  self.table.all()
        return table
    def add_book_ratings(self, book_title, book_rating, notes=None):
        pass

if __name__  == "__main__":
    br = BookReview()
    print(br.get_book_ratings())