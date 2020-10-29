from django.shortcuts import render
from pymongo import MongoClient
import json
from bson import json_util

#main function
def index(request):
    collection = connect()
    var = request.GET.get('search')
    data = str(var)
    result =CheckPalindrome(data)

    if var:
        if isNum(var) == True:
            product_list = list(collection.find({"id": int(var)}))
            if result == True:
                discount_promotion(product_list)
            context = {
                'product_list': product_list, 'palindrome': result
            }
            return render(request, 'walmart/index.html', context)

        else:
            regex_query = [{"brand": {"$regex": data}},{"description": {"$regex": data}}]
            product_list = list(collection.find({'$or': regex_query}))
            if result == True and len(data) > 3:
                discount_promotion(product_list)
            context = {
                'product_list': product_list, 'palindrome': result
            }
            return render(request, 'walmart/index.html', context)



    context = {
               'product_list':'', 'palindrome': ''
               }
    return render(request, 'walmart/index.html', context)

#Check if string its palindrome
def CheckPalindrome(data):
    lenght = len(data)
    condition = True
    math = int(lenght/2)
    for index in range(0, math):
        if data[index] != data[lenght-index-1]:
            condition = False
            break
    return condition
#Number Validation
def isNum(data):
    try:
        int(data)
        return True
    except ValueError:
        return False
#Discount Function
def discount_promotion(product_list):
    for product in product_list:
        product["discount"] = round(product["price"] / 2)
#Database Connection MongoDB
def connect():
    db_name = 'promotions'
    client = MongoClient('mongodb://productListUser:productListPassword@localhost:27017/')
    db_obj = client[db_name]
    collection = db_obj['products']
    return collection
