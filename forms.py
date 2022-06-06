from flask_wtf import FlaskForm
from wtforms import Form, StringField, FloatField, SubmitField, FileField
from wtforms.validators import Required


class formSplineImageVisualization(FlaskForm):
    t = StringField("Knots (t)", validators=[Required("Required value.")])
    c = StringField("Coefficient (c)", validators=[Required("Required value.")])
    k = StringField("Curve degree (k)", validators=[Required("Required value.")])
    image_file = FileField("Upload image", [])
    submit = SubmitField("Submit")
    
    