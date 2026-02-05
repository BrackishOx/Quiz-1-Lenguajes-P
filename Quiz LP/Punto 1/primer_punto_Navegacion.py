class BrowserNavigation:
    def __init__(self):
        self.back = []
        self.forward = []
        self.current = None

    def loadPage(self, url):
        if self.current:
            self.back.append(self.current)
        self.current = url
        self.forward.clear()
        print(f"Página cargada: {self.current}")

    def goBack(self):
        if not self.back:
            print("No hay páginas anteriores.")
            return
        self.forward.append(self.current)
        self.current = self.back.pop()
        print(f"Volviste a: {self.current}")

    def goForward(self):
        if not self.forward:
            print("No hay páginas siguientes.")
            return
        self.back.append(self.current)
        self.current = self.forward.pop()
        print(f"Avanzaste a: {self.current}")

    def show(self):
        print(f"Página actual: {self.current}")

#Menu para interactuar con la Navegacion
if __name__ == "__main__":
    browser = BrowserNavigation()

    while True:
        print("\n1. Cargar página")
        print("2. Atrás")
        print("3. Adelante")
        print("4. Ver página actual")
        print("0. Salir")

        op = input("Seleccione una opción: ")

        if op == "1":
            url = input("Ingrese la URL: ")
            browser.loadPage(url)
        elif op == "2":
            browser.goBack()
        elif op == "3":
            browser.goForward()
        elif op == "4":
            browser.show()
        elif op == "0":
            print("Saliendo del navegador...")
            break
        else:
            print("Opción inválida.")