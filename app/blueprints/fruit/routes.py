from flask import render_template, Blueprint
from .import bp as fruit

@fruit.route('/orange')
def orange():
    # return render_template('orange.html', title='Orange')
    return "Some things are fruits, like an orange."