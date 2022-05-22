##############################################################################
# Imports
from pymongo import MongoClient


##############################################################################
# Main
if __name__ == "__main__":
    HOST = "localhost:27017"
    with MongoClient(host=HOST) as client:
        print(f'Databases: {client.list_database_names()}')
