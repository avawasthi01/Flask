from distutils.log import debug
import re
from urllib import request
from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/review')
def review():
    status=False
    name=request.args.get('name')
    password=request.args.get('password')
    rgx = re.compile(r'\d.*?[A-Z].*?[a-z]') 
    if rgx.match(''.join(sorted(password))) and len(password) >= 7:
        status=True
    return render_template('review.html',name=name,status=status)


if __name__ == '__main__':
    app.run(debug = True)
