from import_files import *
# GET method to retrieve all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data)

# POST method to create a new item
@app.route('/items', methods=['POST'])
def create_item():
    new_item = request.json
    new_item["id"] = len(data) + 1
    data.append(new_item)
    return jsonify({"message": "Item created successfully", "item": new_item}), 201

# DELETE method to delete an item by ID
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    for item in data:
        if item['id'] == item_id:
            data.remove(item)
            return jsonify({"message": f"Item {item_id} deleted successfully"})
    return jsonify({"error": f"Item {item_id} not found"}), 404

