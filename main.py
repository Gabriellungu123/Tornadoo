import asyncio
import tornado

class FormHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("formulario.html")  # busca en /templates

def make_app():
    return tornado.web.Application([
        (r"/", FormHandler),
    ],
    template_path="templates",  # carpeta donde está el HTML
    static_path="static")       # carpeta donde está el CSS



async def main():
    app = make_app()
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())