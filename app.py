from flask import Flask,render_template, url_for
import pandas as pd
app = Flask(__name__)
gps_data_list = []
    
df = pd.read_csv(r'datasets/classified_dataset.csv')
    
            
@app.route('/')
def arduino_iot():
    return render_template('index.html')


@app.route('/fence')
def fencing():
    return render_template('fence.html',tables=[df.to_html(classes='data')],titles=df.columns.values)
if __name__ == '__main__':
    app.run(debug=True)