from flask import Flask, jsonify
from repository.database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'SECKET_KEY_WEBSOCKET'
db.init_app(app)


@app.route("/payments/pix", methods=["POST"])
def create_payments_pix():
    return jsonify({"message": "O pagamento foi criado"})

@app.route("/payments/pix/confirmation", methods=["POST"])
def pix_confirmation():
    return jsonify({"message": "O pagamento foi confirmado"})

@app.route("/payments/pix/<int:payment_id>", methods=["GET"])
def payment_pix_page(payment_id):
    return 'Pagamento pix'


if __name__ == "__main__":
    app.run(debug=True)

