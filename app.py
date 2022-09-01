import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle


app = Flask(__name__)
model = pickle.load(open("ada.pkl", "rb"))

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict',methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        
        months_as_customer = int(request.form['months_as_customer'])
        
        age = int(request.form['age'])
        
        policy_deductable = int(request.form['policy_deductable'])
        
        umbrella_limit = int(request.form['umbrella_limit'])
        
        insured_sex = request.form['insured_sex']
        if(insured_sex=="male"):
            Male = 1
            Female = 0
        elif(insured_sex=="female"):
            Male = 0
            Female = 1
        else:
            Male = 0
            Female = 0
            
        insured_education_level = request.form['insured_education_level']
        if(insured_education_level=="associate"):
            Associate = 1
            College = 0
            High_School = 0
            JD = 0
            Masters = 0
            MD = 0
            PhD = 0
        elif(insured_education_level=="college"):
            Associate = 0
            College = 1
            High_School = 0
            JD = 0
            Masters = 0
            MD = 0
            PhD = 0
        elif(insured_education_level=="high School"):
            Associate = 0
            College = 0
            High_School = 1
            JD = 0
            Masters = 0
            MD = 0
            PhD = 0
        elif(insured_education_level=="jd"):
            Associate = 0
            College = 0
            High_School = 0
            JD = 1
            Masters = 0
            MD = 0
            PhD = 0
        elif(insured_education_level=="masters"):
            Associate = 0
            College = 0
            High_School = 0
            JD = 0
            Masters = 1
            MD = 0
            PhD = 0
        elif(insured_education_level=="md"):
             Associate = 0
             College = 0
             High_School = 0
             JD = 0
             Masters = 0
             MD = 1
             PhD = 0
        elif(insured_education_level=="phd"):
            Associate = 0
            College = 0
            High_School = 0
            JD = 0
            Masters = 0
            MD = 0
            PhD = 1
        else:
            Associate = 0
            College = 0
            High_School = 0
            JD = 0
            Masters = 0
            MD = 0
            PhD = 0
    
        insured_occupation = request.form['insured_occupation']
        if(insured_occupation=="adm-clerical"):
            Admin_Clerical = 1
            Armed_Forces = 0
            Craft_Repair = 0
            Executive_Managerial = 0
            Farming_Fishing = 0
            Handlers_Cleaners = 0
            Machine_op_inspect = 0
            Other_Service = 0
            Private_House_Service = 0
            Professional_Speciality = 0
            Protective_Service = 0
            Sales = 0
            Tech_support = 0
            Transport_Moving = 0         
        elif(insured_occupation=="armed-forces"):
            Admin_Clerical = 0
            Armed_Forces = 1
            Craft_Repair = 0
            Executive_Managerial = 0
            Farming_Fishing = 0
            Handlers_Cleaners = 0
            Machine_op_inspect = 0
            Other_Service = 0
            Private_House_Service = 0
            Professional_Speciality = 0
            Protective_Service = 0
            Sales = 0
            Tech_support = 0
            Transport_Moving = 0
        elif(insured_occupation=="craft-repair"):
            Admin_Clerical = 0
            Armed_Forces = 0
            Craft_Repair = 1
            Executive_Managerial = 0
            Farming_Fishing = 0
            Handlers_Cleaners = 0
            Machine_op_inspect = 0
            Other_Service = 0
            Private_House_Service = 0
            Professional_Speciality = 0
            Protective_Service = 0
            Sales = 0
            Tech_support = 0
            Transport_Moving = 0
        elif(insured_occupation=="exec-managerial"):
            Admin_Clerical = 0
            Armed_Forces = 0
            Craft_Repair = 0
            Executive_Managerial = 1
            Farming_Fishing = 0
            Handlers_Cleaners = 0
            Machine_op_inspect = 0
            Other_Service = 0
            Private_House_Service = 0
            Professional_Speciality = 0
            Protective_Service = 0
            Sales = 0
            Tech_support = 0
            Transport_Moving = 0
        elif(insured_occupation=="farming-fishing"):
            Admin_Clerical = 0
            Armed_Forces = 0
            Craft_Repair = 0
            Executive_Managerial = 0
            Farming_Fishing = 1
            Handlers_Cleaners = 0
            Machine_op_inspect = 0
            Other_Service = 0
            Private_House_Service = 0
            Professional_Speciality = 0
            Protective_Service = 0
            Sales = 0
            Tech_support = 0
            Transport_Moving = 0
        elif(insured_occupation=="handlers-cleaners"):
            Admin_Clerical = 0
            Armed_Forces = 0
            Craft_Repair = 0
            Executive_Managerial = 0
            Farming_Fishing = 0
            Handlers_Cleaners = 1
            Machine_op_inspect = 0
            Other_Service = 0
            Private_House_Service = 0
            Professional_Speciality = 0
            Protective_Service = 0
            Sales = 0
            Tech_support = 0
            Transport_Moving = 0
        elif(insured_occupation=="machine-op-inspct"):
            Admin_Clerical = 0
            Armed_Forces = 0
            Craft_Repair = 0
            Executive_Managerial = 0
            Farming_Fishing = 0
            Handlers_Cleaners = 0
            Machine_op_inspect = 1
            Other_Service = 0
            Private_House_Service = 0
            Professional_Speciality = 0
            Protective_Service = 0
            Sales = 0
            Tech_support = 0
            Transport_Moving = 0
        elif(insured_occupation=="other-service"):
            Admin_Clerical = 0
            Armed_Forces = 0
            Craft_Repair = 0
            Executive_Managerial = 0
            Farming_Fishing = 0
            Handlers_Cleaners = 0
            Machine_op_inspect = 0
            Other_Service = 1
            Private_House_Service = 0
            Professional_Speciality = 0
            Protective_Service = 0
            Sales = 0
            Tech_support = 0
            Transport_Moving = 0
        elif(insured_occupation=="priv-house-serv"):
            Admin_Clerical = 0
            Armed_Forces = 0
            Craft_Repair = 0
            Executive_Managerial = 0
            Farming_Fishing = 0
            Handlers_Cleaners = 0
            Machine_op_inspect = 0
            Other_Service = 0
            Private_House_Service = 1
            Professional_Speciality = 0
            Protective_Service = 0
            Sales = 0
            Tech_support = 0
            Transport_Moving = 0
        elif(insured_occupation=="prof-specialty"):
            Admin_Clerical = 0
            Armed_Forces = 0
            Craft_Repair = 0
            Executive_Managerial = 0
            Farming_Fishing = 0
            Handlers_Cleaners = 0
            Machine_op_inspect = 0
            Other_Service = 0
            Private_House_Service = 0
            Professional_Speciality = 1
            Protective_Service = 0
            Sales = 0
            Tech_support = 0
            Transport_Moving = 0
        elif(insured_occupation=="protective-serv"):
            Admin_Clerical = 0
            Armed_Forces = 0
            Craft_Repair = 0
            Executive_Managerial = 0
            Farming_Fishing = 0
            Handlers_Cleaners = 0
            Machine_op_inspect = 0
            Other_Service = 0
            Private_House_Service = 0
            Professional_Speciality = 0
            Protective_Service = 1
            Sales = 0
            Tech_support = 0
            Transport_Moving = 0
        elif(insured_occupation=="sales"):
            Admin_Clerical = 0
            Armed_Forces = 0
            Craft_Repair = 0
            Executive_Managerial = 0
            Farming_Fishing = 0
            Handlers_Cleaners = 0
            Machine_op_inspect = 0
            Other_Service = 0
            Private_House_Service = 0
            Professional_Speciality = 0
            Protective_Service = 0
            Sales = 1
            Tech_support = 0
            Transport_Moving = 0
        elif(insured_occupation=="tech-support"):
            Admin_Clerical = 0
            Armed_Forces = 0
            Craft_Repair = 0
            Executive_Managerial = 0
            Farming_Fishing = 0
            Handlers_Cleaners = 0
            Machine_op_inspect = 0
            Other_Service = 0
            Private_House_Service = 0
            Professional_Speciality = 0
            Protective_Service = 0
            Sales = 0
            Tech_support = 1
            Transport_Moving = 0
        elif(insured_occupation=="transport-moving"):
            Admin_Clerical = 0
            Armed_Forces = 0
            Craft_Repair = 0
            Executive_Managerial = 0
            Farming_Fishing = 0
            Handlers_Cleaners = 0
            Machine_op_inspect = 0
            Other_Service = 0
            Private_House_Service = 0
            Professional_Speciality = 0
            Protective_Service = 0
            Sales = 0
            Tech_support = 0
            Transport_Moving = 1
        else:
            Admin_Clerical = 0
            Armed_Forces = 0
            Craft_Repair = 0
            Executive_Managerial = 0
            Farming_Fishing = 0
            Handlers_Cleaners = 0
            Machine_op_inspect = 0
            Other_Service = 0
            Private_House_Service = 0
            Professional_Speciality = 0
            Protective_Service = 0
            Sales = 0
            Tech_support = 0
            Transport_Moving = 0            
            
        incident_type = request.form['incident_type']
        if(incident_type=="multi-vehicle Collision"):
            Multi_vehicle_Collision = 1
            Parked_Car = 0
            Single_Vehicle_Collision = 0
            Vehicle_Theft = 0
        elif(incident_type=="parked car"):
            Multi_vehicle_Collision = 0
            Parked_Car = 1
            Single_Vehicle_Collision = 0
            Vehicle_Theft = 0
        elif(incident_type=="single vehicle Collision"):
            Multi_vehicle_Collision = 0
            Parked_Car = 0
            Single_Vehicle_Collision = 1
            Vehicle_Theft = 0
        elif(incident_type=="vehicle theft"):
            Multi_vehicle_Collision = 0
            Parked_Car = 0
            Single_Vehicle_Collision = 0
            Vehicle_Theft = 1
        else:
            Multi_vehicle_Collision = 0
            Parked_Car = 0
            Single_Vehicle_Collision = 0
            Vehicle_Theft = 0
            
        collision_type = request.form['collision_type']
        if(collision_type=="front collision"):
            Front_Collision = 1
            Rear_Collision = 0
            Side_Collision = 0
        elif(collision_type=="rear collision"):
            Front_Collision = 0
            Rear_Collision = 1
            Side_Collision = 0
        elif(collision_type=="side collision"):
            Front_Collision = 0
            Rear_Collision = 0
            Side_Collision = 1
        else:
            Front_Collision = 0
            Rear_Collision = 0
            Side_Collision = 0

        incident_severity = request.form['incident_severity']
        if(incident_severity=="major damage"):
            Major_Damage = 1
            Minor_Damage = 0
            Total_Loss = 0
            Trivial_Damage = 0
        elif(incident_severity=="minor damage"):
            Major_Damage = 0
            Minor_Damage = 1
            Total_Loss = 0
            Trivial_Damage = 0
        elif(incident_severity=="total loss"):
            Major_Damage = 0
            Minor_Damage = 0
            Total_Loss = 1
            Trivial_Damage = 0
        elif(incident_severity=="trivial damage"):
            Major_Damage = 0
            Minor_Damage = 0
            Total_Loss = 0
            Trivial_Damage = 1
        else:
            Major_Damage = 0
            Minor_Damage = 0
            Total_Loss = 0
            Trivial_Damage = 0
                     
        authorities_contacted = request.form['authorities_contacted']
        if(authorities_contacted=="ambulance"):
            Ambulance = 1
            Fire = 0
            None_ = 0
            Other = 0
            Police = 0
        elif(authorities_contacted=="fire"):
            Ambulance = 0
            Fire = 1
            None_ = 0
            Other = 0
            Police = 0
        elif(authorities_contacted=="none"):
            Ambulance = 0
            Fire = 0
            None_ = 1
            Other = 0
            Police = 0
        elif(authorities_contacted=="other"):
            Ambulance = 0
            Fire = 0
            None_ = 0
            Other = 1
            Police = 0
        elif(authorities_contacted=="police"):
            Ambulance = 0
            Fire = 0
            None_ = 0
            Other = 0
            Police = 1
        else:
            Ambulance = 0
            Fire = 0
            None_ = 0
            Other = 0
            Police = 0
            
        incident_hour_of_the_day = int(request.form['incident_hour_of_the_day'])
        
        number_of_vehicles_involved = int(request.form['number_of_vehicles_involved'])
            
        property_damage = request.form['property_damage']
        if(property_damage=="yes"):
            Damage_Yes = 1
            Damage_No = 0
        elif(property_damage=="no"):
            Damage_Yes = 0
            Damage_No = 1
        else:
            Damage_Yes = 0
            Damage_No = 0
            
        bodily_injuries = int(request.form['bodily_injuries'])
        
        witnesses = int(request.form['witnesses'])
        
        police_report_available = request.form['police_report_available']
        if(police_report_available=="yes"):
            Report_Yes = 1
            Report_No = 0
        elif(police_report_available=="no"):
            Report_Yes = 0
            Report_No = 1
        else:
            Report_Yes = 0
            Report_No = 0
        
        total_claim_amount = int(float(request.form['total_claim_amount']))
        
        prediction=model.predict([[
            months_as_customer,
            age,
            policy_deductable,
            umbrella_limit,
            incident_hour_of_the_day,
            number_of_vehicles_involved,
            bodily_injuries,
            witnesses,
            total_claim_amount,
            Male,
            College,
            High_School,
            JD,
            MD,
            Masters,
            PhD,
            Armed_Forces,
            Craft_Repair,
            Executive_Managerial,
            Farming_Fishing,
            Handlers_Cleaners,
            Machine_op_inspect,
            Other_Service,
            Private_House_Service,
            Professional_Speciality,
            Protective_Service,
            Sales,
            Tech_support,
            Transport_Moving,
            Parked_Car,
            Single_Vehicle_Collision,
            Vehicle_Theft,
            Rear_Collision,
            Side_Collision,
            Minor_Damage,
            Total_Loss,
            Trivial_Damage,
            Fire,
            None_,
            Other,
            Police,
            Damage_Yes,
            Report_Yes
        ]])
        
        output = prediction [0]
        if (output == 0):
            output="VALID Claim"
        else:
            output="FRAUDULENT Claim"
                
        return render_template('home.html', prediction_text = 'This is a ' + str(output))
   
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
