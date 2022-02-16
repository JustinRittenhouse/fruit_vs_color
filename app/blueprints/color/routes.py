from flask import render_template, Blueprint
from .import bp as color

# # Hamilton inspired this line with his project.
# color = Blueprint("color=", __name__)

@color.route('/red')
def red():
    # return render_template('red.html', title='Red')
    return "Some things are colors, like red."

@color.route('/yellow')
def blue():
    # return render_template('yellow.html', title='Yellow')
    return "Some things are colors, like yellow."

@color.route('/green')
def blue():
    # return render_template('green.html', title='Green')
    return "Some things are colors, like green."

@color.route('/blue')
def blue():
    # return render_template('blue.html', title='Blue')
    return "Some things are colors, like blue."

@color.route('/purple')
def blue():
    # return render_template('purple.html', title='Purple')
    return "Some things are colors, like purple."