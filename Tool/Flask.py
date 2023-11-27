from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def redfish_event_listener():
    data = request.json  # 取得 POST 資料
    print("Received Redfish Alert:")
    print(data)
    
    # 在這裡可以添加你希望執行的任何處理邏輯，例如發送通知、寫入日誌等
    
    return jsonify({'message': 'Redfish Alert received successfully'})

@app.route('/')
def Hello():
    return 'Hello Flask!'


if __name__ == '__main__':
    app.run(host='10.181.92.129', port=443, ssl_context='adhoc')
    # app.run(host='10.181.92.129', port=80)

# app.run(ssl_context='adhoc') ( 註：adhoc，全名為 Ad Hoc Certificate，臨時憑證的意思 )
# app.run(ssl_context=('SSLcert.cert','SSLkey.key'))
# https://medium.com/@charming_rust_oyster_221/flask-%E9%85%8D%E7%BD%AE-https-%E7%B6%B2%E7%AB%99-ssl-%E5%AE%89%E5%85%A8%E8%AA%8D%E8%AD%89-36dfeb609fa8