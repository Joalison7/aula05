tentativa = 1
senhac = int(input("qual sua senha: "))

if senhac != 1234:
    while tentativa <= 2:
        senhac = int(input("senha incorreta tente novemente: "))
        tentativa += 1
        if senhac == 1234:
            print("senha correta")
    if senhac != 1234:
        print("senha incorreta")

else:
    print("senha correta")

#pin=1234
#tentativas=1
#msg