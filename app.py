from flask import Flask, render_template, request, jsonify
import json
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
import redis

app = Flask(__name__)

# Connect to the local Redis server
redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

# Initialize ChatGoogleGenerativeAI model
llm = ChatGoogleGenerativeAI(model="gemini-pro-vision")

# Function to get or set the cached response
def get_or_set_cached_response(cache_key, callback):
    cached_response = redis_client.get(cache_key)
    
    if cached_response:
        # If the response is in the cache, return it
        return json.loads(cached_response)
    else:
        # If the response is not in the cache, calculate it using the provided callback
        response = callback()
        redis_client.set(cache_key, json.dumps(response))
        return response

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        image_url = request.form['image_url']
        return render_template('index.html', image_url=image_url)
    return render_template('index.html', image_url=None)

@app.route('/ask_question', methods=['GET'])
def ask_question():
    # Get user question from the query parameters
    user_question = request.args.get('question', '')
    latest_image_url = request.args.get('image_url', '')

    # Define a cache key based on user question and image URL
    cache_key = f"{user_question}:{latest_image_url}"

    # Define a callback function to calculate the response
    def calculate_response():
        message = HumanMessage(
            content=[
                {
                    "type": "text",
                    "text": user_question,
                },
                {"type": "image_url", "image_url": latest_image_url},
            ]
        )
        return str(llm.invoke([message])).replace("content=' ","")[:-1]

    # Get or set the cached response
    response = get_or_set_cached_response(cache_key, calculate_response)
    print(response)

    # Return a JSON response with user question and server response
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
