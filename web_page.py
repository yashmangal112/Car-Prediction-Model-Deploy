import numpy as np
import pickle
import streamlit as st
import pandas as pd
#loading the saved model
st.set_option('browser.gatherUsageStats', False)
loaded_model = pickle.load(open('C:/Users/hp/Desktop/car model deployment/car_predict.sav', 'rb'))

df = pd.read_csv('C:/Users/hp/Desktop/car model deployment/cardata.csv')
df = df['Kms_Driven']
# year_data = df['Year']

def prediction(input_data):
    # input_data = (2017,5.71,2400,0,0,0,0)

    #changing the input data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    if prediction >=0:
        # return "You can sell this car at Rs.",prediction[0], "lakhs"
        prediction = f'**{prediction[0]}**'
        return f"You can sell this car at Rs. {prediction} lakhs"
    else:
         return "This car model can not be sold. Please change your data 😊"

def main():
        #giving a title
        st.title('Car Price Prediction System')

        #getting the input data from the user
        # Year,Selling_Price,Present_Price,Kms_Driven,Fuel_Type,Seller_Type,Transmission,Owner
        # year = df1.unique()
        Year = st.number_input("Year", step=1, min_value=2003)
        # year_value = year_data.unique()
        # select_year = st.select_box('Select', year_value)
        # st.write('selected', select_year)


        # st.write("Selected year is:", Year)
        Present_Price = st.number_input(label='Showroom Price(in lakh) ', step=1.,format="%.2f", min_value=0.32)
        Fuel_Type = st.selectbox('select your fuel type',('Petrol', 'Diesel', 'CNG'))
        Seller_Type = st.selectbox('select your seller type',('Dealer', 'Individual'))
        # Seller_Type = st.radio('select your seller type',('Dealer', 'Individual'))
        Transmission = st.selectbox('select your transmission type',('Manual', 'Automatic'))

        Owner = st.slider('Select the number of owner', min_value=0, max_value=3, step=1)
        # st.write('Owner is', Owner)

        # Get unique values from the 'Kms_driven' column
        kms_values = df.unique()
        # Dropdown button
        Kms_Driven = st.selectbox('Select Kms Driven', kms_values)

        # st.write('Selected Kms Driven:', Kms_Driven)


        if Fuel_Type == 'Petrol':
             fuel_p = 0
        elif Fuel_Type == 'Diesel':
             fuel_p = 1     
        elif Fuel_Type == 'CNG':
             fuel_p = 2
        if Seller_Type == 'Dealer':
             sell = 0
        elif Seller_Type == 'Individual':
             sell = 1
        if Transmission == 'Manual':
             transmission = 0
        elif Transmission == 'Automatic':
            transmission =1                         
        #& code for prediction
        Selling_Price = ""

        #Creating a button

        if st.button('calculate selling Price'):
             Selling_Price = prediction([Year, Present_Price, Kms_Driven,fuel_p,sell,transmission, Owner])
             if Selling_Price !="This car model can not be sold. Please change your data 😊":
                st.balloons()
        st.success(Selling_Price)

        with st.container():
            # st.subheader('About the developer')
            # st.subheader('A subheader with _italics_ :blue[colors] and emojis :love')
            # st.markdown('This prediction system is developed by **:blue[Yash Mangal]**')
            text = 'This prediction system is developed by'
            st.write(f'**{text}**' " [yash mangal](https://yashmangal112.vercel.app) with ❤️ ")
            # st.write(f'**{text}**' " [yash mangal](https://yashmangal112.vercel.app) with ❤️ ")
            # st.markdown("check out this **[Yash Mangal]**(%s)" % url)
            # st.markdown("This text is :red[colored red], and About the developer **:blue[developer]** and bold.")
            # st.markdown(":green[$\sqrt{x^2+y^2}=1$] is a Pythagorean identity. :linkedin:")

        
if __name__ == '__main__':
    main()

# values = st.slider(
# 'Select a range of values',
# 0.0, 100.0, (25.0, 75.0))
# st.write('Values:', values)
