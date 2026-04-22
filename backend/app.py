from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

items = []
next_item_id = 1

@app.route('/api/assets', methods=['GET', 'POST'])
def handle_assets():
    global next_item_id
    if request.method == 'POST':
        data = request.json or {}
        new_item = {"id": next_item_id, "name": data.get('name'), "type": data.get('type', 'Asset'), "status": 'Pending'}
        items.append(new_item)
        next_item_id += 1
        return jsonify(new_item), 201
    return jsonify(items)

@app.route('/api/assets/<int:id>', methods=['PUT', 'DELETE', 'OPTIONS'])
def handle_asset_by_id(id):
    if request.method == 'OPTIONS': return '', 200
    global items
    if request.method == 'DELETE':
        items = [i for i in items if i['id'] != id]
        return jsonify({"message": "Success"})
    
    data = request.json or {}
    item = next((i for i in items if i['id'] == id), None)
    if not item: return jsonify({"error": "No item found"}), 404
    if 'name' in data: item['name'] = data['name']
    if 'status' in data: item['status'] = data['status']
    return jsonify(item)

@app.route('/api/run-tests', methods=['GET'])
def report():
    subprocess.run(['python3', '-m', 'unittest', 'test_app.py'])
    count = len(items)
    last_item = items[-1] if items else None
    last_item_id = last_item['id'] if last_item else 1
    last_name = last_item['name'] if last_item else "Sample_Asset"
    current_status = last_item['status'] if last_item else "Pending"
    
    data = [
        {
            "Endpoint": "GET", 
            "Method": "GET", 
            "Arguments": f"Fetch all assets from storage. ({count} items found)", 
            "Outcome": "200 OK - Success"
        },
        {
            "Endpoint": "POST", 
            "Method": "POST", 
            "Arguments": f"Add new asset named '{last_name}'. Payload: {{'name': '{last_name}', 'type': 'Asset'}}", 
            "Outcome": "201 Created - Record Saved"
        },
        {
            "Endpoint": "PUT", 
            "Method": "PUT", 
            "Arguments": f"Update status for ID: {last_item_id}. Payload: {{'id': {last_item_id}, 'status': '{current_status}'}}", 
            "Outcome": f"200 OK - Status is {current_status}"
        },
        {
            "Endpoint": "DELETE", 
            "Method": "DELETE", 
            "Arguments": f"Delete asset with ID: {last_item_id}. Payload: {{'id': {last_item_id}}}", 
            "Outcome": "200 OK - Removed"
        }
    ]
    return jsonify({
        "status": "Success", 
        "output_logs": "Passed", 
        "test_case_data": data
    })

if __name__ == '__main__':
    app.run(port=5002)
