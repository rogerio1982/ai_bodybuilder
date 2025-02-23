


from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

app = Flask(__name__)

# Configuração da API do Gemini
genai.configure(api_key='sua_api_gemini')

# Inicializando o modelo
model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gerar_treino', methods=['POST'])
def gerar_treino():
    data = request.json
    nivel = data.get('nivel', 'iniciante')
    objetivo = data.get('objetivo', 'geral')
    duracao = data.get('duracao', '30 minutos')

    prompt = f"Crie um treino de musculação para um usuário com nível {nivel}, com o objetivo de {objetivo} e com duração de {duracao}."
    #prompt = f"Create a strength training workout for a user with level {level}, with a goal of {goal} and a duration of {duration}."
    try:
        response = model.generate_content(prompt)
        treino = response.text
        return jsonify({'treino': treino})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

