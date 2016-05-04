import flask, flask.views
from flask import url_for, request, session, redirect, jsonify, Response, make_response, current_app
from jinja2 import environment, FileSystemLoader
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.ext.orderinglist import ordering_list
from flask.ext import admin
from flask.ext.admin.contrib import sqla
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin import Admin, BaseView, expose
from dateutil.parser import parse as parse_date
from flask import render_template, request
from functools import update_wrapper
from flask import session, redirect
from datetime import timedelta
from datetime import datetime
from functools import wraps
import threading
from threading import Timer
from multiprocessing.pool import ThreadPool
from time import sleep
import requests
import datetime
import time
import json
import uuid
import os

app = flask.Flask(__name__)
db = SQLAlchemy(app)
app.secret_key = '234234rfascasascqweqscasefsdvqwefe2323234dvsv'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///local.db'
# os.environ['DATABASE_URL']
# 'sqlite:///local.db'
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    category = db.Column(db.String(20))
    description = db.Column(db.String(1000))
    price = db.Column(db.Integer())
    image = db.Column(db.String(60))

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))
    email = db.Column(db.String(60))
    password = db.Column(db.String(60))
    msisdn = db.Column(db.String(11))
    address = db.Column(db.Text)
    province = db.Column(db.String(30))
    city = db.Column(db.String(30))
    barangay = db.Column(db.String(30))

class IngAdmin(sqla.ModelView):
    column_display_pk = True
    
admin = Admin(app)
admin.add_view(IngAdmin(Item, db.session))
admin.add_view(IngAdmin(User, db.session))


def search_list(values, searchFor):
    for k in values:
        if k['id'] == searchFor:
            return k
    return None


@app.route('/', methods=['GET', 'POST'])
def index_route():
    shirts = Item.query.filter_by(category="pants").all()
    flavors = Item.query.filter_by(category="flavors").all()
    mods = Item.query.filter_by(category="mods").all()
    accessories = Item.query.filter_by(category="accessories").all()
    return flask.render_template('index.html',
        shirts=shirts,
        flavors=flavors,
        mods=mods,
        accessories=accessories
        )


@app.route('/login', methods=['GET', 'POST'])
def login():
    if session:
        return redirect('/')
    credentials = flask.request.form.to_dict()
    user = User.query.filter_by(email=credentials['email'], password=credentials['password']).first()
    if not user or user == None:
        return jsonify(status='failed', error='Invalid Account'), 401
    session['logged_in'] = True
    session['user_id'] = user.id
    session['display_name'] = user.first_name
    return jsonify(status='success'), 200


@app.route('/item/info/get', methods=['GET', 'POST'])
def get_item_info():
    item_id = flask.request.form.get('item_id')
    item = Item.query.filter_by(id=item_id).first()
    return flask.render_template('item_info.html', item=item)


@app.route('/clear', methods=['GET', 'POST'])
def clear_cart():
    session.clear()
    return 'ok'


@app.route('/cart/item/add', methods=['GET', 'POST'])
def add_item_to_cart():
    item_id = flask.request.form.get('item_id')
    size = flask.request.form.get('size')
    item = Item.query.filter_by(id=item_id).first()
    if not session:
        session['cart_items'] = [{
            "id":item.id,
            "name":item.name,
            "size":size,
            "quantity":'1',
            "price":item.price,
            "image":item.image
            }]
    else:
        session['cart_items'].append({
            "id":item.id,
            "name":item.name,
            "size":size,
            "quantity":'1',
            "price":item.price,
            "image":item.image
            })
        print session['cart_items']
    return '',201


@app.route('/cart', methods=['GET', 'POST'])
def open_cart():
    if not session:
        return flask.render_template('cart.html')
    session['total'] = 0
    for i in session['cart_items']:
        session['total'] += (int(i['price']) * int(i['quantity']))
    return flask.render_template('cart.html',cart=session['cart_items'], total=session['total'])


@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if not session:
        return flask.render_template('checkout.html')
    session['total'] = 0
    for i in session['cart_items']:
        session['total'] += (int(i['price']) * int(i['quantity']))
    return flask.render_template('checkout.html',cart_items=session['cart_items'], total=session['total'])


@app.route('/favicon.ico', methods=['GET', 'POST'])
def favicon():
    return '',200


@app.route('/quantity/control', methods=['GET', 'POST'])
def control_quantity():
    item_id = flask.request.form.get('item_id')
    quantity = int(flask.request.form.get('quantity'))
    operation = flask.request.form.get('operation')

    item = Item.query.filter_by(id=item_id[5:]).first()

    if operation == 'add':
        quantity += 1
    else:
        if quantity > 1:
            quantity -= 1

    index = search_list(session['cart_items'],int(item_id[5:]))
    index['quantity'] = quantity

    session['total'] = 0

    for i in session['cart_items']:
        session['total'] += (int(i['price']) * int(i['quantity']))
    return jsonify(quantity=quantity,item_price=quantity*item.price,total=session['total']),200


@app.route('/db/rebuild', methods=['GET', 'POST'])
def rebuild_database():
    db.drop_all()
    db.create_all()

    item = Item(
        name="Eric Coston SW",
        category="pants",
        description="The ED-55 is our most popular style, a relaxed tapered fit with a mid-rise. Due to its versatility it can be worn in many different ways and suits a wide range of body shapes.",
        price=260,
        image="../static/images/pants.jpg"
        )
    db.session.add(item)
    db.session.commit()

    item = Item(
        name="Eric Coston SW",
        category="pants",
        description="This is the item's description. It must be at least this long for it to look good.",
        price=260,
        image="../static/images/pants1.jpg"
        )
    db.session.add(item)
    db.session.commit()

    item = Item(
        name="Eric Coston SW",
        category="pants",
        description="This is the item's description. It must be at least this long for it to look good.",
        price=260,
        image="../static/images/pants2.jpg"
        )
    db.session.add(item)
    db.session.commit()

    item = Item(
        name="Eric Coston SW",
        category="pants",
        description="This is the item's description. It must be at least this long for it to look good.",
        price=260,
        image="../static/images/pants3.jpg"
        )
    db.session.add(item)
    db.session.commit()

    item = Item(
        name="Eric Coston SW",
        category="pants",
        description="This is the item's description. It must be at least this long for it to look good.",
        price=260,
        image="../static/images/pants4.jpg"
        )
    db.session.add(item)
    db.session.commit()

    item = Item(
        name="Eric Coston SW",
        category="pants",
        description="This is the item's description. It must be at least this long for it to look good.",
        price=260,
        image="../static/images/pants5.jpg"
        )
    db.session.add(item)
    db.session.commit()

    item = Item(
        name="Eric Coston SW",
        category="pants",
        description="This is the item's description. It must be at least this long for it to look good.",
        price=260,
        image="../static/images/pants.jpg"
        )
    db.session.add(item)
    db.session.commit()

    item = Item(
        name="Eric Coston SW",
        category="shirts",
        description="This is the item's description. It must be at least this long for it to look good.",
        price=260,
        image="../static/images/pants1.jpg"
        )
    db.session.add(item)
    db.session.commit()

    item = Item(
        name="Eric Coston SW",
        category="shirts",
        description="This is the item's description. It must be at least this long for it to look good.",
        price=260,
        image="../static/images/pants2.jpg"
        )
    db.session.add(item)
    db.session.commit()

    item = Item(
        name="Eric Coston SW",
        category="shirts",
        description="This is the item's description. It must be at least this long for it to look good.",
        price=260,
        image="../static/images/pants3.jpg"
        )
    db.session.add(item)
    db.session.commit()

    item = Item(
        name="Eric Coston SW",
        category="shirts",
        description="This is the item's description. It must be at least this long for it to look good.",
        price=260,
        image="../static/images/pants4.jpg"
        )
    db.session.add(item)
    db.session.commit()

    item = Item(
        name="Eric Coston SW",
        category="shoes",
        description="This is the item's description. It must be at least this long for it to look good.",
        price=260,
        image="../static/images/pants5.jpg"
        )
    db.session.add(item)
    db.session.commit()

    item = Item(
        name="Eric Coston SW",
        category="shoes",
        description="This is the item's description. It must be at least this long for it to look good.",
        price=260,
        image="../static/images/pants.jpg"
        )
    db.session.add(item)
    db.session.commit()

    item = Item(
        name="Eric Coston SW",
        category="shoes",
        description="This is the item's description. It must be at least this long for it to look good.",
        price=260,
        image="../static/images/pants1.jpg"
        )
    db.session.add(item)
    db.session.commit()

    item = Item(
        name="Eric Coston SW",
        category="shoes",
        description="This is the item's description. It must be at least this long for it to look good.",
        price=260,
        image="../static/images/pants2.jpg"
        )
    db.session.add(item)
    db.session.commit()

    item = Item(
        name="Eric Coston SW",
        category="pants",
        description="This is the item's description. It must be at least this long for it to look good.",
        price=260,
        image="../static/images/pants3.jpg"
        )
    db.session.add(item)
    db.session.commit()

    item = Item(
        name="Eric Coston SW",
        category="pants",
        description="This is the item's description. It must be at least this long for it to look good.",
        price=260,
        image="../static/images/pants4.jpg"
        )
    db.session.add(item)
    db.session.commit()

    item = Item(
        name="Eric Coston SW",
        category="pants",
        description="This is the item's description. It must be at least this long for it to look good.",
        price=260,
        image="../static/images/pants5.jpg"
        )
    db.session.add(item)
    db.session.commit()

    user = User(
        first_name='Jasper',
        last_name='Barcelona',
        email='barcelona.jasperoliver@gmail.com',
        password='ratmaxi8',
        msisdn='09159484200'
        )
    db.session.add(user)
    db.session.commit()

    return 'ok'


if __name__ == '__main__':
    app.debug = True
    app.run()