from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Length



class SignupForm(FlaskForm):
    
    username = StringField('Nombre de Usuario', validators=[DataRequired(), Length(min=3, max=50, message="Campo Nombre es incorrecto")])
    
    fullname = StringField('Nombre Completo', validators=[DataRequired(), Length(min=10, max=80, message="Campo Apellidos es incorrecto")])
    
    biography = StringField('Biografía', validators=[DataRequired(), Length(min=3, max=120, message="Campo Biografía incorrecto")])
    
    email = StringField('Correo', validators=[DataRequired(), Length(min=3, max=25, message="Campo Correo es incorrecto")])
    
    phone = StringField('Número Telefonico', validators=[DataRequired(), Length(min=10, max=12, message="Campo Número Telefonico incorrecto")])
    
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(min=8, max=30, message="Campo Contraseña incorrecto")])

class LoginForm(FlaskForm):
    
    username = StringField('Nombre de Usuario', validators=[DataRequired(), Length(min=3, max=50, message="Campo Nombre es incorrecto")])
    
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(min=8, max=30, message="Campo Contraseña incorrecto")])


class HomeForm(FlaskForm):

    comment = TextAreaField('Comentario', validators=[DataRequired(), Length(min=3, max=250, message="Campo Publicación es incorrecto")])