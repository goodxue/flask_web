from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,SelectField
from wtforms.validators import DataRequired,Length

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(1,20)])
    password = PasswordField('Password',validators=[DataRequired(),Length(8,128)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log in')

class PostForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired(),Length(1,60)])
    category = SelectField('Category',coerce=int,default=1)     #表示html里<select>标签，下拉列表的选项由
    body = CKEditorField('Body',validators=[DataRequired()])    #choice参数决定
    submit = SubmitField()

    def __init__(self,*args,**kwargs):
        super(PostForm,self).__init__(*args,**kwargs)
        self.category.choices = [(category.id,category.name)
            for category in Category.query.order_by(Category.name).all()]