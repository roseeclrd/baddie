from wtforms import Form, StringField, SelectField
from wtforms.validators import DataRequired

class UserForm(Form):
    street = StringField('Street', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])

    country = SelectField(
        'Country',
        choices=[
            ('USA', 'USA'),
            ('UK', 'UK'),
            ('Canada', 'Canada'),
            ('Kazakhstan', 'Kazakhstan'),
            ('Germany', 'Germany'),
            ('France', 'France'),
            ('Other', 'Other')
        ],
        validators=[DataRequired()]
    )

    rating = StringField('Rating', validators=[DataRequired()])
    review = StringField('Review', validators=[DataRequired()])


class ExperienceForm(Form):
    textExp = StringField('Experience', validators=[DataRequired()])
    category = SelectField(
        'Category',
        choices=[
            ('Domestic Violence', 'Domestic Violence'),
            ('Abuse on the road', 'Abuse on the road'),
            ('Abuse at workplace', 'Abuse at workplace'),
            ('Abuse during travelling', 'Abuse during travelling'),
            ('Abuse from a close relative', 'Abuse from a close relative'),
            ('Others', 'Others')
        ],
        validators=[DataRequired()]
    )

