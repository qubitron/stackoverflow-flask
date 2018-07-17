from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  print("Hello!")
  return app.send_static_file('index.html')

@app.route('/api/data')
def get_data():
  print("Data!")
  return app.send_static_file('data.json')

if __name__ == '__main__':
  app.run()
