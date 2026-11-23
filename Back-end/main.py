from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="My Portfolio API")

# CRUCIAL: This allows your HTML file to safely talk to your Python backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from any origin (like your local HTML file)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# This is a sample list of your projects. You can add more here!
PROJECTS_DATABASE = [
    {
        "id": 1,
        "title": "Full-Stack Personal Portfolio & API",
        "description": "A responsive web application built from scratch with semantic HTML/CSS and JavaScript, dynamically fetching project metadata from an asynchronous Python FastAPI backend.",
        "tech_stack": ["Python", "FastAPI", "HTML5", "CSS3", "JavaScript", "REST API"],
        "github_url": "https://github.com/joanehi/professional-portfolio",
        "live_url": ""
    },
    {
        "id": 2,
        "title": "Bookstore Inventory & GUI Application",
        "description": "A desktop bookstore management system built in Python using a modular architecture that separates core backend logic from the graphical user interface.",
        "tech_stack": ["Python", "GUI", "Modular Architecture", "Software Design"],
        "github_url": "https://github.com/joanehi/python_bookstore_gui",
        "live_url": ""
    },
   {
        "id": 3,
        "title": "Snack Man Interactive Browser Game",
        "description": "Engineered the complete JavaScript game engine and added custom interactive features on top of a provided HTML/CSS base template, implementing movement controls, collision detection, and score tracking.",
        "tech_stack": ["JavaScript", "DOM Manipulation", "Event Handling", "HTML5/CSS3"],
        "github_url": "https://github.com/joanehi/SnackMan-",
        "live_url": ""
    },
    
]

@app.get("/")
def home():
    return {"message": "Welcome to my Portfolio API. Go to /projects to see my work!"}

@app.get("/projects")
def get_projects():
    # This endpoint returns your project list as JSON data
    return PROJECTS_DATABASE