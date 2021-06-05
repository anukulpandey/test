from flask import Flask
app = Flask(_name_)

@app.route('/',methods=['GET']
def home():
  return 'Hello World'

app.run()
