from cars import *

# test route
@app.route('/', methods=['GET'])
def index():
    '''Index'''
    return jsonify({ 
        'success': True,
        'message': 'our API works'
    })

# route to get all cars
@app.route('/cars', methods=['GET'])
def get_cars():
    '''Get Cars route'''
    return jsonify({
        'success': True,
        'cars': Car.get_all_cars()
    })

# route to get a car by id
@app.route('/cars/<int:id>', methods=['GET'])
def get_car_by_id(id):
    '''Get Car by id route'''
    car = Car.get_car(id)
    return jsonify({
        'success': True,
        'car': car
    })

# route to create a new car
@app.route('/cars', methods=['POST'])
def add_car():
    '''Add new Car'''
    request_data = request.get_json() # get request data from client
    Car.add_car(
        request_data["make"],
        request_data["model"],
        request_data["fuel_type"],
        request_data["gearbox"],
        request_data["year"]
    )
    response = Response({'Car created successfully'}, 201, mimetype='application/json')
    return response

# route to update a car by id
@app.route('/cars/<int:id>', methods=['PUT'])
def update_car(id):
    '''Update a Car'''
    request_data = request.get_json()
    Car.update_car(
        id,
        request_data["make"],
        request_data["model"],
        request_data["fuel_type"],
        request_data["gearbox"],
        request_data["year"]
    )
    response = Response({ 'Car updated successfully' }, status=200, mimetype='application/json')
    return response

# route to delete a car by id
@app.route('/cars/<int:id>', methods=['DELETE'])
def remove_car(id):
    '''Delete a Car'''
    Car.delete_car(id)
    response = Response({ 'Car deleted' }, status=200, mimetype='application/json')
    return response

if __name__ == "__main__":
    app.run(port=1234, debug=True)