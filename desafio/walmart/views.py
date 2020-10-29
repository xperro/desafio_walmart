from django.shortcuts import render
#main function
from . import helpers


def index(request):
    collection = helpers.connect()
    var = request.GET.get('search')
    data = str(var)
    result =helpers.CheckPalindrome(data)

    if var:
        if helpers.isNum(var) == True:
            product_list = list(collection.find({"id": int(var)}))
            if result == True:
                helpers.discount_promotion(product_list)
            context = {
                'product_list': product_list, 'palindrome': result
            }
            return render(request, 'walmart/index.html', context)

        else:
            regex_query = [{"brand": {"$regex": data}},{"description": {"$regex": data}}]
            product_list = list(collection.find({'$or': regex_query}))
            if result == True and len(data) > 3:
                helpers.discount_promotion(product_list)
            context = {
                'product_list': product_list, 'palindrome': result
            }
            return render(request, 'walmart/index.html', context)



    context = {
               'product_list':'', 'palindrome': ''
               }
    return render(request, 'walmart/index.html', context)
