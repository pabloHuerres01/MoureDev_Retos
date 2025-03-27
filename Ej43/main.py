class Main:
    def celsiusAfarenheit(self):
        celsius=input(f"Introduce el numero de grados en celsius")
        print(float(celsius)*(9/5)+32)

if __name__ == "__main__":
    app = Main()
    app.celsiusAfarenheit()