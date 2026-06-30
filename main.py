from fastapi import FastAPI ,Path
import json


app = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)

    return data
@app.get("/")
def hello():
    return {"message": "Patient management system API"}

@app.get('/about')
def about():
    return {"message": "Fully functional API to manage you patient records "}

@app.get('/view')
def view():
    data = load_data()
    return data 

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str):
    data = load_data()
    for patient in data:
        if patient_id== patient_id:
            return data[patient_id]
    return {"message": "Patient not found"}