from flask import Flask,render_template, url_for
app = Flask(__name__)
gps_data_list = []
    

    
            
@app.route('/')
def arduino_iot():
    return render_template('index.html')

@app.route('/vehicle_track')
def vehicle_tracker():
    with open(r'gps_data.txt','r') as file:
        while file.read(1):
            data = file.readline()
            gps_data_list.append(data)
    file.close()
    return render_template('track_vehicle.html',data=gps_data_list)

if __name__ == '__main__':
    app.run(debug=True)