from flask_wtf import FlaskForm
from wtforms import  StringField,PasswordField,SubmitField,BooleanField,FloatField
from wtforms.validators import DataRequired


# create fields for each variable 
class Inputform(FlaskForm):
    sl = FloatField('SEPAL LENGTH',validators=[DataRequired()])
    sw = FloatField('SEPAL WIDTH',validators=[DataRequired()])
    pl = FloatField('PETAL LENGTH',validators=[DataRequired()])
    pw = FloatField('PETAL WIDTH',validators=[DataRequired()])
    submit = SubmitField('PREDICT')