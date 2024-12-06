from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello World! Doamna Miron va iubesc!!!!'

@app.route('/factorial/<int:factorial>')
def factorial(factorial):
    result = 1
    factorial = int(factorial)
    print(factorial)
    for i in range (1, factorial + 1):
        result *= i
    return f"Factorial of {factorial} is {result}"