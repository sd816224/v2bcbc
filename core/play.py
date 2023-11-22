from dotenv import load_dotenv
import os


# Load variables from .env file
load_dotenv()

# Get the value of a variable
if os.getenv('DS_DB_NAMEs'):
    print('yes')
else:
    print('no')

# Use the variable


