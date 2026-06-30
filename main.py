from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()


def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data


@app.get("/")
def hello():
    return {"message": "Patient Management System API"}


@app.get("/about")
def about():
    return {"message": "Fully functional API to manage patient records."}


@app.get("/view")
def view():
    return load_data()


@app.get("/patient/{patient_id}")
def view_patient(
    patient_id: str = Path(..., description="The ID of the patient to retrieve")
):
    data = load_data()

    if patient_id in data:
        return data[patient_id]

    raise HTTPException(status_code=404, detail="Patient not found")


@app.get("/sort")
def sort_patients(
    sort_by: str = Query(
        ...,
        description="Sort on the basis of height, weight, or BMI"
    ),
    order: str = Query(
        "asc",
        description="Sort order: 'asc' or 'desc'"
    ),
):

    valid_fields = ["height", "weight", "bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid sort field. Valid fields are: {', '.join(valid_fields)}"
        )

    if order not in ["asc", "desc"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid sort order. Valid orders are: 'asc' or 'desc'"
        )

    data = load_data()

    reverse_order = order == "desc"

    sorted_data = sorted(
        data.values(),
        key=lambda patient: patient[sort_by],
        reverse=reverse_order
    )

    return sorted_data