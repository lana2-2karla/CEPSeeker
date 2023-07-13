from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class CEPForm(FlaskForm):
    cep = StringField('CEP', validators=[DataRequired()])
    submit = SubmitField('Buscar')

class IPForm(FlaskForm):
    ip = StringField('IP', validators=[DataRequired()])
    submit = SubmitField('Buscar')

