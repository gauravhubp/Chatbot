from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load knowledge base data
with open('knowledge_base.json', 'r', encoding='utf-8') as f:
    knowledge_base = json.load(f)

# Function to query knowledge base
def query_knowledge_base(query):
    for entry in knowledge_base:
        if query.lower() in entry['question'].lower():
            return entry['answer']
    return "Sorry, I couldn't find any relevant information."

# Flask route to handle chatbot requests
@app.route('/chatbot', methods=['POST'])
def chatbot():
    if request.method == 'POST':
        user_input = request.json['message']
        response = {"message": query_knowledge_base(user_input)}
        return jsonify(response)
    else:
        return jsonify({"error": "Method Not Allowed"}), 405  # Return a 405 Method Not Allowed error

if __name__ == '__main__':
    app.run(debug=True)
