from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "Message": "app up and running successfully"
    })

@app.route("/access")
def access():
    data = request.get_json()
    name = data.get("name", "dipto")
    server = data.get("server","server1")

    message = f"User {name} received access to server {server}"

    return jsonify({
        "Message": message
    })


if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)