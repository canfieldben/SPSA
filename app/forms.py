from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class StockForm(FlaskForm):
    stock = StringField('Stock Code', validators=[DataRequired()])
    submit = SubmitField('Run Analysis')