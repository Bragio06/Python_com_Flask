import  requests
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/')
def home():
  return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():

  login = request.json

  login_arquivo = open('login.txt', 'a')
  login_arquivo.write(f'{str(login)}' + '\n')
  
  return jsonify(login)

@app.route('/cadastro', methods=['POST'])
def cadastro():

  cadastro = request.json

  cadastro_arquivo = open('cadastro.txt', 'a')
  cadastro_arquivo.write(f'{str(cadastro)}' + '\n')

  return jsonify(cadastro)


if __name__ == '__main__':
  app.run(host='0.0.0.0')
