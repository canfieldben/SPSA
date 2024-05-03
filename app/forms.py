from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


# forms for input boxes

class StockForm(FlaskForm):
    stock = StringField('Stock Code', validators=[DataRequired()])  # stock ticker form
    company = StringField('Company Name (as referred to in social media)',
                          validators=[DataRequired()])  # company name form
    submit = SubmitField('Run Analysis')  # submit form
