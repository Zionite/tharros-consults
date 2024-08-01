from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/book-coach')
def book_coach():
    return render_template('book_coach.html')


if __name__ == '__main__':
    app.run(debug=True)