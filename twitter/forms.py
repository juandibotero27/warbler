from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class MessageForm(FlaskForm):
    """Form for adding/editing messages."""

    text = TextAreaField('text', validators=[DataRequired()])


class UserAddForm(FlaskForm):
    """Form for adding users."""

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[Length(min=6)])
    image_url = StringField('(Optional) Image URL')


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])


class UserEditForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    image_url = StringField("(Optional) Image Url")
    header_image_url = StringField("(Optional) Image For Header")
    bio = StringField("(Optional) Tell Us About Yourself")
    password = PasswordField("Password", validators=[Length(min=6)])
