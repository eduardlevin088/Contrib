from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import config 

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup templates
templates = Jinja2Templates(directory="templates")


@app.get("/home")
def home(request: Request):
    return templates.TemplateResponse(
        "index.html", 
        {
            "request": request,
            "app_name": config.APP_NAME,
            "app_version": config.APP_VERSION
        }
    )


@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "app": config.APP_NAME}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=config.HOST, port=config.PORT)
