import pydocumentdb.documents as documents
import pydocumentdb.document_client as document_client

from flask import Flask, jsonify

app = Flask(__name__)
settings = {
    'host': '',
    'master_key': '',
    'database_id': '',
    'collection_id': ''
}

HOST = settings['host']
MASTER_KEY = settings['master_key']
DATABASE_ID = settings['database_id']

@app.route('/')
def index():
  return app.send_static_file('index.html')

@app.route('/api/data')
def get_data():
  client = document_client.DocumentClient(HOST, {'masterKey': MASTER_KEY} )
  collection_link = 'dbs/Tasks/colls/Survey Summary'
  query = {'query': "SELECT * FROM c WHERE c.id = 'languages' "}

  document = list(client.QueryDocuments(collection_link, query)).pop()
  return jsonify(document)

if __name__ == '__main__':
  app.run()
