import json

from flask import Blueprint, request, render_template, session
from flask_wtf import Form
from wtforms import validators, IntegerField, FileField, StringField

from products.get_data_from_json import get_prod_data

products = Blueprint('products', __name__, template_folder='templates')


@products.route('/product', methods=['GET', 'POST'])
def get_prod():
    if request.method == 'GET':
        data = get_prod_data()
        return render_template('all_products.html', data=data)


@products.route('/product/<int:id>', methods=["GET"])
def get_product(id):
    product = get_prod_data()[id-1]
    return render_template("product.html", product=product)


class AddForm(Form):
    id = IntegerField('id', validators=[validators.input_required()])
    name = StringField('name', validators=[validators.input_required()])
    description = StringField('description', validators=[validators.input_required()])
    price = IntegerField('price', validators=[validators.input_required()])
    img_name = FileField('img_name', validators=[validators.input_required()])


@products.route('/add_product', methods=['POST', 'GET'])
def add_product_form():
    form = AddForm()
    if request.method == 'POST':
        new_product = {"id": request.form['id'], "name": request.form['name'], "description": request.form['description'],
                       "img_name": request.files['img_name'].filename, "price": request.form['price']}
        json.dumps(new_product)
    return render_template('add_product.html', form=form)


@products.route('/clear_session', methods=['POST', 'GET'])
def clear_session():
    session.clear()
    return render_template("home.html")


@products.errorhandler(404)
def handle_404(error):
    return render_template('error_404.html')