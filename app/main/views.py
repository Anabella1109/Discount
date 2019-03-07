from flask import render_template
from . import main
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    

    title = 'Home - Welcome to The best Blogs Review Website Online'

    return render_template('index.html', title = title)
@main.route('/access')
def accessories():

    '''
    View root page function that returns the index page and its data
    '''
   

    title = 'Home - Welcome to The best Blogs Review Website Online'

    return render_template('accessories.html', title = title)