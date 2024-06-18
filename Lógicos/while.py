# Inicia um loop infinito
while True:
    # Solicita ao usuário que insira uma nota de 1 a 10 e converte a entrada para um número inteiro
    nota = int(input('Insira uma nota de 1 a 10: '))
    # Verifica se a nota inserida está entre 1 e 10
    if 1 <= nota <= 10:
        # Se a nota for maior ou igual a 7, imprime 'Aprovado' no console
        if nota >=7:
            print('Aprovado')
        # Se a nota for menor que 7, imprime 'Reprovado' no console
        else:
            print('Reprovado')
        # Interrompe o loop
        break
    # Se a nota inserida não estiver entre 1 e 10, imprime 'Nota invalida, digite uma nota entre 1 e 10' no console
    else:
        print('Nota invalida, digite uma nota entre 1 e 10')