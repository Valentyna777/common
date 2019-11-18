from flask import Flask, render_template
from utils import get_data

app = Flask(__name__)

def words_count(data):
    return len(data.split(' '))


@app.route('/')
def get_home_page():
    return render_template("home.html", data=get_data())


@app.route('/alarm_clock')
def get_alarm_clock():
    page_name = get_data()[0]['title']
    page_text = get_data()[0]['text']
    page_words = words_count(page_text)
    return render_template('alarm_clock.html', page_name=page_name, page_text=page_text, page_words=page_words)


@app.route('/calculator')
def get_calculator():
    page_name = get_data()[3]['title']
    page_text = get_data()[3]['text']
    page_words = words_count(page_text)
    return render_template('calculator.html', page_name=page_name, page_text=page_text, page_words=page_words)


@app.route('/coffeemaker')
def get_coffeemaker():
    page_name = get_data()[4]['title']
    page_text = get_data()[4]['text']
    page_words = words_count(page_text)
    return render_template('coffeemaker.html', page_name=page_name, page_text=page_text, page_words=page_words)


@app.route('/headphones')
def get_headphones():
    page_name = get_data()[1]['title']
    page_text = get_data()[1]['text']
    page_words = words_count(page_text)
    return render_template('headphones.html', page_name=page_name, page_text=page_text, page_words=page_words)


@app.route('/iPod')
def get_iPod():
    page_name = get_data()[2]['title']
    page_text = get_data()[2]['text']
    page_words = words_count(page_text)
    return render_template('iPod.html', page_name=page_name, page_text=page_text, page_words=page_words)


@app.route('/recharger')
def get_recharger():
    page_name = get_data()[5]['title']
    page_text = get_data()[5]['text']
    page_words = words_count(page_text)
    return render_template('recharger.html', page_name=page_name, page_text=page_text, page_words=page_words)


@app.route('/author')
def get_author():
    return render_template('author.html')


if __name__ == "__main__":
    app.run(debug=True)
