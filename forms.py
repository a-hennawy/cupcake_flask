from flask_wtf import FlaskForm
from wtforms import StringField, URLField, FloatField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, NumberRange

class new_cupcake_form(FlaskForm):
    flavor = StringField("Flavor", validators=[InputRequired()])
    size = StringField("Size", validators=[InputRequired()])
    rating = FloatField("Rating", validators=[InputRequired()])
    image = URLField("Cupcake image", validators=[Optional()])