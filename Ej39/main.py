class Main:
    def binarioDecimal(self):
        numBinario = input("Introduce el numero binario\n")
        indice = 0 
        sol = 0
        for num in reversed(numBinario):
            sol += (2 ** indice) * int(num)
            indice += 1
        print(f"\nEl número decimal es {sol}")  

if __name__ == "__main__":
    app = Main()
    app.binarioDecimal()
