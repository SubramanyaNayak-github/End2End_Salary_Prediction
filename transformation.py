import pickle

#Converting words to integer values
education_mapping = {"Bachelor's": 1, "Master's": 2, "PhD": 3}

with open('education_mapping.pkl', 'wb') as mapping_file:
    pickle.dump(education_mapping, mapping_file)