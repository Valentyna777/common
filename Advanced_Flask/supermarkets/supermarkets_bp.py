from flask import Blueprint, request, render_template, session, abort
from wtforms import Form, IntegerField, StringField, FileField, validators

from supermarkets.get_data_from_json import get_super_data

supermarkets = Blueprint('supermarkets', __name__, template_folder='templates')

supermarket_list = list(get_super_data())
last_supermarket = supermarket_list[-1]
last_id = last_supermarket['id']


@supermarkets.route('/supermarket', methods=['GET', 'POST'])
def get_super():
    if request.args:
        for key, value in request.args.items():
            new_list = [i for i in supermarket_list if i['location'] == value]
            if len(new_list) > 0:
                return render_template('all_supermarkets.html', data=new_list)
            else:
                abort(404)
    elif request.method == 'GET':
        return render_template('all_supermarkets.html', data=supermarket_list)


@supermarkets.route('/supermarket/<int:id>', methods=["GET"])
def get_supermarket(id):
    try:
        supermarket = supermarket_list[id-1]
        session[supermarket['name']] = True
        return render_template("supermarket.html", supermarket=supermarket)
    except IndexError:
        abort(404)


class AddForm(Form):
    id = IntegerField('id', validators=[validators.input_required()])
    name = StringField('name', validators=[validators.input_required()])
    location = StringField('location', validators=[validators.input_required()])
    img_name = FileField('img_name', validators=[validators.input_required()])


@supermarkets.route('/add_supermarket', methods=['POST', 'GET'])
def add_supermarket_form():
    form = AddForm()
    if request.method == 'POST':
        new_supermarket = {"id": last_id+1, "name": request.form['name'], "location": request.form['location'],
                           "img_name": request.files['img_name'].filename}
        supermarket_list.append(new_supermarket)
    return render_template('add_supermarket.html', form=form)


@supermarkets.route('/clear_session', methods=['POST', 'GET'])
def clear_session():
    session.clear()
    return render_template("home.html")


@supermarkets.errorhandler(404)
def handle_404(error):
    return render_template('error_404.html')