from flask import Flask, request, jsonify
from flask_cors import CORS
from compiler import TamilCompiler

app = Flask(__name__)
# Enable CORS so your frontend app can talk to this API
CORS(app)

@app.route('/api/compile', methods=['POST'])
def compile_code():
    try:
        data = request.get_json()
        tamil_code = data.get('code', '')
        lang = data.get('lang', 'tamil')
        
        compiler = TamilCompiler(lang)
        python_code = compiler.translate(tamil_code)
        
        return jsonify({
            'success': True,
            'python_code': python_code
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500