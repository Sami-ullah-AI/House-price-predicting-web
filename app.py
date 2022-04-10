import flask
import pickle
import pandas as pd
with open(f'model/Saniya_model.pkl', 'rb') as f:
    model = pickle.load(f)
app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
       return(flask.render_template('index.html')) 
    if flask.request.method == 'POST':
       property_type = flask.request.form['property_type']
       city= flask.request.form['city']
       province_name = flask.request.form['province_name']
       baths = flask.request.form['baths']
       bedrooms = flask.request.form['bedrooms']
       input_variables = pd.DataFrame([[property_type,city,province_name,baths,bedrooms]],columns=['Property Type','City','Province Name','Number of Baths','Number of Bedrooms'],index=['input'])
       prediction = model.predict(input_variables)[0]
       return flask.render_template('index.html',original_input={'Property Type':property_type,'City':city,'Province Name':province_name,'Number of Baths':baths,'Number of Bedrooms':bedrooms},result=int(prediction))
if __name__ == '__main__':
   app.run(debug=True)
