from contextlib import contextmanager
from fastapi import FastAPI
from common.loadJson import LoadJson
from routes.api_service_routes import ApiServiceRoutes
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from hypercorn.config import Config
from hypercorn.asyncio import serve







app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(               #setting up the middlware
    CORSMiddleware, 
    allow_origins = ["http://localhost:3000","*"],
    allow_credentials = True,
    allow_methods = ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers = ["*"]
)



v1 = ApiServiceRoutes(app)
v1.initialize()

config = LoadJson()



if __name__ == "__main__":
 
    configs = {
        "bind": f"{config.json['HOST']}:{config.json['PORT']}"         # refer coomon/configFiles/config.json
    }
    asyncio.run(serve(app, Config.from_mapping(configs)))
 
