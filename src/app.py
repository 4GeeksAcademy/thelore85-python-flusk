from flask import Flask, jsonify, request
app = Flask(__name__)


todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False },
    { "label": "Another task", "done": False },
    { "label": "Many task", "done": False },
    { "label": "Last task", "done": False }
]


@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)


@app.route('/todos', methods=['POST'])
def add_new_todo():
    print('json', request)
    request_json = request.json
    todos.insert(0, request_json)
    
    return jsonify(todos)


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print('element do delete', todos[position])
    print('position to  delete', position)

    todos.pop(position)

    return todos


# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)