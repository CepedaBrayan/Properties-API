from fastapi import FastAPI

from .owners import routes as owner_routes
from .properties import routes as prop_routes

app = FastAPI(
    title="Property Management API",
    description="Properties project, tech challenge",
    version="0.0.1",
)

# Version 1
app.include_router(owner_routes.router, prefix="/api/v1")
app.include_router(prop_routes.router, prefix="/api/v1")
