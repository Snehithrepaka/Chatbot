from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyC365fQM8BUcxHhrIh6RSBmeCn1bPOgD_c"  # Ensure that your API key is filled in
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index11.html')

@app.route('/chat', methods=['POST'])
def chat_response():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    try:
        # Send user input to the Google Gemini AI model
        response_raw = chat.send_message(user_input)
        
        # Extract text response
        response = response_raw.text
        return jsonify({"response": response})
    
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
