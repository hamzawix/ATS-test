from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from wtforms import TextField, SubmitField
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///product_db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = "sdlfsdf5é'é'''(454dfsdfsdf)"
db = SQLAlchemy(app)

#Database models
class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)

    product_name = db.Column(db.String(100))
    category = db.Column(db.String(100))
    base_price = db.Column(db.Integer)
    image_url = db.Column(db.String(250))
    brand = db.Column(db.String(100))
    details = db.Column(db.String(100))
    material = db.Column(db.String(100))
    delivery = db.Column(db.String(100))

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True)

    product_id = db.Column(db.Integer, db.ForeignKey('products.id'),
        nullable=False)

    product = db.relationship('Product',
        backref=db.backref('reviews', lazy=True))

    content = db.Column(db.Text)
    rating = db.Column(db.Integer)


#Product form
class ProductForm(FlaskForm):
    name = TextField('Product Name')
    category = TextField('Category')
    price = TextField('Base Price')
    image = TextField('Image URL')
    brand = TextField('Brand')
    material = TextField('Material')
    delivery = TextField('Delivery')
    submit = SubmitField('Submit')

# routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def list_products():
    products = Product.query.all()
    return render_template('list.html',products=products)

@app.route('/products/detail/<int:id>')
def detail_product(id):
    product = Product.query.get(id)
    return render_template('detail.html', product=product)


@app.route('/products/new', methods=['GET', 'POST'])
def new_product():
    form = ProductForm()
    if request.method == 'POST':
        new = Product(
                product_name=form.name.data,
                category=form.category.data,
                base_price=form.price.data,
                image_url=form.image.data,
                brand=form.brand.data,
                material=form.material.data,
                delivery=form.delivery.data
        )
        db.session.add(new)
        db.session.commit()
        return redirect('/products')
    return render_template('new.html', form=form)

@app.route('/products/statistics')
def statistics():
    prods = Product.query.all()

    # number of products
    n_prods = len(prods)
    
    # Get total ratings for each product
    dict_list = []
    for p in prods:
        rev_dict = dict()
        total_revs = 0
        for rev in p.reviews:
            total_revs += rev.rating
        
        rev_dict = {
            'product': p,
            'total_rating': total_revs
        }
        dict_list.append(rev_dict)

    #Get best product
    best_rev = 0
    best_product = dict()
    for d in dict_list:
        if d['total_rating'] > best_rev:
            best_rev = d['total_rating']
            best_product = {
                'product': d['product'],
                'rating': best_rev
            }

    #Get worst product
    worst_rev = 27
    worst_product = dict()
    for d in dict_list:
        if d['total_rating'] <= worst_rev:
            worst_rev = d['total_rating']
            worst_product = {
                'product': d['product'],
                'rating': worst_rev
            }

    return render_template('stat.html', n_prods=n_prods,
                                        best_product=best_product,
                                        worst_product=worst_product
                                        )

@app.route('/products/statistics/chartdata')
def chartdata():
    prods = Product.query.all()
    dict_count = dict()
    # Get total ratings for each product
    dict_list = []
    for p in prods:
        rev_dict = dict()
        total_revs = 0
        for rev in p.reviews:
            total_revs += rev.rating
        
        rev_dict = {
            'product': p,
            'total_rating': total_revs
        }
        dict_list.append(rev_dict)

    #get count ratings
    count0_10 = 0
    count11_20 = 0
    count21_30 = 0

    rating0_10 = [i for i in range(11)]
    rating11_20 = [i for i in range(11, 21)]
    rating21_30 = [i for i in range(21, 31)]
    for d in dict_list:
        if d['total_rating'] in rating0_10:
            count0_10 += 1

        if d['total_rating'] in rating11_20:
            count11_20 += 1

        if d['total_rating'] in rating21_30:
            count21_30 += 1

    dict_count = {
        'count0_10': count0_10,
        'count11_20': count11_20,
        'count21_30': count21_30
    }

    return jsonify(dict_count)


if __name__ == "__main__":
    db.create_all()
    app.run(host="localhost", port=3000)