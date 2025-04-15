alunos = int(input("quantos aulunos: "))
x = 1
soma = 0

while x <= alunos:
    nota = int(input("qual sua nota: "))
    soma += nota
    x+=1

media = soma/alunos
print(media)
