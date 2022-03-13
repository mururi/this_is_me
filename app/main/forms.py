from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')

class NewPost(FlaskForm):
    content = TextAreaField('Your Post', validators=[DataRequired()])
    submit = SubmitField('Post')