from flask import Flask,request,render_template,jsonify

app=Flask('__name__')

@app.route('/',methods=['POST','GET'])
def home():
    return "<h1>This is my first application in Heroku Platform</h1>"


if __name__ == '__main__':
    app.run()