from flask import ( Blueprint, render_template ) 

bp = Blueprint('facts_create', __name__, url_prefix="/facts")

@bp.route('/new')
def new(): 
    return render_template('new.html')