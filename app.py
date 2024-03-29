from flask import Flask, render_template, jsonify
import urllib3
import json

app = Flask(__name__)
http = urllib3.PoolManager()
iis_now_api = 'http://api.open-notify.org/iss-now.json'

@app.route('/')
def index():
    response = http.request('GET', '{0}'.format(iis_now_api))
    data = json.loads(response.data.decode('utf-8'))

    with open('iss-now.log', 'a') as f:
        f.write(str(data) + '\n')

    return render_template('index.html', data=data)

@app.route('/status')
def status():
    try:
        # Check if ISS API is available
        response = http.request('GET', '{0}'.format(iis_now_api))
        if response.status == 200:
            return jsonify({
                'status': 'OK',
                'http_status': response.status,
                }), 200
        else:
            return jsonify({'status': 'ISS API is not available'}), 503
    except Exception as e:
        return jsonify({
            'status': 'ISS API is not available',
            'error_message': '{0}'.format(str(e))
            }), 503

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)