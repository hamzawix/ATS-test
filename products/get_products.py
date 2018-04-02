import requests
import json


all_products = {}
r = requests.get('http://internal.ats-digital.com:3066/api/products')
all_products = r.json()

product_keys = all_products
print(product_keys)

count = 1
for product in all_products:
    print("Num: {}".format(count))
    print("Name: {}".format(product['productName']))
    print("Details: {}".format(product['details']))
    print("Reviews: {}".format(product['reviews']))

    
    print("Brand: {}".format(product['brand']))
    print("Price: {}".format(product['basePrice']))
    print("Category: {}".format(product['category']))
    
    count +=1 
    print('----------------------------------------------')

print('--------Total products--------: {}'.format(count - 1))
