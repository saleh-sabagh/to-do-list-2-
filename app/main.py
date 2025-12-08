from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import JSONResponse, RedirectResponse

from app.api.routers import api_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="To-Do List API",
        version="0.3.0",
        description="FastAPI-based Web API for managing projects and tasks.",
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(GZipMiddleware, minimum_size=500)

    @app.get("/", include_in_schema=False)
    def root_redirect():
        return RedirectResponse(url="/docs")

    @app.get("/api/v1/health", tags=["health"])
    def healthcheck():
        return {"status": "ok"}

    @app.exception_handler(ValueError)
    def handle_value_error(_, exc: ValueError):
        return JSONResponse(status_code=400, content={"detail": str(exc)})

    app.include_router(api_router, prefix="/api/v1")
    return app


app = create_app()

