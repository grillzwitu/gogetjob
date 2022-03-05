from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms_sqlalchemy.fields import QuerySelectField



class JobSearchForm(FlaskForm):
    keyword = StringField('Keyword', validators=[DataRequired(),
                                                 Length(max=30)])
    submit = SubmitField('Get Jobs')
