
# Chat with Google Generative AI using Flask and Redis 🤖

This is a simple Flask application that allows you to chat with Google's Generative AI (LangChain) while leveraging Redis for caching responses. The application uses the ChatGoogleGenerativeAI model from LangChain to provide responses to user questions.

## Prerequisites 🛠️

Before running the application, ensure that you have the following dependencies installed:

- Python 3.x 🐍
- Flask 🌐
- langchain_google_genai 🧠
- redis-py 🔄

Install the required dependencies using:

```bash
pip install Flask langchain_google_genai redis
```

## Getting Started 🚀

1. Clone the repository:

```bash
git clone <repository-url>
cd <repository-directory>
```

2. Run the Flask application:

```bash
python app.py
```

3. Visit `http://localhost:5000` in your web browser.

## Usage 🤔💬

- Open the application in your web browser.
- Enter an image URL and ask a question.
- The application will use Google Generative AI to provide responses.
- Responses are cached using Redis for improved performance.


## Credits 🙌

- Flask: [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/) 🌐
- LangChain Google Generative AI: [https://github.com/langchain/google-genai](https://github.com/langchain/google-genai) 🧠
- Redis: [https://redis.io/](https://redis.io/) 🔄

## License 📝

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Happy chatting! 🚀🤖✨