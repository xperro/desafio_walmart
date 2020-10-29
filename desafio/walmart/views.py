from django.shortcuts import render
from pymongo import MongoClient
import json
from bson import json_util
def index(request):
    db_name = 'promotions'
    client = MongoClient('mongodb://productListUser:productListPassword@localhost:27017/')
    db_obj = client[db_name]
    collection = db_obj['products']
    print(collection)
    var = 181
    data = str(var)
    result =CheckPalindrome(data)
    print(result)

    if isNum(var):
        product_list = list(collection.find({"id": var}))

    else:
        regex_query = [{"brand": {"$regex": data}},{"description": {"$regex": data}}]
        product_list = list(collection.find({'$or': regex_query}))

    if result == True:
        for product in product_list:
            product["discount"] = round(product["price"]/2)

    context = {
               'product_list':product_list, 'palindrome': result
               }
    return render(request, 'walmart/index.html', context)


def CheckPalindrome(data):
    lenght = len(data)
    condition = True
    math = int(lenght/2)
    for index in range(0, math):
        if data[index] != data[lenght-index-1]:
            condition = False
            break
    return condition

def isNum(data):
    try:
        int(data)
        return True
    except ValueError:
        return False

