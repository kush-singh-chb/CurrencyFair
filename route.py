import json
from uuid import uuid4

from dateutil import parser
from flask import request, make_response, render_template, jsonify
from sqlalchemy import and_

from app import app, db
from models.TradeData import TradeData, set_default


@app.before_first_request
def before_first_request():
    db.create_all()


@app.route('/save_trade', methods=['POST'])
def save_trade():
    if request.method == 'POST':
        r_data = request.json
        check_string = ['userId', 'currencyFrom', 'currencyTo', 'amountBuy', 'amountSell', 'rate', 'timePlaced',
                        'originatingCountry']
        for value in check_string:
            if value not in r_data:
                return make_response("Invalid Data, {} is missing in data".format(value), 422)
        data = TradeData()
        data.id = str(uuid4())
        data.user_id = r_data['userId']
        data.from_currency = r_data['currencyFrom']
        data.to_currency = r_data['currencyTo']
        data.buy_amount = r_data['amountBuy']
        data.sell_amount = r_data['amountSell']
        data.rate = r_data['rate']
        data.time_placed = parser.parse(r_data['timePlaced'])
        data.org_country = r_data['originatingCountry']
        try:
            db.session.add(data)
            db.session.commit()
            return make_response("Saved Data", 200)
        except Exception as e:
            return make_response("Invalid Data \n Error: {}".format(e), 422)
    else:
        return make_response("This url is not allowed", 404)


@app.route('/', methods=['GET'])
def show_graph_page():
    if request.method == "GET":
        return render_template('GraphPage.html')
    else:
        return make_response("This url is not allowed", 404)


@app.route("/graph", methods=['GET'])
def show_graph():
    # only process get method
    if request.method == "GET":
        # data validation
        for value in ["to", "from"]:
            if request.args.get(value) is None or request.args.get(value) is "":
                return make_response("Invalid Data, {} currency is missing".format(value), 422)
        res = TradeData.query.filter(and_(
            TradeData.to_currency.like(request.args.get('to')),
            TradeData.from_currency.like(request.args.get('from'))
        )).all()
        # response/query validation
        if len(res) > 0:
            records = [data.serialize() for data in res]
            return jsonify(records), 200, {'Content-Type': 'application/json; charset=utf-8'}
        else:
            return make_response("No Data Found", 404)
    else:
        return make_response("This url is not allowed", 404)


@app.route("/getCurrency", methods=['GET'])
def get_currency():
    # get currency abbreviation
    if request.method == "GET":
        currency = set()
        try:
            for value in db.session.query(TradeData.to_currency).distinct():
                currency.add(value[0])
            for value in db.session.query(TradeData.from_currency).distinct():
                currency.add(value[0])
            return json.dumps(currency, default=set_default), 200, {'Content-Type': 'application/json; charset=utf-8'}
        except Exception as e:
            return make_response("Error occurred \n Error: {}".format(e), 422)
    else:
        return make_response("This url is not allowed", 404)
