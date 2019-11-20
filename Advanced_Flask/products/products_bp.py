import json

from flask import Blueprint, request, render_template, session, abort
from wtforms import Form, IntegerField, FileField, StringField, validators

from products.get_data_from_json import get_prod_data

products = Blueprint('products', __name__, template_folder='templates')

product_list = list(get_prod_data())
last_product = product_list[-1]
last_id = last_product['id']


@products.route('/product', methods=['GET', 'POST'])
def get_prod():
    if request.args:
        for key, value in request.args.items():
            new_list = [i for i in product_list if i['price'] == int(value) or i['id'] == int(value)]
            if len(new_list) > 0:
                return render_template('all_products.html', data=new_list)
            else:
                abort(404)
    if request.method == 'GET':
        return render_template('all_products.html', data=product_list)


@products.route('/product/<int:id>', methods=["GET"])
def get_product(id):
    try:
        product = product_list[id-1]
        session[product['name']] = True
        return render_template("product.html", product=product)
    except IndexError:
        abort(404)


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
        new_product = {"id": last_id+1, "name": request.form['name'], "description": request.form['description'],
                       "img_name": request.files['img_name'].filename, "price": request.form['price']}
        product_list.append(new_product)
    return render_template('add_product.html', form=form)


@products.route('/clear_session', methods=['POST', 'GET'])
def clear_session():
    session.clear()
    return render_template("home.html")


@products.errorhandler(404)
def handle_404(error):
    return render_template('error_404.html')