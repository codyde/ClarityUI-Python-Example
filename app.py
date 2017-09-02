# Run this file by having Python3 installed on your system and running "python3 app.py" from a prompt in the current app's directory.  

from flask import Flask, render_template, redirect, request, url_for, jsonify, session
from flask_assets import Bundle, Environment
import requests
from base64 import b64encode

app = Flask(__name__)
app.secret_key = "super secret key"

# Our bundling for css. This bundling starts in the static directory, so we just need to group them togehtre. You can see we create
# Objects off of each of these that we reference in our header.html file
env = Environment(app)
js = Bundle('js/clarity-icons.min.js', 'js/clarity-icons-api.js',
            'js/clarity-icons-element.js', 'js/custom-elements.min.js')
env.register('js_all', js)
css = Bundle('css/clarity-ui.min.css', 'css/clarity-icons.min.css')
env.register('css_all', css)

# App routes are how we build URLs in flask. / corresponds to the base, so http://localhost:5000/ would be the url. More examples later
@app.route('/', methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
# This is where we grab the variables from the form wwithin tihin the index.html page. We do a simple if/then to say if the password is true
# Then redirect to the next page 
        attempted_username = request.form['username']
        print(attempted_username)
        attempted_password = request.form['password']
        print(attempted_password)
        if attempted_username == "admin" and attempted_password == "password":
            session['logged_in'] = True
            session['wrong_pass'] = False
            session['username'] = request.form['username']
            return redirect(url_for('vmlist'))
        else:
            session['logged_in'] = False
            session['wrong_pass'] = True
    return render_template('index.html')

# As mentioned above, this route corresponds to http://localhost:5000/vms
@app.route('/vms')
def vmlist():
    req = requests.get('https://pyva.humblelab.com/rest/vcenter/vms') # Update this URL with the REST API details of your vCenter API. Mine is up so you can use it for testing. 
    req_json = req.json()
    return render_template('vms.html', vms = req_json)

@app.route('/workflows')
def workflows():
# For vRO you'll want to update the URL to your vRO base url (https://hlcloud.humblelab.com for me) 
    url = 'https://hlcloud.humblelab.com'
# Update the username:password field to match yours, i.e. administrator@vsphere.local:VMware1!
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