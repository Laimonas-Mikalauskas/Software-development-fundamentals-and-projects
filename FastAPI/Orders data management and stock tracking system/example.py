from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/program/{_id}/details")
async def read_program(_id: int):
    return {"program_id": _id, "status": "Program details would be here"}

@app.post("/program/")
async def create_program(program_data: dict):
    return {"program_data": program_data, "status": "Program created successfully"}

@app.put("/program/{_id}")
async def update_program(_id: int, program_data: dict):
    return {"program_id": _id, "program_data": program_data, "status": "Program updated successfully"}

@app.delete("/program/{_id}")
async def delete_program(_id: int):
    return {"program_id": _id, "status": "Program deleted successfully"}

@app.restore("/program/{_id}/details")
async def restore_program(_id: int):
    return {"program_id": _id, "status": "Program restored successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
