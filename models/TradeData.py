from datetime import datetime

from route import db


class TradeData(db.Model):
    # trade data model
    id = db.Column(db.String, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    from_currency = db.Column(db.String(3), nullable=False)
    to_currency = db.Column(db.String(3), nullable=False)
    buy_amount = db.Column(db.Integer, nullable=False)
    sell_amount = db.Column(db.Integer, nullable=False)
    rate = db.Column(db.Integer, nullable=False)
    time_placed = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    org_country = db.Column(db.String(5), nullable=False)

    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'userId': self.user_id,
            'currencyFrom': self.from_currency,
            'currencyTo': self.to_currency,
            'amountSell': self.sell_amount,
            'amountBuy': self.buy_amount,
            'rate': self.rate,
            'timePlaced': dump_datetime(self.time_placed),
            'originatingCountry': self.org_country
        }

    def __repr__(self):
        return '<User {}>'.format(self.user_id)


def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return value.strftime("%Y-%m-%d %H:%M:%S")


def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError
