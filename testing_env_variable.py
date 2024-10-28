from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env.


testing_variable = os.getenv("AIRTABLE_TOKEN")
print(testing_variable)

#path = os.environ['PATH']
#print(path)
