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
#print(table.all()[0]['fields']['Book'])
#print(table.all()[0]['fields']['Notes'])

class BookReview:
    def __init__(self):
        #setting up authentication API key and which airtable documents
        self.api=Api(os.getenv("AIRTABLE_API_KEY")) #ini authentication ke airtablenya supaya bisa akses
        self.table = self.api.table('apptYkb7hxYFchrJA','tblYAreTaEsBGzRdG') # menghubungi airtable yang mana

    def get_book_ratings(self): #store all data from airtable in a variable called table then return the value of it
        table =  self.table.all()
        return table
    def add_book_ratings(self, book_title, book_rating, notes=None):
        fields = {"Book":book_title, "Rating":book_rating, "Notes":notes}
        self.table.create(fields=fields)

if __name__  == "__main__":
    br = BookReview()
    get_book_ratings = br.get_book_ratings()
    #print(br.add_book_ratings("Fantastic Beast : and what they gossiping about",2, "Al about some beasts hanging around and gossiping about their neighbour"))
#    print(br.add_book_ratings("Wilson and Fantastic Beast and how to tame them",9.5,"About Wilson catching pokemons"))
    print(br.add_book_ratings("Gavin Radiant Guide series 100",100,"Get to radiant under 1 seconds"))
    print(br.get_book_ratings())
    
