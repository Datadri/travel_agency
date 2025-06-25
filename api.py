from fastapi import FastAPI, HTTPException
from project.utils.parser import parse_natural_input_to_travel_request
from project.models import TravelRequest

app = FastAPI()


@app.post("/parse", response_model=TravelRequest)
def parse(text: str):
    try:
        return parse_natural_input_to_travel_request(text)
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc))
