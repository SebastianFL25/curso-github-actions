import os

def main():
    lenguage = os.getenv("LANGUAGE")
    nombre = os.getenv("USERNAME")
    print(f"¡Hola, Soy {nombre} y mi lenguage favorito es {lenguage} desde GitHub!")


if __name__ == "__main__":
    main()