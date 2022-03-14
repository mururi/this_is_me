from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField
from wtforms.validators import DataRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [DataRequired()])
    submit = SubmitField('Submit')

class NewPost(FlaskForm):
    content = TextAreaField('Your Post', validators=[DataRequired()])
    submit = SubmitField('Post')

class NewComment(FlaskForm):
    author = StringField('Your Name', validators=[DataRequired()])
    content = TextAreaField('Your Comment', validators=[DataRequired()])
    submit = SubmitField('Comment')