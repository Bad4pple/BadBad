from fastapi import FastAPI
from badapple.api.routers import router
from badapple.api import inject


def create_app():
    app = FastAPI()
    inject.inject_adapter()
    app.include_router(router=router)
    return app

app = create_app()