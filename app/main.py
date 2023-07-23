
from fastapi import FastAPI, Depends, status, HTTPException
from routes.api import router as api_router

app = FastAPI()

app.include_router(api_router)

# generate example python code making pandas dataframe from csv file


@app.get("/health_check")
async def service_health_check():
    return {"message": "service active.."}
