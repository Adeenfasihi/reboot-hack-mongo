from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello and welcome to my first <u>Django App</u> project!</h1>")

import pymongo
from django.conf import settings
my_client = pymongo.MongoClient(settings.DB_NAME)

# First define the database name
dbname = my_client['reboot_db']

# Now get/create collection name (remember that you will see the database in your mongodb cluster only after you create a collection)
collection_name = dbname["SME"]

#let's create two documents
sme_1 = {
    "Name": "Woodpecker",
    "Email" : "peckingLord@nest.com",
    "Password" : "penglings",
    "Post Code" : "BG12 32",
    "Industry": "Furniture",
    "Sector": "Woodwork"
}
sme_2 = {
    "Name": "Nirala Sweets",
    "Email" : "sweet@sweeter.sweetest",
    "Password" : "fooood",
    "Post Code" : "Ab12 32",
    "Industry": "Food",
    "Sector": "Catering"
}



collection_name.insert_many([medicine_1,medicine_2])

med_details = collection_name.find({})

for r in med_details:
	print(r["common_name"])

update_data = collection_name.update_one({'medicine_id':'RR000123456'}, {'$set':{'common_name':'Paracetamol 500'}})

count = collection_name.count()
print(count)

delete_data = collection_name.delete_one({'medicine_id':'RR000123456'})
