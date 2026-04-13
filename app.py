print("Welcome To Docker")
from flask import Flask
from PIL import Image

app = Flask(__name__)

@app.route("/")
def home():
    # Create a simple image
    img = Image.new('RGB', (200, 200), color='blue')
    img.save("output.png")

    return "Image created successfully!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
