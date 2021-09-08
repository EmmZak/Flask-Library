from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from models import db, User

bp = Blueprint('Auth', __name__, url_prefix="/")

@bp.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'GET':
        return render_template('login.html')
    
    return redirect('/')
    
