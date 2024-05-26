from flask import Flask, redirect, render_template, request

app = Flask(__name__)

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
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run ()
    
