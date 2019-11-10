from flask import Flask, render_template

from products.products_bp import products
from supermarkets.supermarkets_bp import supermarkets


app = Flask(__name__)
app.config['SECRET_KEY'] = 'super_secret_password'
app.register_blueprint(products)
app.register_blueprint(supermarkets)


@app.route('/')
def get_home():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)