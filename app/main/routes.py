from flask import render_template, flash, request
from app.main import bp
from app.main.forms import UserInput, CountryPopulation, CountryToCompare
from app.main.utils import getPercentage, get_allcountries, get_country_population, get_world_population, get_jokes

@bp.route('/')
@bp.route('/index')
def index():
    joke = get_jokes()
    return render_template('main/index.html', title='Home', joke=joke)

@bp.route('/crush', methods=['GET', 'POST'])
def crush():
    form = UserInput()
    result = []
    if form.validate_on_submit():
        info = {}
        info["fname"] = form.first_name.data
        info["sname"] = form.second_name.data

        result = getPercentage(info)
    return render_template('main/crush.html', title='Crush', form=form, result=result)


@bp.route('/population', methods=['GET', 'POST'])
def population():
    world_population = get_world_population()
    form = CountryPopulation()
    country_pop = []
    if form.validate_on_submit():
        country = {}
        country["country_name"] = form.country.data.title()

        country_pop = get_country_population(country)

    return render_template('main/population.html', title='Population', form=form, country_pop=country_pop, world_population=world_population)


@bp.route('/compare', methods=['GET', 'POST'])
def compare():
    form = CountryToCompare()
    country_one_pop = []
    country_two_pop = []
    if form.validate_on_submit():
        country = {}
        country["country_name"] = form.country_one.data.title()
        country_one_pop = get_country_population(country)

        country["country_name"] = form.country_two.data.title()
        country_two_pop = get_country_population(country)
    return render_template('main/compare.html', title='Population', form=form, country_one_pop=country_one_pop, country_two_pop=country_two_pop)
