from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def get_home():
    return render_template('home.html')


@app.route("/vegetables")
def get_vegetables():
    veg_list = ['beans', 'carrot', 'beetroot', 'cucumber']
    return render_template('vegetables.html', list=veg_list)


@app.route("/fruits")
def get_fruits():
    fruit_list = ['melon', 'apple', 'strawberry', 'grape']
    return render_template('fruits.html', list=fruit_list)


if __name__ == "__main__":
    app.run(debug=True)