from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('Tag', __name__, url_prefix="/tag")

@bp.route('/show')
def show():
    return "tag"