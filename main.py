import os
import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

# Django ORM 
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from apps.views import router as apps_router


if __name__ == "__main__":
    app = FastAPI()
    app.include_router(apps_router)
    uvicorn.run(app, host="0.0.0.0", port=8000)