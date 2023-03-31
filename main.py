from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from pydantic import BaseModel

app = FastAPI()


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Seach Job API",
        version="1.1.0",
        description="This is a OpenAPI schema for our Job API",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

class Job(BaseModel):
    id: int
    title: str
    company: str
    location: str
    description: str

jobs = [
    Job(
        id=1,
        title="Software Engineer",
        company="Tech Inc.",
        location="Tokyo",
        description="Develop and maintain web applications."
    ),
    Job(
        id=2,
        title="Data Scientist",
        company="Data Corp.",
        location="Osaka",
        description="Analyze and interpret complex data sets.",
    ),
    Job(
        id=3,
        title="Product Manager",
        company="Innovate Ltd.",
        location="Nagoya",
        description="Define product vision and deliver the best user experience.",
    )
]

@app.get("/jobs", response_model=Job)
async def root():
    return jobs[1]

# @app.get("/jobs/{job_id}", response_model=Job)
# async def get_job(job_id: int):
#     for job in jobs:
#         if job.id == job_id:
#             return job
#     return None

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)