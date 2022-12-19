import pickle 
import json
import config1
import numpy as np


class Diabetes():

    def __init__(self,user_data):

        self.user_data=user_data
        self.model_file_path= 'log_reg.pkl'
        
    def load_save_data(self):

        with open (self.model_file_path,'rb') as f:

            self.model_file = pickle.load(f)

        with open ('project_data.json','r') as f:
            self.proj_data = json.load(f)



    def get_predicted_outcome(self):

        self.load_save_data()

        col_len = len(self.proj_data['columns'])
        # print(col_len)

        test_array =np.zeros(col_len)

        test_array[0]=eval(self.user_data['Glucose'])
        test_array[1]=eval(self.user_data['BloodPressure'])
        test_array[2]=eval(self.user_data['SkinThickness'])
        test_array[3]=eval(self.user_data['Insulin'])
        test_array[4]=eval(self.user_data['BMI'])
        test_array[5]=eval(self.user_data['DiabetesPedigreeFunction'])
        test_array[6]=eval(self.user_data['Age'])

        predict_outcome = self.model_file.predict([test_array])[0]


        print("Diabetes Prediction :",predict_outcome)

        return predict_outcome

if __name__ == '__main__':

    ins=Diabetes()
    ins





