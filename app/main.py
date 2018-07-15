from flask import Flask, render_template
import ptvsd

# Allow other computers to attach to ptvsd at this IP address and port, using the secret
ptvsd.enable_attach("shhh", address = ('0.0.0.0', 4001))

# Pause the program until a remote debugger is attached
ptvsd.wait_for_attach()

app = Flask(__name__)

import os
print(os.getcwd())
print("Starting up!")

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
