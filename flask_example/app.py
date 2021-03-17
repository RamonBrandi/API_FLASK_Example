from flask import Flask, request, jsonify

json_post = {}
dados = [{"canal": "Feichas", "msg": "Desespero!"}]

app = Flask("app")

@app.route("/")
def Feichas():
    return jsonify({"canal" : dados})

@app.route("/", methods=['POST'])
def add_post():
    dado = {'canal': request.json['canal'],
            'msg': request.json['msg']}

    dados.append(dado)
    
    return jsonify({"canal" : dados})