traductor={
    "JUICIOSO":"Persona responsable ",
    "ACHICHAY":"Se lo utiliza para decir que esta haciendo frio",
    "BACANO": "Algo para indicar que es bonito"
}

 

palabra=input("Ingres la palabra a traducir: ")

if palabra in traductor:
    print(traductor[palabra])

else:
    print("No esta esta en mi base de datos")
