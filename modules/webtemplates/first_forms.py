from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField
from wtforms.validators import Required



class Dataform(FlaskForm):
    numberone = TextField('numberone', validators = [Required()])
    numbertwo = TextField('numbertwo', validators=[Required()])
