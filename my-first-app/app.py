


from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def home():
    return '<h1>Hello from my Docker container on AWS!</h1>'
 
@app.route('/health')
def health():
    return '<h1>App is healthy!</h1>'
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
