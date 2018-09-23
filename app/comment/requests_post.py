# requests_post.py

# Обробатывает POST-запросы 

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from flask import request, jsonify, url_for, flash, escape

from . import comment
from ..models.region import Region
from ..models.city import City
from ..models.user import User
from ..models.comment import Comment
from .. import db

from .forms import AddComment_form

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

@comment.route('/comment/..add', methods=['POST'])
def addComment_req():
    form = AddComment_form()
    csrf_token_val = escape(form.csrf_token.data)
    first_name_val = escape(form.first_name.data)
    last_name_val = escape(form.last_name.data)
    middle_name_val = escape(form.middle_name.data)
    email_val = escape(form.email.data)
    phone_val = escape(form.phone.data)
    region_val = escape(form.region.data)
    city_val = escape(form.city.data)
    comment_val = escape(form.comment.data)

    region = Region.query.get_or_404(region_val)
    city = City.query.get_or_404(city_val)

    user = User.query.filter_by(email=email_val).first()
    if not user:
        user = User(
            first_name = first_name_val, 
            last_name = last_name_val, 
            middle_name = middle_name_val,
            email = email_val,
            phone = phone_val,
            region = region,
            city = city)

    comment = Comment(body=comment_val, author=user)

    db.session.add_all([user, comment])
    db.session.commit()

    flash(category='success', message='Комментарий успешно сохранён.')
    return jsonify({'next_url': url_for(endpoint='comment.addComment_page')})



@comment.route(rule='/comment/<int:id>...del', methods=['POST'])
def delComment_req(id):
    comment = Comment.query.get_or_404(id)
    db.session.delete(comment)
    db.session.commit()

    return jsonify({'success': True})