from flask import Flask, render_template
from flask.views import MethodView, request
from wtforms import Form, StringField, SubmitField

from calorie import Calorie
from temperature import Temperature

app = Flask(__name__)

class HomePage(MethodView):
    def get(self):
        return render_template('index.html') # Path to this file is not needed, Flask expects the "templates" folder

class CaloriesFormPage(MethodView):
    def get(self):
        calories_form = CaloriesForm()
        return render_template('calories_form_page.html',
                               calories_form=calories_form)

class ResultsPage(MethodView):
    def post(self):
        calories_form = CaloriesForm(request.form)
        age = calories_form.age.data
        weight = calories_form.weight.data
        height = calories_form.height.data
        country = calories_form.country.data
        city = calories_form.city.data
        temperature = Temperature(country=country, city=city).get()
        print(temperature)
        calorie = Calorie(weight=float(weight),
                          height=float(height),
                          age=float(age), temperature=temperature)

        return str(calorie.calculate())

class CaloriesForm(Form):
    age = StringField("Age: ")
    weight = StringField("Weight: ")
    height = StringField("Height: ")
    country = StringField("Country: ")
    city = StringField("City: ")

    button = SubmitField("Calculate")


app.add_url_rule('/',
                 view_func=HomePage.as_view('home_page'))
app.add_url_rule('/calories',
                 view_func=CaloriesFormPage.as_view('calories_form_page'))
app.add_url_rule('/results',
                 view_func=ResultsPage.as_view('results_page'))

app.run(debug=True)