"""
this is a github codespaces test
"""

from flask import Flask

app = Flask('Codespace Test')

@app.route('/index')
def print_hello():
    """Flask 欢迎"""
    print("Welcome Codespaces!")
    print("Well, Not Bad!")


if __name__ == '__main__':
    app.run()
