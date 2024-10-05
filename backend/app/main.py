from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .data_retrieval import load_sustainability_data, load_christmas_data

app = FastAPI()

# Add CORS middleware to allow requests from the frontend (localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React app URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/sustainability")
def get_sustainability_data():
    data = load_sustainability_data()
    return data.to_dict(orient='records')

@app.get("/christmas")
def get_christmas_data():
    data = load_christmas_data()
    return data.to_dict(orient='records')
