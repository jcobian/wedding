from wedding import app
from flask import jsonify

# TODO: dummy data for now
invitees = [
    {
        'id': 1,
        'firstName': 'foo',
        'lastName': 'bar'
    },
    {
        'id': 2,
        'firstName': 'foo2',
        'lastName': 'bar2'
    }
]


@app.route('/api/invitees')
def list():
    return jsonify(invitees)


@app.route('/api/invitees/<_id>')
def get(_id):
    return jsonify(invitees[int(_id)])
