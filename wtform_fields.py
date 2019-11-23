from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import InputRequired,Length,EqualTo


class RegistartionForm(FlaskForm):
    '''
    Registration form
    '''
    username = StringField('username_label',validators=[InputRequired(message="Username required"),Length(min=4,max=25, message="username must be between 4 and 25 characters")])
    password = PasswordField('password_label',validators=[InputRequired(message="password required"),Length(min=4, max=10 ,message="password must be between 4 and 25 characters")])
    confirm_pswd =PasswordField('confirm_pswd_label',validators=[InputRequired(message="password required"),EqualTo('password',message="passwords must match")])
    submit_button = SubmitField('create')

