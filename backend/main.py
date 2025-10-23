from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
@app.get("/api/health") 
async def health_check(): 
    return {"status": "ok", "app": "oct23App3", "description": "test"}
@app.get("/api/data") 
async def get_data(): 
    return {"message": "Hello from oct23App3!", "data": []}
if __name__ == "__main__": 
    uvicorn.run(app, host="0.0.0.0", port=8000)