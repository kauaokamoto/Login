import create
import data

login = False

while True:
    nameArray = data.loadFile()
    name = input("Qual é o seu nome?: ").lower()
    
    found = False
    existsUser = None

    for user in nameArray:
        if name in user["name"]:
            found = True
            existsUser = user
            print(f"Você é {user["característica"]}, mas qual é a sua senha?")
            break  

    if not found and login == False:
        print("Você é beta, não tem conta!\n")
        create.register_fun()
        continue

    if not found and login == True:
        print("Você é beta, demais. Tente novamente!\n")
        continue 
    
    attempts = 0
    password = ""
    
    while attempts < 5:
        password = input("Qual é a senha?: ").strip()
        attempts += 1
        
        if password == user["senha"]:
            print("Você fez login com sucesso!")
            exit()
        
        if attempts == 5:
            print("Beta tentou virar o alpha e foi mogado!")
        else:
            print(f"Senha incorreta. Você só tem mais {5 - attempts} tentativa(s) até ser mogado.")