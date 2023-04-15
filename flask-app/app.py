from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'It works! You deployed your app on an ECS cluster!'

if __name__ == '__main__':
    app.run(debug=True)
