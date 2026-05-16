from flask import Flask, request, render_template, redirect, url_for
from forms import UserForm
from forms import ExperienceForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) 




class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    street = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)

    rating = db.Column(db.String(125), nullable=False)
    review = db.Column(db.String(400), nullable=False)

    def __repr__(self):
        return '<User Review>'







class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    textExp = db.Column(db.String(1000), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    def __repr__(self):
        return f'<Experience {self.textExp}>'



with app.app_context():
    db.create_all()








@app.route('/')
def index():
    return render_template("index.html")

@app.route('/apps')
def apps():
    return render_template("apps.html")

@app.route('/websites')
def websites():
    return render_template("websites.html")


@app.route('/expform')
def expform():
    return render_template("expform.html")


@app.route('/hotline')
def hotline():
    return render_template("hotline.html")


@app.route('/form')
def form():
    return render_template("form.html")


@app.route('/tools')
def tools():
    return render_template("tools.html")

@app.route('/users')
def users():
    selected_country = request.args.get('country')

    if selected_country and selected_country != 'All':
        all_users = User.query.filter_by(country=selected_country).all()
    else:
        all_users = User.query.all()

    countries = [
        c[0] for c in db.session.query(User.country).distinct().all()
    ]

    return render_template(
        'users.html',
        users=all_users,
        countries=countries,
        selected_country=selected_country or 'All'
    )


@app.route('/experience')
def experience():
    selected_category = request.args.get('category')

    if selected_category and selected_category != 'All':
        all_experience = Experience.query.filter_by(category=selected_category).all()
    else:
        all_experience = Experience.query.all()

    categories = [
        'All',
        'Domestic Violence',
        'Abuse on the road',
        'Abuse at workplace',
        'Abuse during travelling',
        'Abuse from a close relative',
        'Others'
    ]

    return render_template(
        'experience.html',
        experience=all_experience,
        categories=categories,
        selected_category=selected_category or 'All'
    )




@app.route('/submit', methods=['POST'])
def submit():
    form = UserForm(request.form)
    if form.validate():
        user = User(
            street=form.street.data,
            city=form.city.data,
            state=form.state.data,
            country=form.country.data,
            rating=form.rating.data,
            review=form.review.data
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users'))
    else:
        return str(form.errors)




    
@app.route('/submitExperience', methods=['POST'])
def submitExperience():
    form = ExperienceForm(request.form)
    if form.validate():
        exp = Experience(
            textExp=form.textExp.data,
            category=form.category.data
        )

        db.session.add(exp)
        db.session.commit()
        return redirect(url_for('experience'))
    else:
        return str(form.errors)

    




if __name__ == '__main__':
    app.run(debug=True)
