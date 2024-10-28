import os
from dotenv import load_dotenv
from pyairtable import Api

#this is from loading the .env  file, which contains our AirTable API key.
load_dotenv() 
env_path = '/Users/ottaaccount/Pyton_Class/python-api-example/.env'#add r in the right side of = sign for windows custom according to your own path
load_dotenv(dotenv_path=env_path) # take environment variables from .env.
#section ends here for the dot env load

#testing_variable = os.getenv("TESTING_TOKEN")  just to test out  getting an environmental variable

#to get airtable api
#api_key = os.getenv("AIRTABLE_API_KEY")
#print(testing_variable)
#print(api_key)

api = Api(os.getenv("AIRTABLE_API_KEY"))#custom variable name in your dot env
print(api)
#table = api.table('appExampleBaseId', 'tblExampleTableId')
table = api.table('apptYkb7hxYFchrJA', 'tblYAreTaEsBGzRdG')#custom according to your own path
#table.all()
print(table.all())

#to get certain section to like Rating only or Book title
print(table.all()[0]['fields']['Rating'])
print(table.all()[0]['fields']['Book'])
print(table.all()[0]['fields']['Notes'])
