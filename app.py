from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
return "<h1>Welcome to OE Portal 🚀</h1>"

if name == "main":
app.run(host="0.0.0.0", port=8080)
