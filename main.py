from flask import Flask, request, jsonify
from flask_cors import CORS  # Импортируем CORS
from retrive import rag_pipeline

app = Flask(__name__)

# Разрешаем CORS для всех доменов или только для конкретного порта
CORS(app, origins=["http://localhost:3020"])  # Это разрешит запросы только с http://localhost:3020

@app.route('/ask', methods=['POST'])
def ask_yandex_gpt():
    data = request.json
    prompt = data.get('prompt', '')

    if not prompt:
        return jsonify({'error': 'No prompt provided'}), 400

    try:
        # Отправляем запрос в RAG пайплайн
        result = rag_pipeline(prompt)
        
        # Возвращаем результат на клиентскую сторону
        return jsonify({'response': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == 'main':
    app.run(port=5001)