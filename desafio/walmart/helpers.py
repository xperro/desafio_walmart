import pymongo
from pymongo import MongoClient

#Check if string its palindrome
def CheckPalindrome(data):
    lenght = len(data)
    if len(data)>0:
        condition = True
        math = int(lenght/2)
        for index in range(0, math):
            if data[index] != data[lenght-index-1]:
                condition = False
                break
        return condition
    return False
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
        product["discount"] = round(discount(product["price"]))
def discount(price):
    return round(price / 2)
#Database Connection MongoDB
def connect():
    db_name = 'promotions'
    try:
        client = MongoClient('mongodb://productListUser:productListPassword@localhost:27017/')
        db_obj = client[db_name]
        collection = db_obj['products']
    except pymongo.errors.ServerSelectionTimeoutError as err:
        print(err)
        return False
    return collection

def integration_test_function(data):
    collection = connect()
    var = data
    data = str(var)
    result = CheckPalindrome(data)

    if var:
        if isNum(var) == True:
            product_list = list(collection.find({"id": int(var)}))
            if result == True:
                discount_promotion(product_list)

            return product_list

        else:
            regex_query = [{"brand": {"$regex": data}}, {"description": {"$regex": data}}]
            product_list = list(collection.find({'$or': regex_query}))
            if result == True and len(data) > 3:
                discount_promotion(product_list)

            return product_list
