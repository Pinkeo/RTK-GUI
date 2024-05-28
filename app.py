from flask import Flask, redirect, render_template, request
from waitress import serve

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




if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)
    app.run(debug=True)
