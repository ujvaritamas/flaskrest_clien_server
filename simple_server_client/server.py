from flask import Flask, jsonify, request


app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/login',methods = ['POST'])  
def login():  
    uname=request.form['uname']
    passwrd=request.form['pass']
    print("User: {}, passwrd: {}".format(uname, passwrd))
    return "Welcome %s" %uname  

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)