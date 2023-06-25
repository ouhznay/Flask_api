from flask import Flask, jsonify
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

@app.route('/api/modules/', methods= ['GET'])
def get_modules():
    modules = [
        {'name': 'BT1101', 'details': "Last Week's Content Review: 2 hours, This Week's Content Review: 2 hours, Tutorial: 2 hours, Lecture: 3 hours, Lab: 2 hours"},
        {'name': "MA1521", 'details': "Last Week's Content Review: 3 hours, This Week's Content Review: 2 hours, Tutorial: 2 hours, Lecture: 4 hours"},
        {'name': 'MA2001', 'details': "Last Week's Content Review: 3 hours, This Week's Content Review: 3 hours, Tutorial: 2 hours, Lecture: 4 hours"},
        {'name': 'BT2102', 'details': "Last Week's Content Review: 2 hours, This Week's Content Review: 2 hours, Tutorial: 2 hours, Lecture: 2 hours"},
        {'name': 'BT2101', 'details': "Last Week's Content Review: 2 hours, This Week's Content Review: 2 hours, Tutorial: 2 hours, Lecture: 3 hours"},
        {'name': 'CS1010S', 'details': "Last Week's Content Review: 2 hours, This Week's Content Review: 3 hours, Tutorial: 4 hours, Lecture: 2 hours, Lab: 5 hours"},
        {'name': 'CS2030', 'details': "Last Week's Content Review: 2 hours, This Week's Content Review: 3 hours, Recitation: 2 hours, Lecture: 3 hours, Lab: 5 hours"},
        {'name': 'CS2040', 'details': "Last Week's Content Review: 2 hours, This Week's Content Review: 3 hours, Tutorial: 4 hours, Lecture: 3 hours, Lab: 6 hours"},
        {'name': 'SC1101E', 'details': "Last Week's Content Review: 1 hours, This Week's Content Review: 1 hours, Tutorial: 3 hours, Lecture: 3 hours"},
        {'name': 'IS1108', 'details': "Last Week's Content Review: 1 hours, This Week's Content Review: 1 hours, Tutorial: 3 hours"}
    ]
    return jsonify(modules)

if __name__ == '__main__':
    app.run(debug=True)

