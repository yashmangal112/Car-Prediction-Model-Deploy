import numpy as np
import pickle


#loading the saved model
loaded_model = pickle.load(open('C:/Users/hp/Desktop/car model deployment/car_predict.sav', 'rb'))

input_data = (2017,5.71,2400,0,0,0,0)

#changing the input data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print("You can sell this car at Rs.",prediction[0], "lakhs")