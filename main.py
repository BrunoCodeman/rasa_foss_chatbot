import asyncio
import logging
import uvloop
from aiohttp import web

intents = { "Bom dia. Tudo bem?": "Bom dia! Eu estou bem e você?", 
            "Tchau": "Até logo, nos vemos em breve!"}

async def index(request):
    return web.Response(text="hello")


async def chat_request(request):
    resp = {"text":""}

    try:
        phrase = await request.json()
        intent = phrase["intent"]
        resp["text"] = intents[intent]
    except Exception as ex:
        resp["text"] = "Não entendi!"
    finally:
        return web.json_response(resp)

async def config_app():
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    app = web.Application(loop=asyncio.get_event_loop())
    app.router.add_get("/", index)
    app.router.add_post("/chat", chat_request)
    return app

def main():
    logging.basicConfig(level=logging.DEBUG)
    app = config_app()
    web.run_app(app)

if __name__ == '__main__':
    main()