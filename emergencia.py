import asyncio
import tornado.web


# ============================
#   HANDLERS (Controladores)
# ============================

class ControladorFormulario(tornado.web.RequestHandler):
    def get(self):
        # Se ejecuta cuando el usuario entra a "/" con método GET
        self.render("formulario.html")  # Busca en /templates


class SubmitHandler(tornado.web.RequestHandler):
    def post(self):
        # Recoge los datos enviados desde el formulario
        usuario = self.get_argument("nombre")
        email = self.get_argument("email")

        # Aquí podrías validar login, guardar datos en BD, etc.

        # Redirige a otra página
        self.redirect("/pagina")


class PaginaHandler(tornado.web.RequestHandler):
    def get(self):
        # Renderiza la página final
        self.render("pagina.html")


# ============================
#   APLICACIÓN TORNADO
# ============================

def make_app():
    return tornado.web.Application([
        (r"/", ControladorFormulario),   # Página principal
        (r"/submit", SubmitHandler),     # Procesa formulario
        (r"/pagina", PaginaHandler),     # Página final
    ],
    template_path="templates",  # Carpeta de HTML
    static_path="static")       # Carpeta de CSS/JS/imagenes


# ============================
#   FUNCIÓN PRINCIPAL
# ============================

async def main():
    app = make_app()
    app.listen(8888)  # Servidor en puerto 8888
    await asyncio.Event().wait()  # Mantiene el servidor activo


# ============================
#   PUNTO DE ENTRADA
# ============================

if __name__ == "__main__":
    asyncio.run(main())