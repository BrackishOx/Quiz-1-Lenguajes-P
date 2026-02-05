class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word):
        node = self.trie
        for c in word:
            node = node.setdefault(c, {})
        node["*"] = True

    def autocomplete(self, prefix):
        node = self.trie
        for c in prefix:
            if c not in node:
                return []
            node = node[c]
        return self._dfs(node, prefix)

    def _dfs(self, node, prefix):
        words = [prefix] if "*" in node else []
        for c in node:
            if c != "*":
                words += self._dfs(node[c], prefix + c)
        return words


trie = Trie()
#Menu para interactuar con el sistema de autocompletado
while True:
    print("\n- Auto Completar -")
    print("1. Insertar palabra")
    print("2. Autocompletar prefijo")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        palabra = input("Ingrese palabra: ").lower()
        trie.insert(palabra)
        print("Palabra insertada.")

    elif opcion == "2":
        prefijo = input("Ingrese prefijo: ").lower()
        print("Resultados:", trie.autocomplete(prefijo))

    elif opcion == "3":
        print("Saliendo...")
        break

    else:
        print("Opción inválida")