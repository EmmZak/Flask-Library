from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from models import db, Tag, Livre, Auteur, User

bp = Blueprint('Main', __name__, url_prefix="/")

def get_prev_next(page, pages):
    if page - 1 <= 0:
        prev = 1
    else:
        prev = page - 1

    if page + 1 > pages:
        next = page
    else:
        next = page + 1
    return prev, next

@bp.route('/')
def index(elements=None):
    page = request.args.get('page', 1, type=int)
    
    elements = request.args.get('elements', None)
    if elements:
        elements = int(elements)
    else:
        elements = 2
    """
    page = request.args.get('page', None)
    if page:
        page = int(page)
    else:
        page = 1
    """
    sort = request.args.get('sort', None)
    if not sort:
        sort = "asc"

    pages = Livre.query.count() / elements 
    if not pages.is_integer():
        pages = int(pages) + 1

    prev, next = get_prev_next(page, pages)

    print(page, elements)
    livres = Livre.query.paginate(page=page, per_page=elements).items
    print(livres, len(livres))

    data = {
        'elements': elements,
        'sort': sort,
        'page': page,
        'pages': pages,
        'next': next,
        'prev': prev,
        'tags': Tag.query.all(),
        'auteurs': Auteur.query.all(),
        'livres': livres,
    }

    return render_template('home.html', **data)