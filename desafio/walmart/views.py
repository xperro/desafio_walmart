from django.shortcuts import render
# Create your views here.
from walmart.models import products
import pymongo
from pymongo import MongoClient

def index(request):
    db_name = 'promotions'
    client = MongoClient('mongodb://productListUser:productListPassword@localhost:27017/')
    db_obj = client[db_name]
    collection = db_obj['products']
    data = str("ASA")
    result = CheckPalindrome(data)
    product_list = list(collection.find({"price":500}))
    context = {'product':product_list, 'msg': result}
    return render(request, 'walmart/index.html', context)

#Palindrome function to check if data recieved its palindrome (True is palindrome)
def CheckPalindrome(data):
    lenght = len(data)
    condition = True
    math = int(lenght/2)
    for index in range(0, math):
        if data[index] != data[lenght-index-1]:
            condition = False
            break
    return condition



