from flask import Flask, render_template_string

app = Flask(__name__)

# HTML template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About Me</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 2em;
            padding: 2em;
            background-color: #f4f4f9;
        }
        .container {
            max-width: 600px;
            margin: auto;
            padding: 20px;
            background: #fff;
            border: 1px solid #ddd;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
        }
        p {
            line-height: 1.6;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Hello, I am Pooja M</h1>
        <p>I have the following skills:</p>
        <ul>
            <li>Linux</li>
            <li>AWS</li>
            <li>Terraform</li>
            <li>Kubernetes</li>
            <li>Docker</li>
            <li>SQL</li>
            <li>Maven</li>
            <li>Python</li>
            <li>Shell Scripting</li>
        </ul>
        <p>I am actively looking for a job where I can apply my skills and contribute to the growth of the organization.</p>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
