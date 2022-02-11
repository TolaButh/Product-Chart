from unicodedata import category
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField,SubmitField
from wtforms.validators import DataRequired,Length

class ProductManagement(FlaskForm):
    product_id = StringField("Product ID", validators=[DataRequired(),Length(min=5,max=8)])
    product_name = StringField("Product Name", validators=[DataRequired()])
    product_type = SelectField("Product Type", validators=[DataRequired()],
                               choices=[('income', 'Income'),
                                        ('expense', 'Expense')])
    category = SelectField("Category", validators=[DataRequired()],
                           choices=[('computer', 'Computer'),
                                    ('ipad', 'Ipad'),
                                    ('phone', 'Phone'),
                                    ('AirPods', 'AriPods'),
                                    ('radio', 'Radio')])
    price = IntegerField("Price of product", validators=[DataRequired()])
    submit = SubmitField("Add Product")
    
    