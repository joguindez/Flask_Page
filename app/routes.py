from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index(): 
    user = {'username': 'Jordan'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beutiful day in Portland'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Average movie was so cool!'
        },
        {
            'author': {'username': 'Steven'},
            'body': "it's a really cold day "
        },
        {
            'author': {'username': 'Carlos'},
            'body': 'I really like working with flask in Python'
        },
        {
            'author': {'username': 'Monique'},
            'body': 'Are there any good places to eat in downtown Portland'
        },
        {
            'author': {'username': 'Bruce'},
            'body': 'Have anyone tried the new hooks in React.js?'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)