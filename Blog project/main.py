from flask import Flask, render_template, request
import requests


app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get('https://api.npoint.io/7b2d1e82343d9f69f19f')
    response_json = response.json()
    return render_template('index.html', posts=response_json)


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/contact')
def contact_page():
    return render_template('contact.html')


@app.route('/post/<id>')
def post_page(id):
    response = requests.get('https://api.npoint.io/7b2d1e82343d9f69f19f')
    response_json = response.json()
    return render_template('post.html', posts=response_json, num=int(id))


@app.route('/form-entry')
def receive_data():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']
    print(f'{name}\n{email}\n{phone}\n{message}')
    return '<h1> Successfully sent your message</h1>'


if __name__ == '__main__':
    app.run(debug=True)
