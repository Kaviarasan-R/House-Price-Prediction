from flask import Flask, render_template, request
import pickle
import numpy as np

filename = 'house-linReg-model.pkl'
regressor = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    
    temp_array=list()
    
    if request.method == 'POST':
        
        neighborhood = request.form['neighborhood']
        
        if neighborhood == 'Bloomington Heights':
            temp_array = temp_array + [15]
        elif neighborhood == 'Bluestem':
            temp_array = temp_array + [11]
        elif neighborhood == 'Briardale':
            temp_array = temp_array + [2]
        elif neighborhood == 'Brookside':
            temp_array = temp_array + [3]
        elif neighborhood == 'Clear Creek':
            temp_array = temp_array + [17]
        elif neighborhood == 'College Creek':
            temp_array = temp_array + [14]
        elif neighborhood == 'Crawford':
            temp_array = temp_array + [16]
        elif neighborhood == 'Edwards':
            temp_array = temp_array + [5]
        elif neighborhood == 'Gilbert':
            temp_array = temp_array + [13]
        elif neighborhood == 'Iowa DOT and Rail Road':
            temp_array = temp_array + [0]
        elif neighborhood == 'Meadow Village':
            temp_array = temp_array + [1]
        elif neighborhood == 'Mitchell':
            temp_array = temp_array + [9]
        elif neighborhood == 'North Ames':
            temp_array = temp_array + [8]
        elif neighborhood == 'Northridge':
            temp_array = temp_array + [22]
        elif neighborhood == 'Northpark Villa':
            temp_array = temp_array + [11]
        elif neighborhood == 'Northridge Heights':
            temp_array = temp_array + [21]
        elif neighborhood == 'Northwest Ames':
            temp_array = temp_array + [12]
        elif neighborhood == 'Old Town':
            temp_array = temp_array + [4]
        elif neighborhood == 'South & West of Iowa State University':
            temp_array = temp_array + [7]
        elif neighborhood == 'Sawyer':
            temp_array = temp_array + [6]
        elif neighborhood == 'Sawyer West':
            temp_array = temp_array + [10]
        elif neighborhood == 'Somerset':
            temp_array = temp_array + [18]
        elif neighborhood == 'Stone Brook':
            temp_array = temp_array + [20]
        elif neighborhood == 'Timberland':
            temp_array = temp_array + [19]
        elif neighborhood == 'Veenker':
            temp_array = temp_array + [11]
            
        
        overall_quality = request.form['overall_quality']
        
        if overall_quality == 'Very Excellent':
            temp_array = temp_array + [10]
        elif overall_quality == 'Excellent':
            temp_array = temp_array + [9]
        elif overall_quality == 'Very Good':
            temp_array = temp_array + [8]
        elif overall_quality == 'Good':
            temp_array = temp_array + [7]
        elif overall_quality == 'Above Average':
            temp_array = temp_array + [6]
        elif overall_quality == 'Average':
            temp_array = temp_array + [5]
        elif overall_quality == 'Below Average':
            temp_array = temp_array + [4]
        elif overall_quality == 'Fair':
            temp_array = temp_array + [3]
        elif overall_quality == 'Poor':
            temp_array = temp_array + [2]
        elif overall_quality == 'Very Poor':
            temp_array = temp_array + [1]
        
        year_sold = int( request.form['year_sold'])
        
        remodel_year = int( request.form['remodel_year'])
        
        new_year = year_sold - remodel_year
        temp_array = temp_array + [new_year]
        
        
        basement_exposure = request.form['basement_exposure']
        
        if basement_exposure == 'Good Exposure':
            temp_array = temp_array + [4]
        elif basement_exposure == 'Average Exposure':
            temp_array = temp_array + [3]
        elif basement_exposure == 'Mimimum Exposure':
            temp_array = temp_array + [2]
        elif basement_exposure == 'No Exposure':
            temp_array = temp_array + [1]
        elif basement_exposure == 'No Basement':
            temp_array = temp_array + [0]
        
        
        living_area = int(request.form['living_area'])
        
        grLivArea = np.log(living_area)
        temp_array = temp_array + [grLivArea]
        
        
        kitchen_quality = request.form['kitchen_quality']

        if kitchen_quality == 'Excellent':
            temp_array = temp_array + [3]
        elif kitchen_quality == 'Good':
            temp_array = temp_array + [2]
        elif kitchen_quality == 'Typical/Average':
            temp_array = temp_array + [1]
        elif kitchen_quality == 'Fair':
            temp_array = temp_array + [0]
        elif kitchen_quality == 'Poor':
            temp_array = temp_array + [0]
            
        fireplace_quality = request.form['fireplace_quality']

        if fireplace_quality == 'Excellent':
            temp_array = temp_array + [5]
        elif fireplace_quality == 'Good':
            temp_array = temp_array + [4]
        elif fireplace_quality == 'Average':
            temp_array = temp_array + [3]
        elif fireplace_quality == 'Fair':
            temp_array = temp_array + [2]
        elif fireplace_quality == 'Poor':
            temp_array = temp_array + [0]
        elif fireplace_quality == 'No Fireplace':
            temp_array = temp_array + [1]
            
            
        garage_location = request.form['garage_location']

        if garage_location == 'More than one type of garage':
            temp_array = temp_array + [3]
        elif garage_location == 'Attached to home':
            temp_array = temp_array + [4]
        elif garage_location == 'Basement Garage':
            temp_array = temp_array + [0]
        elif garage_location == 'Built-In':
            temp_array = temp_array + [5]
        elif garage_location == 'Car Port':
            temp_array = temp_array + [1]
        elif garage_location == 'Detached from home':
            temp_array = temp_array + [2]
        elif garage_location == 'No Garage':
            temp_array = temp_array + [0]            
            
        garage_finish = request.form['garage_finish']

        if garage_finish == 'Finished':
            temp_array = temp_array + [3]
        elif garage_finish == 'Rough Finished':
            temp_array = temp_array + [2]
        elif garage_finish == 'Unfinished':
            temp_array = temp_array + [1]
        elif garage_finish == 'No Garage':
            temp_array = temp_array + [0]


        garage_cars = int(request.form['garage_cars'])
        temp_array = temp_array + [garage_cars]
        
        data = np.array([temp_array])
        
        my_pred = int(regressor.predict( data )[0])

        return render_template('result.html', lower_limit = (my_pred)-10000, upper_limit = (my_pred)+10000)


if __name__ == '__main__':
	app.run(debug=True)
