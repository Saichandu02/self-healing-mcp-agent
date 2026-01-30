from fastapi import FastAPI, HTTPException
import os

app = FastAPI()

@app.get("/health")
def health():
    # Trigger the log BEFORE the exception
    if not os.getenv("DB_SECRET"):
        print("CRITICAL: DB_SECRET missing!", flush=True) # Forces immediate output
        raise HTTPException(status_code=500, detail="CRITICAL: DB_SECRET missing!")
    return {"status": "ok"}