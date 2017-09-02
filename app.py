from flask import Flask, render_template, redirect, request, url_for, jsonify, session
from flask_assets import Bundle, Environment
import requests
from base64 import b64encode

app = Flask(__name__)
app.secret_key = "super secret key"

env = Environment(app)
js = Bundle('js/clarity-icons.min.js', 'js/clarity-icons-api.js',
            'js/clarity-icons-element.js', 'js/custom-elements.min.js')
env.register('js_all', js)
css = Bundle('css/clarity-ui.min.css', 'css/clarity-icons.min.css')
env.register('css_all', css)

@app.route('/', methods=["GET", "POST"])
def homepage():
    if request.method == "POST": 
        attempted_username = request.form['username']
        print(attempted_username)
        attempted_password = request.form['password']
        print(attempted_password)
        if attempted_username == "admin" and attempted_password == "password":
            session['logged_in'] = True
            session['wrong_pass'] = False
            session['username'] = request.form['username']
            return redirect(url_for('homepage'))
        else:
            session['logged_in'] = False
            session['wrong_pass'] = True
    return render_template('index.html')

@app.route('/vms')
def vmlist():
    req = requests.get('https://pyva.humblelab.com/rest/vcenter/vms')
    req_json = req.json()
    return render_template('vms.html', vms = req_json)

@app.route('/workflows')
def workflows():
    url = 'https://hlcloud.humblelab.com'
    value = b64encode(b"username:password").decode("ascii")
    headers = {
        'Authorization': 'Basic '+ value,
        'content-type': 'application/json',
        'accept' : 'application/json' 
    }
    req = requests.get('{}/vco/api/workflows/'.format(url), verify=False, headers=headers)
    return render_template('workflows.html', flows=req.json()['link'])


if __name__ == '__main__':
    app.run(debug=True)