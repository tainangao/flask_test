from flask import Flask
import numpy
import json
import jsonify # the format we're sending the data in
import sys # for any kind of rewrite operation
import pandas as pd # we need dataframe to modify the data
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib
import stripe

from flask import Flask, request
from flask_firebase import FirebaseAuth
from flask_login import LoginManager, UserMixin, login_user, logout_user
from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy(app)
auth = FirebaseAuth(app)
login_manager = LoginManager(app)

app.register_blueprint(auth.blueprint, url_prefix='/auth')



app = Flask(__name__)

@app.route('signup'), methods=['GET']
def signup process():

	card_data = request.json

	charge = stripe.Charge.create(
      amount=card_data.amount, 
      currency=card_data.currency,
      customer=card_data.customer,
      description=card_data.description,
      metadata=card_data.id

   )

	new_order.charge_id = charge_id
	# sort in our database

@app.route('/')
def hello_world():
    return 'Hello, World!'

filename = 'trained_model.sav'

@app.route('/api/vo/verify', methods=['GET','POST'])
def predict_test():
	vector = pd.dataframe([request.json])

	if (database.query(vector.id)) ==True:
		loaded_model = joblib.load(filename)
		res = str(loaded_model.predict(vector)[0])
		result = [

		{
			'id':0
			'prediction':res
		}


		]

	return jsonify(result)

	else:
		return jsonify('you must pay!')




	