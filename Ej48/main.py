class Main:
    def vocales(self):
        cadenaTexto = input("Introduce la cadena de texto\n")
        print("Leyendo la cadena de texto\n")
        contador = {
            "A": 0,
            "E": 0,
            "I": 0,
            "O": 0,
            "U": 0
        }

        for letra in cadenaTexto:
            match letra.upper():
                case "A":
                    contador["A"] += 1
                case "E":
                    contador["E"] += 1
                case "I":
                    contador["I"] += 1
                case "O":
                    contador["O"] += 1
                case "U":
                    contador["U"] += 1

        vocal_mas_repetida = max(contador, key=contador.get)
        repeticiones = contador[vocal_mas_repetida]

        print(f"La vocal que más se repite es '{vocal_mas_repetida}' con {repeticiones} repeticiones")

if __name__ == "__main__":
    app = Main()
    app.vocales()
