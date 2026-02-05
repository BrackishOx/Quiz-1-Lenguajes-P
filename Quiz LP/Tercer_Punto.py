class Recommender:
    def __init__(self):
        self.data = {}

    def addPurchase(self, user, product):
        self.data.setdefault(user, set()).add(product)

    def getRecommendations(self, user):
        if user not in self.data:
            return []

        user_products = self.data[user]
        recs = set()

        for u, products in self.data.items():
            if u != user and user_products & products:
                recs |= products

        return list(recs - user_products)


system = Recommender()
#Menu para interactuar con el sistema de recomendaciones
while True:
    print("\n- MENU  -")
    print("1. Registrar compra")
    print("2. Obtener recomendaciones")
    print("3. Salir")

    op = input("Seleccione una opción: ")

    if op == "1":
        u = input("Usuario: ")
        p = input("Producto: ")
        system.addPurchase(u, p)
        print("Compra registrada.")

    elif op == "2":
        u = input("Usuario: ")
        print("Recomendaciones:", system.getRecommendations(u))

    elif op == "3":
        print("Saliendo...")
        break

    else:
        print("opcion invalida")

