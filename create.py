import data


data.nameArray = data.loadFile()

def register_fun():
    while True:
        newName = input("Defina o seu nome: ").lower().strip()

        existsName = False
        for users in data.nameArray:
            if newName in users["name"]:
                existsName = True
                break

        if existsName:
            print("ERRO: Este nome já está cadastrado. Tente outro!\n")
            continue

        new_nickName = input("Qual é a sua característica?: ").lower().strip()
        new_password = input("Crie uma senha: ").strip()
        new_ID = len(data.nameArray)
        
        data.nameArray.append(
            {
                "num": new_ID,
                "name": [newName],
                "característica": new_nickName,
                "senha": new_password,
            }
        )

        data.saveFile(data.nameArray)

        print("\nConta criada com sucesso!")
        break