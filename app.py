import numpy as np
from flask import Flask, request, jsonify ,render_template
import pickle


app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

with open('education_mapping.pkl', 'rb') as mapping_file:
    education_mapping = pickle.load(mapping_file)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    age_str = request.form.get('Age')
    gender = request.form.get('Gender')
    education_level_text = request.form.get('EducationLevel')
    years_of_experience_str = request.form.get('YearsOfExperience')


    # Convert to float if possible
    age = float(age_str) 
    years_of_experience = float(years_of_experience_str)  
    
    # Gender mapping
    gender_mapping = {'Female': 0, 'Male': 1}
    if gender in gender_mapping:
        mapped_gender = gender_mapping[gender]
    else:
        return render_template('index.html', prediction_text='Invalid gender value: {}'.format(gender))


    # Education level mapping
    education_mapping = {"Bachelor's": 1, "Master's": 2, 'PhD': 3}
    if education_level_text in education_mapping:
        mapped_education_level = education_mapping.get(education_level_text)
    else:
        return render_template('index.html', prediction_text='Invalid education level value: {}'.format(education_level_text))

    # Debugging: Print values before prediction
    print("Debugging - Values before prediction:")
    print("age:", age)
    print("mapped_gender:", mapped_gender)
    print("mapped_education_level:", mapped_education_level)
    print("years_of_experience:", years_of_experience)



    # Make prediction
    try:
        prediction = model.predict([[age, mapped_gender, mapped_education_level, years_of_experience]])
        output = round(prediction[0], 2)
        return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))
    except Exception as e:
        return render_template('index.html', prediction_text='Error during prediction: {}'.format(str(e)))



if __name__ == "__main__":
    app.run(debug=True)