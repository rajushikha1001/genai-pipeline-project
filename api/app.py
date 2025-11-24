import os
from flask import Flask, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer

app = Flask(__name__)

# Configuration
MODEL_PATH = os.environ.get('MODEL_PATH', './model/gpt2') 
# The model files will be copied into this path inside the Docker container

# Global variables to load the model once
model = None
tokenizer = None

def load_model():
    """Load the model and tokenizer from the specified path."""
    global model, tokenizer
    try:
        # Load the model and tokenizer from the saved directory
        tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
        model = AutoModelForCausalLM.from_pretrained(MODEL_PATH)
        print(f"Successfully loaded model from {MODEL_PATH}")
    except Exception as e:
        print(f"Error loading model: {e}")
        # In a real app, this should crash if the model is essential

# Load the model on startup
with app.app_context():
    load_model()

@app.route('/generate', methods=['POST'])
def generate_text():
    """API endpoint for text generation."""
    if not model or not tokenizer:
        return jsonify({"error": "Model not loaded"}), 500

    data = request.get_json(silent=True)
    if not data or 'prompt' not in data:
        return jsonify({"error": "Missing 'prompt' in request body"}), 400

    prompt = data['prompt']
    
    # Simple generation parameters
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    
    # Generate text (limiting to 50 tokens for quick inference)
    output = model.generate(
        input_ids, 
        max_length=len(input_ids[0]) + 50, 
        num_return_sequences=1,
        do_sample=True, 
        top_k=50, 
        top_p=0.95
    )
    
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    return jsonify({
        "prompt": prompt,
        "generated_text": generated_text
    })

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({"status": "ok", "model_loaded": model is not None})

if __name__ == '__main__':
    # Download the model files locally before running for testing
    if not os.path.exists(MODEL_PATH):
        print(f"Model path {MODEL_PATH} not found. Downloading GPT-2.")
        AutoModelForCausalLM.from_pretrained("gpt2").save_pretrained(MODEL_PATH)
        AutoTokenizer.from_pretrained("gpt2").save_pretrained(MODEL_PATH)
        print("Download complete. Starting server.")
        
    app.run(host='0.0.0.0', port=5000)