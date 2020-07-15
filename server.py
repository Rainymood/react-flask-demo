from flask import Flask
from flask import jsonify
import time
app = Flask(__name__)

@app.route('/time')
def get_current_time():
    return jsonify({'time': time.time()})

if __name__ == '__main__':
   app.run(debug=True)