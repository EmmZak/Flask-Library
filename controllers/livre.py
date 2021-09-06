from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('Livre', __name__, url_prefix="/livre")

@bp.route('/show')
def show():
    return "livre"