from dotenv import load_dotenv
import os
#if load_dotenv is empty like below, it's going to load .env in the same folder
load_dotenv() 

#if load_env filled with dotenv_path=env_path it will load the .env whichever it targetted to
env_path = '/Users/ottaaccount/Pyton_Class/.env'
load_dotenv(dotenv_path=env_path) # take environment variables from .env.


#testing_variable = os.getenv("TESTING_TOKEN") 
#AIRTABLE_API_KEY = os.getenv("AIRTABLE_API_KEY") 
#print(testing_variable)
#print(AIRTABLE_API_KEY)

test_Variable = os.getenv("testing")
print(test_Variable)