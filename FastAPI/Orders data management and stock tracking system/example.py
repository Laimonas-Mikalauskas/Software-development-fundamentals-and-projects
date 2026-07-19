try:
    from fastapi import FastAPI
except ImportError:
    import sys
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "fastapi"])
    from fastapi import FastAPI

app = FastAPI()

try:
    from uvicorn import uvicorn
except ImportError:
    import sys
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "uvicorn"])
    from uvicorn import uvicorn


@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/program/{program_id}/details")
async def read_program(program_id: int):
    return {"program_id": program_id, "status": "Program details would be here"}

@app.post("/program/")
async def create_program(program_data: dict):
    return {"program_data": program_data, "status": "Program created successfully"}

@app.put("/program/{program_id}")
async def update_program(program_id: int, program_data: dict):
    return {"program_id": program_id, "program_data": program_data, "status": "Program updated successfully"}

@app.delete("/program/{program_id}")
async def delete_program(program_id: int):
    return {"program_id": program_id, "status": "Program deleted successfully"}

# Replaced the invalid @app.restore decorator with a POST to a clear /restore path
@app.post("/program/{program_id}/restore")
async def restore_program(program_id: int):
    return {"program_id": program_id, "status": "Program restored successfully"}


if __name__ == "__main__":
    # import uvicorn here to avoid unresolved import at module import time in some editors
    # use "module:app" so uvicorn can reload when run as a script; add reload=True during development if desired
    uvicorn.run("example:app", host="0.0.0.0", port=8000, reload=True)
