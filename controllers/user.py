from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('User', __name__, url_prefix="/user")

@bp.route('/show')
def show():
    return "show"