import bcrypt
from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from routes.api import router as api_router
import uvicorn


config = dotenv_values(".env")

app = FastAPI()

@app.on_event("startup")
def startup_mongo_client():
    salt = bcrypt.gensalt() 
    app.mongodb_client = MongoClient(config["URL_MONGO_ATLAS"])
    app.database = app.mongodb_client[config["DBNAME_ATLAS"]]
    print("Connect to mongodb !!!")

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
    
