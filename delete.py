import pymongo
import ssl
from datetime import date
import pandas as pd

myclient = pymongo.MongoClient("mongodb+srv://afridi:afridi0153@cluster0.ekt0p.mongodb.net/test",ssl_cert_reqs=ssl.CERT_NONE)
mydb = myclient["Bank_App"]

mycol = mydb["user"]
myquery = { "_id": input("Enter Nid to delete") }

mycol.delete_one(myquery)