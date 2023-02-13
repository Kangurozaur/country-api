from flask import Flask, jsonify
import pycountry_convert as pc

app = Flask(__name__)

@app.route('/country/<string:country_name>', methods=['GET'])
def get_country_continent(country_name):
    try:
        country_alpha2 = pc.country_name_to_country_alpha2(country_name)
        country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
        country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)
        return jsonify({'continent': country_continent_name})
    except KeyError:
        return jsonify({'error': 'Invalid country name'}), 404

if __name__ == '__main__':
    app.run(debug=True)