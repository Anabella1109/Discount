from flask import render_template
from ..models import  User,Product,Contact,Role,Transaction,Address,Location
# from ..request import get_quote
from . import main
# from .forms import AddPostForm,CommentForm,SubscriptionForm,UpdateForm
from ..import db,photos
# from flask_login import login_required,current_user
# from ..email import mail_message

@main.route('/' , methods = ['GET','POST'])
def index():

    '''
    View root page function that returns the index page and its data
    '''
   
    title = 'Utensils'

    return render_template('index.html', title = title)
    

@main.route('/utensils')
def utensils():
    
    
    title = 'utensils page'
    

    return render_template('utensils.html' , title = title)