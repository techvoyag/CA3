from flask import Flask

app = Flask(__name__)

@app.route('/calc/mul/<int:a>/<int:b>', methods=['GET'])
def Multiply( a, b ): 
    
    return str(a*b)

@app.route('/calc/add/<int:a>/<int:b>', methods=['GET'])
def add(a,b):
    return str(a+b)

@app.route('/calc/sub/<int:a>/<int:b>', methods=['GET'])
def sub(a,b):
    return str(a-b)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
