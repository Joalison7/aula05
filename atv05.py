resp = "s"
while resp == "s":
    n1 = float(input("sua primeira nota: "))

    while n1<0 or n1>10:

        n1 = int(input("numero invalido digite novemente: "))

    n2 = float(input("sua segunda nota: "))

    while n2<0 or n2>10:

        n2 = int(input("numero invalido digite novemente: "))

    calculo = (n1+n2)/2

    print(calculo)

resp = input("deseja fazer novemente(s/n)")
