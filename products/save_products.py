
import requests
import json
from web_app import db, Product, Review

all_products = {}
r = requests.get('http://internal.ats-digital.com:3066/api/products')
all_products = r.json()

for p in all_products:
    prod = Product(product_name=p['productName'],
                   category=p['category'],
                   base_price=p['basePrice'],
                   image_url=p['imageUrl'],
                   brand=p['brand'],
                   details=p['details'],
                   material=p['productMaterial'],
                   delivery=p['delivery']
    )

    if len(p['reviews']) > 0:
        for review in p['reviews']:
            rev = Review(product=prod,
                         content=review['content'],
                         rating=review['rating']
            )
    else:
        pass

    db.session.add(prod)
    db.session.add(rev)
    db.session.commit()