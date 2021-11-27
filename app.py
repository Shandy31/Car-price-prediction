from flask import Flask,render_template,request
import pickle
import sklearn
import numpy as np

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
	return render_template('Home.html')
	# return "hello"
@app.route('/predict', methods = ['POST'])
def predict():
	if request.method == 'POST':
		name = request.form["name"]
		fuelType = request.form["fuel"]
		aspiration = request.form["aspiration"]
		doors = request.form["door"]
		stroke = request.form["stroke"]
		horsepower = request.form["horsepower"]
		peakrpm = request.form["peakrpm"]
		enginetype = request.form["enginetype"]

		
		cars = {'alfa-romero': 1,'audi': 2,'bmw': 3,'chevrolet': 4,'dodge': 5,'honda': 6,'isuzu': 7,'jaguar': 8,'mazda': 9,'buick': 10,'mercury': 11,'mitsubishi': 12,'nissan': 13,'peugeot': 14,'plymouth': 15,'porsche': 16,'renault': 17,'saab': 18,'subaru': 19,'toyota': 20,'volkswagen': 21,'volvo': 22}
		fueltypes = {'gas': 1,'diesel': 0}
		aspirations = {'std': 0,'turbo':1}
		doorss = {'four': 1,'two': 0}
		enginetypes = {'ohc':0,'ohcf':5,'ohcv':3 ,'dohc':2,'l':6,'rotor':4,'dohcv':1}

		name = cars[name]
		fuelType = fueltypes[fuelType]
		aspiration = aspirations[aspiration]
		doors = doorss[doors]
		enginetype = enginetypes[enginetype]

		model = pickle.load(open("car_pred.pkl","rb"))
		array = [[name,fuelType,aspiration,doors,stroke,horsepower,peakrpm,enginetype]]
		array = [np.array(array[0],dtype = 'float64')]
		price = model.predict(array)
		result = 'The price of the car is: ' + '$ ' +str(int(price[0]))
		return render_template("Home.html", a = result)

		
if __name__ == '__main__':
	app.run(debug=False, host = "0.0.0.0")
