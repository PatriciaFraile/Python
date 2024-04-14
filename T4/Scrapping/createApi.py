from flask import Flask, jsonify , request

app = Flask(__name__)

people = [
]
@app.route('/people/add', methods=['POST'])
def add_people():
    new_people = request.json
    people.append(new_people)
    return jsonify({"message": "Added person"}), 201
@app.route('/people', methods=['GET'])
def list_people():
    return jsonify(people)
@app.route('/people/<int:people_id>', methods=['GET'])
def get_people(people_id):
    peoples = next((p for p in people if p['id'] == people_id), None)
    if peoples:
        return jsonify(peoples), 200
    else:
        return jsonify({'message': 'Person not found'}), 404
@app.route('/people/update/<int:id>', methods=['PUT'])
def update_people(id):
    data_update = request.json
    for data in people:
        if data['id'] == id:
            data.update(data_update)
            return jsonify({"message": "People update"})
    return jsonify({"message": "Data not found"}), 404
@app.route('/people/delete/<int:id>', methods=['DELETE'])
def delete_people(id):
  global people
  people = [p for p in people if p['id'] != id]
  return jsonify({'message': 'People delete'}), 200


if __name__ == '__main__':
    app.run(debug=True)