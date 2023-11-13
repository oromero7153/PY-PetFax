from flask import ( Blueprint, render_template)
import json

pets = json.load(open('pets.json'))
print(pets)

#creating an instance
bp = Blueprint('pet',
               __name__, 
               url_prefix = '/pets')

#defining a route
@bp.route('/')
def index(): 
    return render_template ('index.html', pets=pets)
