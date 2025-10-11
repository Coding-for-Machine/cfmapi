from aiohttp import web

class CfmAPI:
    def __init__(self):
        self._app = web.Application()
    
    def get(self, path):
        def decorator(func):
            async def wrapper(request, *args, **kwargs):
                data = await func(request, *args, **kwargs) #  "Asadbek", name="Asadbek"
                if isinstance(data, dict):
                    return web.json_response(data)
                return web.Response(text=data, content_type="text/html")
            self._app.add_routes([web.get(path, wrapper)])
            return wrapper
        return decorator
    # def post(self, path):
    # def put(self, path):
    # def delete(self, path):

    
    def run(self, host: str = "0.0.0.0", port: int = 8000):
        web.run_app(self._app, host=host, port=port)