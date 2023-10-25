from flask import Flask, request, jsonify
from newspaper import Article
import logging

# Configure the logging level and format
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    stream=sys.stdout,
)

# Initialize the Flask application
flask_app = Flask(__name__)


url = 'https://www.theverge.com/2023/9/27/23892900/microsoft-dall-e-windows-11-paint-cocreator'
article = Article(url)

article.download()
article.parse()

print(article.title)
print(article.authors)
print(article.publish_date)
print(article.top_image)
# print(article.text)

# Run the app
if __name__ == '__main__':
    logging.info("Starting Flask app, listening on port %d", 8000)
    flask_app.run(host='0.0.0.0', port=8000)