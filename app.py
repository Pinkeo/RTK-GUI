import os
from flask import Flask, redirect, render_template, request, url_for, flash
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('KEY')
secret_key = os.getenv('KEY')
print(f'Secret Key: {secret_key}')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    flash('You were redirected to the login page.')

    #return f'Hello, {name}!'
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)


