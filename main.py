from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from datetime import datetime
import json

app = Flask(__name__)
CORS(app) 

# Dados dos petshops
petshops = [{
    'nome': 'Meu Canino Feliz',
    'distancia': 2.0,
    'preco_semana_pequeno': 20.0,
    'preco_semana_grande': 40.0,
    'aumento_fim_semana': 0.2 
}, {
    'nome': 'Vai Rex',
    'distancia': 1.7,
    'preco_semana_pequeno': 15.0,
    'preco_semana_grande': 50.0,
    'preco_fim_semana_pequeno': 20.0, 
    'preco_fim_semana_grande': 55.0
}, {
    'nome': 'ChowChawgas',
    'distancia': 0.8,
    'preco_semana_pequeno': 30.0,
    'preco_semana_grande': 45.0
}]

@app.route('/')
def main():
 return render_template('index.html')

@app.route('/api/CalcularMelhorPetshop', methods=['POST'])
def calcular_melhor_petshop():
  # Receber os dados da requisição
  print('requisitado')
  requested = request.get_data() 
  requested_normalize = str(requested)
  requested_dic = requested_normalize[2:-1]
  requested_json = json.loads(requested_dic) 

  data = requested_json['Data']
  caes_pequenos = requested_json['CaesPequenos']
  caes_grandes = requested_json['CaesGrandes']

  print('data: ' + data)
  # Calcular o dia da semana (0 a 6, onde 0 é segunda-feira e 6 é domingo)
  dia_semana = datetime.strptime(data, '%Y-%m-%d').weekday() 

  # Calcular o preço total em cada petshop e encontrar o melhor
  melhor_petshop = None
  melhor_preco = float('inf')  

  for petshop in petshops:
    preco = calcular_preco(petshop, dia_semana, caes_pequenos, caes_grandes)
    if preco < melhor_preco or (preco == melhor_preco and petshop['distancia']
                                < melhor_petshop['distancia']):
      melhor_petshop = petshop
      melhor_preco = preco
 
  resultado = {
      'NomePetshop': melhor_petshop['nome'],
      'PrecoTotal': melhor_preco,
      'Distancia': melhor_petshop['distancia']
  }

  return resultado

def calcular_preco(petshop, dia_semana, caes_pequenos, caes_grandes):
  # Calcular o preço total  
  if dia_semana < 5:
    preco_total = (int(caes_pequenos) * petshop['preco_semana_pequeno']) + (
        int(caes_grandes) * petshop['preco_semana_grande'])
  else: 
    preco_total = (int(caes_pequenos) * petshop.get('preco_fim_semana_pequeno', petshop['preco_semana_pequeno'])) + \
                  (int(caes_grandes) * petshop.get('preco_fim_semana_grande', petshop['preco_semana_grande']))

  return preco_total


if __name__ == '__main__':
  app.run(debug=True)