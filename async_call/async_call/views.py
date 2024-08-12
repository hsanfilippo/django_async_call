import asyncio
import httpx
from time import sleep
from django.http import HttpResponse


def home_sync_view(request):
    return HttpResponse("<h2>"
        "Para ver o que fiz no exercício, navegue para "
        "<a href='http://localhost:8000/exercicio/'>localhost:8000/exercicio/</a></h2>"
        "")


async def exercicio():
    test_list = ["Oi tutor", "Tudo bem aí?", "Espero que sim :)"]
    msg_say = "Henrique diz:"
    for item in test_list:
        await asyncio.sleep(1.5)
        print(f"{msg_say} {item}")
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org")
        print(r)


async def exercicio_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(exercicio())
    return HttpResponse(""
        "<h2>Da uma olhada no seu terminal :)</h2>"
        "<img width='300px' src='https://imgs.search.brave.com/KlF1KjIJTORBRPoPdPULJT_WLaKBjskeyQkDkBBAhXs/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9paDEu/cmVkYnViYmxlLm5l/dC9pbWFnZS40MTEx/NTMzMzk3Ljc4NTMv/ZmxhdCw3NTB4LDA3/NSxmLXBhZCw3NTB4/MTAwMCxmOGY4Zjgu/anBn' />"
    "")
