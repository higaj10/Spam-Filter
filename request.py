from flask import Flask
from flask import Flask , redirect , url_for , request , render_template , jsonify , json
import requests

# create app
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # show html form
        return '''
            <form method="post">
                <input type="text" name="expression" />
                <input type="submit" value="Submit" />
            </form>
        '''
    elif request.method == 'POST':
        # calculate result
        expression = request.form.get('expression')
        url = "http://127.0.0.1:5000/predict"
        payload = {"text":expression}
        r = requests.post(url , data=json.dumps(payload))
        # print(r.text)
        a = r.text
        return (a)

# run app
if __name__ == '__main__':
    app.run('127.0.0.1' , 5001 , debug = True)