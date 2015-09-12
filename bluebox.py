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
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
# os.environ['DATABASE_URL']
# 'sqlite:///local.db'
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    category = db.Column(db.String(20))
    description = db.Column(db.String(1000))
    price = db.Column(db.String(5))
    image = db.Column(db.String(60))

class IngAdmin(sqla.ModelView):
    column_display_pk = True
admin = Admin(app)
admin.add_view(IngAdmin(Item, db.session))

@app.route('/', methods=['GET', 'POST'])
def index_route():
    pants = Item.query.filter_by(category="pants").all()
    return flask.render_template('index.html',items=pants)


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
            "name":item.name,
            "size":size,
            "quantity":'1',
            "price":item.price,
            "image":item.image
            }]
        print session['cart_items']
    else:
        session['cart_items'].append({
            "name":item.name,
            "size":size,
            "quantity":'1',
            "price":item.price,
            "image":item.image
            })
        print session['cart_items']
    return '',201


@app.route('/cart/open', methods=['GET', 'POST'])
def open_cart():
    session['total'] = 0
    if not session:
        return flask.render_template('cart.html')

    for i in session['cart_items']:
        session['total'] += int(i['price'])
    return flask.render_template('cart.html',cart=session['cart_items'],total=session['total'])


@app.route('/favicon.ico', methods=['GET', 'POST'])
def favicon():
    return '',200


@app.route('/db/rebuild', methods=['GET', 'POST'])
def rebuild_database():
    db.drop_all()
    db.create_all()

    item = Item(
        name="Eric Coston SW",
        category="pants",
        description="ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod\
        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,\
        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo\
        consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse\
        cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non\
        proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        price="260",
        image="../static/images/pants.jpg"
        )
    db.session.add(item)
    db.session.commit()

    item = Item(
        name="Eric Coston SW",
        category="pants",
        description="This is the item's description.",
        price="260",
        image="../static/images/pants1.jpg"
        )
    db.session.add(item)
    db.session.commit()

    item = Item(
        name="Eric Coston SW",
        category="pants",
        description="This is the item's description.",
        price="260",
        image="../static/images/pants2.jpg"
        )
    db.session.add(item)
    db.session.commit()

    item = Item(
        name="Eric Coston SW",
        category="pants",
        description="This is the item's description.",
        price="260",
        image="../static/images/pants3.jpg"
        )
    db.session.add(item)
    db.session.commit()

    item = Item(
        name="Eric Coston SW",
        category="pants",
        description="This is the item's description.",
        price="260",
        image="../static/images/pants4.jpg"
        )
    db.session.add(item)
    db.session.commit()

    item = Item(
        name="Eric Coston SW",
        category="pants",
        description="This is the item's description.",
        price="260",
        image="../static/images/pants5.jpg"
        )
    db.session.add(item)
    db.session.commit()

    item = Item(
        name="Eric Coston SW",
        category="pants",
        description="This is the item's description.",
        price="260",
        image="../static/images/pants.jpg"
        )
    db.session.add(item)
    db.session.commit()

    item = Item(
        name="Eric Coston SW",
        category="shirts",
        description="This is the item's description.",
        price="260",
        image="../static/images/pants1.jpg"
        )
    db.session.add(item)
    db.session.commit()

    item = Item(
        name="Eric Coston SW",
        category="shirts",
        description="This is the item's description.",
        price="260",
        image="../static/images/pants2.jpg"
        )
    db.session.add(item)
    db.session.commit()

    item = Item(
        name="Eric Coston SW",
        category="shirts",
        description="This is the item's description.",
        price="260",
        image="../static/images/pants3.jpg"
        )
    db.session.add(item)
    db.session.commit()

    item = Item(
        name="Eric Coston SW",
        category="shirts",
        description="This is the item's description.",
        price="260",
        image="../static/images/pants4.jpg"
        )
    db.session.add(item)
    db.session.commit()

    item = Item(
        name="Eric Coston SW",
        category="shoes",
        description="This is the item's description.",
        price="260",
        image="../static/images/pants5.jpg"
        )
    db.session.add(item)
    db.session.commit()

    item = Item(
        name="Eric Coston SW",
        category="shoes",
        description="This is the item's description.",
        price="260",
        image="../static/images/pants.jpg"
        )
    db.session.add(item)
    db.session.commit()

    item = Item(
        name="Eric Coston SW",
        category="shoes",
        description="This is the item's description.",
        price="260",
        image="../static/images/pants1.jpg"
        )
    db.session.add(item)
    db.session.commit()

    item = Item(
        name="Eric Coston SW",
        category="shoes",
        description="This is the item's description.",
        price="260",
        image="../static/images/pants2.jpg"
        )
    db.session.add(item)
    db.session.commit()

    item = Item(
        name="Eric Coston SW",
        category="pants",
        description="This is the item's description.",
        price="260",
        image="../static/images/pants3.jpg"
        )
    db.session.add(item)
    db.session.commit()

    item = Item(
        name="Eric Coston SW",
        category="pants",
        description="This is the item's description.",
        price="260",
        image="../static/images/pants4.jpg"
        )
    db.session.add(item)
    db.session.commit()

    item = Item(
        name="Eric Coston SW",
        category="pants",
        description="This is the item's description.",
        price="260",
        image="../static/images/pants5.jpg"
        )
    db.session.add(item)
    db.session.commit()

    return 'ok'


if __name__ == '__main__':
    app.debug = True
    app.run(port=int(os.environ['PORT']), host='0.0.0.0')