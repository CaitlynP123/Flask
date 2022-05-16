from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [
    {
        'id': 1,
        'name': 'Book McBookerson',
        'contact': '+91 4968832124',
        'done': False
    },
    {
        'id': 2,
        'name': 'Fifi the Feather Duster',
        'contact': '1231312354',
        'done': True
    }
]

@app.route('/getdata')
def getContacts():
    return jsonify({
        'data' : contacts,
    })

@app.route('/add_data', methods=['POST'])
def addContacts():
    if not request.json:
        return jsonify({
            'status' : 'ERROR',
            'message' : 'Please Provide the Data'
        },400)
    
    task = {
        'id': contacts[-1]['id']+1,
        'name': request.json['name'],
        'contact': request.json.get('contact', ''),
        'done': False
    }

    contacts.append(task)

    return jsonify({
        'status' : 'Success',
        'message' : 'Contact added successfully'
    })


if (__name__ == "__main__"):
    app.run(debug=True)