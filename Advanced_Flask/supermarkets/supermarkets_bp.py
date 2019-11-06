import json

from flask import Blueprint, request, render_template, session
from flask_wtf import Form
from wtforms import IntegerField, StringField, FileField, validators

from supermarkets.get_data_from_json import get_super_data

supermarkets = Blueprint('supermarkets', __name__, template_folder='templates')


@supermarkets.route('/supermarket', methods=['GET', 'POST'])
def get_super():
    if request.method == 'GET':
        data = get_super_data()
        return render_template('all_supermarkets.html', data=data)


@supermarkets.route('/supermarket/<int:id>', methods=["GET"])
def get_supermarket(id):
    supermarket = get_super_data()[id-1]
    session[supermarket['name']] = True
    return render_template("supermarket.html", supermarket=supermarket)


class AddForm(Form):
    id = IntegerField('id', validators=[validators.input_required()])
    name = StringField('name', validators=[validators.input_required()])
    location = StringField('location', validators=[validators.input_required()])
    img_name = FileField('img_name', validators=[validators.input_required()])


@supermarkets.route('/add_supermarket', methods=['POST', 'GET'])
def add_supermarket_form():
    form = AddForm()
    if request.method == 'POST':
        new_supermarket = {"id": request.form['id'], "name": request.form['name'], "location": request.form['location'],
                           "img_name": request.files['img_name'].filename}
        json.dumps(new_supermarket)
    return render_template('add_supermarket.html', form=form)


@supermarkets.route('/clear_session', methods=['POST', 'GET'])
def clear_session():
    session.clear()
    return render_template("home.html")


@supermarkets.errorhandler(404)
def handle_404(error):
    return render_template('error_404.html')