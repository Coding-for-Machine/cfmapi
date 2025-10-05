from aiohttp import web
from datetime import datetime

app = web.Application()

# http method get, post, put, delate
def route(method: str, path: str):
    def decorator(func):
        async def wrapper(request, *args, **kwargs):
            data = await func(request, *args, **kwargs)
            if isinstance(data, dict):
                return web.json_response(data)
            return web.Response(text=data)
        
        if method == "get":
            app.add_routes([web.get(path, wrapper)])
        return wrapper
    return decorator

@route("get", "/")
async def home_api(request):
    return {"cfmapi": "version: v1"}

@route("get", "/about")
async def about_api(request):
    data = {
        "about": {
            "title": "CfmAPi yaratayabmiz",
            "time": datetime.now().isoformat()
        }
    }
    return data

@route("get", "/profile")
async def profile(request):
    return {
        "profile": {
            "username": "@asadbek",
            "email": "codingformachine@gmail.com"
        }
    }


if __name__=="__main__":
    web.run_app(app, port=8000)