from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World! I'm PYTHON app-b!!"

if __name__ == '__main__':
    print("Servidor rodando na porta 8080...")
    app.run(host='0.0.0.0', port=8080)
