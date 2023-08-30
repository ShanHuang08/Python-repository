from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/redfish_event_listener', methods=['POST'])
def redfish_event_listener():
    data = request.json  # 取得 POST 資料
    print("Received Redfish Alert:")
    print(data)
    
    # 在這裡可以添加你希望執行的任何處理邏輯，例如發送通知、寫入日誌等
    
    return jsonify({'message': 'Redfish Alert received successfully'})

if __name__ == '__main__':
    app.run(host='10.181.92.129', port=443)