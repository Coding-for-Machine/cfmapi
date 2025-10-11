# from aiohttp import web
# from datetime import datetime

# app = web.Application()

# # http method get, post, put, delate
# def route(method: str, path: str):
#     def decorator(func):
#         async def wrapper(request, *args, **kwargs):
#             data = await func(request, *args, **kwargs)
#             if isinstance(data, dict):
#                 return web.json_response(data)
#             return web.Response(text=data)
        
#         if method == "get":
#             app.add_routes([web.get(path, wrapper)])
#         return wrapper
#     return decorator

# @route("get", "/")
# async def home_api(request):
#     return {"cfmapi": "version: v1"}

# @route("get", "/about")
# async def about_api(request):
#     data = {
#         "about": {
#             "title": "CfmAPi yaratayabmiz",
#             "time": datetime.now().isoformat()
#         }
#     }
#     return data

# @route("get", "/profile")
# async def profile(request):
#     return {
#         "profile": {
#             "username": "@asadbek",
#             "email": "codingformachine@gmail.com"
#         }
#     }


# if __name__=="__main__":
#     web.run_app(app, port=8000)


# CfmAPI -- version: 1.1

from cfmapi import CfmAPI


app = CfmAPI()


@app.get("/")
async def home(requets):
    return {"api": f"version:1.1, {requets}"}


@app.get("/about")
async def home(requets):
    data = {
        "about": {
            "title": "54654616",
            "discraption": "cfm api",
        }
    }
    return data

html_text = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Single File Example</title>
    <style>
        /* CSS styles go here */
        body {
            font-family: Arial, sans-serif;
            background-color: lightblue;
            text-align: center;
        }
        h1 {
            color: navy;
        }
    </style>
</head>
<body>
    <!-- HTML content goes here -->
    <h1>Welcome to a Single File Webpage!</h1>
    <p id="message">Click the button below.</p>
    <button onclick="changeMessage()">Change Message</button>

    <script>
        // JavaScript code goes here
        function changeMessage() {
            document.getElementById('message').innerText = 'The message has been changed by JavaScript!';
        }
    </script>
</body>
</html><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Single File Example</title>
    <style>
        /* CSS styles go here */
        body {
            font-family: Arial, sans-serif;
            background-color: lightblue;
            text-align: center;
        }
        h1 {
            color: navy;
        }
    </style>
</head>
<body>
    <!-- HTML content goes here -->
    <h1>Welcome to a Single File Webpage!</h1>
    <p id="message">Click the button below.</p>
    <button onclick="changeMessage()">Change Message</button>

    <script>
        // JavaScript code goes here
        function changeMessage() {
            document.getElementById('message').innerText = 'The message has been changed by JavaScript!';
        }
    </script>
</body>
</html>

"""
@app.get("/test")
async def test(request):
    return html_text
if __name__=="__main__":
    app.run()