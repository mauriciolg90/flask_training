# For routing and queries on the model
from src.models.indicators import Indicators, session
from flask import Flask, jsonify, request

app = Flask(__name__)

"""
    Returns a list of countries filtering by:
        INDICATOR: SW_LIFS (Life satisfaction)
        INEQUALITY: TOT (Total)
        VALUE: greater than the input index
    Parameters:
        index: min threshold for filtering
"""
@app.route('/countries/sw_lifs_gt/<float:index>', methods=['GET'])
def countries_sw_lifs_gt(index):
    if index > 0:
        # Query on the database according to the filters
        countries = session.query(Indicators.location, Indicators.country).filter(
            Indicators.indicator_code == 'SW_LIFS',
            Indicators.inequality_code == 'TOT',
            Indicators.value > index
        ).all()
        # Return the results
        return jsonify(countries)
    else:
        return 'The index format is invalid!'

@app.errorhandler(404)
def not_found(error):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    response = jsonify(message)
    response.status_code = 404
    return response