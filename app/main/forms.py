from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class UserInput(FlaskForm):
    first_name = StringField('', validators=[DataRequired(), Length(min=2, max=20)], render_kw={"placeholder":"Your Name"})
    second_name = StringField('', validators=[DataRequired(), Length(min=2, max=20)], render_kw={"placeholder":"Partner/Lover/Crush"})
    submit = SubmitField('Calculate')

class CountryPopulation(FlaskForm):
    country = StringField('', validators=[DataRequired()], render_kw={"Placeholder":"Country"})
    submit = SubmitField('Submit')

class CountryToCompare(FlaskForm):
    country_one = StringField('', validators=[DataRequired()], render_kw={"Placeholder":"First Country"})
    country_two = StringField('', validators=[DataRequired()], render_kw={"Placeholder":"Second Country"})
    submit = SubmitField('Submit')