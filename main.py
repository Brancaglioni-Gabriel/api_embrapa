from flask import Flask, make_response, jsonify
import teste

app = Flask(__name__)


@app.route('/inicio', methods=['GET'])
def teste():
    return make_response(
        jsonify(
            teste.info
        )
    ) 

app.run()