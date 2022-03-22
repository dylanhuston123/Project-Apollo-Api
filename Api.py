import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
   [
{
"status": 200,
"data": [
{
"name": "Cube",
"_Wrning!": "This api is in development and is used for testing. Made by worstgamer13",
"Size": "3",
"Location": "102",
"Rotation": "73",
"length": 654,
"url": "test"
},
{}
]
}
]
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


# A route to return all of the available entries in our catalog.
@app.route('/api/test', methods=['GET'])
def api_all():
    return jsonify(books)

app.run()