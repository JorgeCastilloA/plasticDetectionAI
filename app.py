from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "Plastic Detection API"


@app.route("/api/v1/detect", methods=['POST', 'GET'])
def detect_garbage():
    contains = {}
    
    if request.method == 'POST':
        contains['name'] = 'El método es POST'
    else:
        CustomVisionQuickstar('./imagen_test.png')

    return jsonify(contains)

app.run(debug=True)