from aiohttp import web

async def handle(request):
    name = request.match_info.get('name', 'Anonymous')
    text = "Hello, " + name
    return web.Response(text=text)

app = web.Application()
app.router.add_get('/', handle)
app.router.add_get('/{name}', handle)

web.run_app(app)

'''
Above, we have created a simple web server using the aiohttp library, which responds with a personalized greeting.

Run the Script:
    'python app.py'

    Access the Web Server:
        Open a web browser and navigate to http://localhost:8080/.
            You should see the response: Hello, Anonymous
        Navigate to http://localhost:8080/yourname (replace yourname with any name you choose).
            You should see the response: Hello, yourname

Example Test Cases

    Access the Root URL:
        URL: http://localhost:8080/
        Expected Response: Hello, Anonymous

    Access a Personalized URL:
        URL: http://localhost:8080/Ramakant
        Expected Response: Hello, Ramakant

    Access Another Personalized URL:
        URL: http://localhost:8080/Manish
        Expected Response: Hello, Manish
'''