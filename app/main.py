from fastapi import FastAPI

app = FastAPI(title="Debt CRM Cloud Test")

@app.get("/")
def root():
    return {"status": "running"}

@app.get("/health")
def health():
    return {"ok": True}
