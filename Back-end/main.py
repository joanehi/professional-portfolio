from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="My Portfolio API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


PROJECTS_DATABASE = [
    {
        "id": 1,
        "title": "Full-Stack Portfolio & API",
        "description": "A responsive personal portfolio powered by a custom Python FastAPI backend and vanilla HTML/CSS/JS frontend.",
        "tech_stack": ["Python", "FastAPI", "HTML5", "CSS3", "JavaScript"],
        "github_url": "https://github.com",
        "live_url": "https://vercel.app"
    },
    {
        "id": 2,
        "title": "Python Automation Project",
        "description": "A backend automation tool built to streamline data processing and API integration.",
        "tech_stack": ["Python", "SQL"],
        "github_url": "https://github.com",
        "live_url": ""
    }
]

@app.get("/")
def home():
    return {
        "status": "online",
        "message": "Portfolio API is running. Visit /projects to view project data."
    }

@app.get("/projects")
def get_projects():
    return PROJECTS_DATABASE