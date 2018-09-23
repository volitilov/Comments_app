# requests_get.py

# Обрабатывает GET-запросы 

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from flask import render_template, request, jsonify, url_for

from . import comment
from ..models.region import Region
from ..models.city import City
from ..models.comment import Comment
from .. import db

from .data import page_titles
from .forms import AddComment_form
from ..utils import flash_errors

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

@comment.route('/')
def home_page():
    return render_template('index.html', data={
        'title_page': page_titles['home_page']
    })



@comment.route('/comment/')
def addComment_page():
    form = AddComment_form()
    regions = Region.query
    cities = City.query.filter_by(region=regions[0])

    form.region.choices = [(region.id, region.title) for region in regions]
    form.city.choices = [(city.id, city.title) for city in cities]

    return render_template('comment.html', data={
        'title_page': page_titles['addComment_page'],
        'form': form
    })



@comment.route('/view/')
def viewComments_page():
    return render_template('view.html', data={
        'title_page': page_titles['viewComments_page'],
        'comments': Comment.query
    })



@comment.route(rule='/comment/region/<int:id>')
def getRegionCity_req(id):
    region = Region.query.get_or_404(id)
    cities = [{
        'id': city.id,
        'title': city.title
        } for city in region.cities]
    return jsonify({'cities': cities})



@comment.route('/stat/')
def stat_page():
    regions_and_count_comments = []
    for region in Region.query.all():
        region_comments_count = [region, 0]
        for city in region.cities.all():
            for user in city.citizens.all():
                region_comments_count[1] += user.comments.count()
        regions_and_count_comments.append(region_comments_count)

    favorit_regions = [x for x in regions_and_count_comments if x[1] >= 5]
    regions = []
    for region in favorit_regions:
        regions.append({
            'region': region[0],
            'comment_count': region[1]
        })

    return render_template('stat.html', data={
        'title_page': page_titles['stat_page'],
        'regions': regions
    })


@comment.route('/stat/region/<int:id>')
def statRegion_page(id):
    region = Region.query.get_or_404(id)
    cities_and_count_comments = []

    for city in region.cities.all():
        city_comments_count = [city, 0]
        for user in city.citizens.all():
            city_comments_count[1] += user.comments.count()
        cities_and_count_comments.append(city_comments_count)

    cities = []
    for city in cities_and_count_comments:
        cities.append({
            'city': city[0],
            'comment_count': city[1]
        })

    return render_template('stat_region.html', data={
        'title_page': page_titles['stat_page'],
        'cities': cities,
        'region': region
    })
