from flask import Flask, render_template_string
app = Flask(__name__)
HTML = """
 <!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>OE Portal</title>
    <style>
        body {
            font-family: Arial;
            background: #0f172a;
            color: white;
            text-align: center;
            padding-top: 100px;
        }
        h1 {
            font-size: 50px;
        }
        p {
            font-size: 20px;
            color: #cbd5f5;
        }
        .btn {
            margin-top: 30px;
            padding: 12px 25px;
            background: #22c55e;
            color: white;
            border-radius: 8px;
            text-decoration: none;
        }
    </style>
</head>
<body> 
<h1>Welcome to OE Portal</h1>
<p>Your Operational Excellence Dashboard</p>
<a href="#" class="btn">Enter System</a> 
 </body>
</html>
""" 

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="8.0.8.0", port=5000)
