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
    "Id" : 0x00,
    "Name": "Woodpecker",
    "Email" : "peckingLord@nest.com",
    "Password" : "penglings",
    "Post Code" : "BG12 32",
    "Industry": "Furniture",
    "Sector": "Woodwork",
    "Network": ""
}
sme_2 = {
    "Id": 0x01,
    "Name": "Nirala Sweets",
    "Email" : "sweet@sweeter.sweetest",
    "Password" : "fooood",
    "Post Code" : "Ab12 32",
    "Industry": "Food",
    "Sector": "Catering",
    "Network": "Sugar Cubez,A Onion"
}

sme_3 = {
    "Id": 0x02,
    "Name": "Sugar Cubez",
    "Email" : "sugar@SuarCubers.com",
    "Password" : "YUM",
    "Post Code" : "NM24 64",
    "Industry": "Food",
    "Sector": "Catering",
    "Network": "Nirala Sweets,A Onion"
}

sme_4 = {
    "Id": 0x03,
    "Name": "A ONION",
    "Email" : "A@onion.com",
    "Password" : "OP_Onion",
    "Post Code" : "KL23 56",
    "Industry": "Food",
    "Sector": "Catering",
    "Network": "Sugar Cubez,Nirala Sweets"

}

sme_5 = {
    "Id": 0x04,
    "Name": "Real Steel",
    "Email" : "steel@seelt",
    "Password" : "fire",
    "Post Code" : "lm12 32",
    "Industry": "Raw Materials",
    "Sector": "Metals",
    "Network": "Marble Works"
}

sme_6 = {
    "Id": 0x05,
    "Name": "Marble Works",
    "Email" : "marblez@fishy.com",
    "Password" : "stone",
    "Post Code" : "pb12 32",
    "Industry": "Raw Materials",
    "Sector": "Metals",
    "Network": "Real Steel"
}


collection_name.insert_many([])

med_details = collection_name.find({})

for r in med_details:
	print(r["common_name"])

update_data = collection_name.update_one({'medicine_id':'RR000123456'}, {'$set':{'common_name':'Paracetamol 500'}})

count = collection_name.count()
print(count)

delete_data = collection_name.delete_one({'medicine_id':'RR000123456'})
