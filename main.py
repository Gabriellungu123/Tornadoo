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


class SubmitHandler(tornado.web.RequestHandler):
    def post(self):
        usuario = self.get_argument("nombre")
        email = self.get_argument("email")

        # Aquí podrías validar login, guardar datos, etc.

        self.redirect("/pagina")


class PaginaHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("pagina.html")


async def main():
    app = make_app()
    app.listen(8888)
    await asyncio.Event().wait()

def make_app():
    return tornado.web.Application([
        (r"/", FormHandler),
        (r"/submit", SubmitHandler),
        (r"/pagina", PaginaHandler),
    ],
    template_path="templates",
    static_path="static")

if __name__ == "__main__":
    asyncio.run(main())