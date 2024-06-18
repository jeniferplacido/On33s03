# Define uma função chamada 'soma' que recebe dois argumentos: 'a' e 'b'
def soma (a, b):
    # A função retorna a soma dos argumentos 'a' e 'b'
    return a + b

# Solicita ao usuário que digite o primeiro número e armazena a entrada do usuário na variável 'entrada1'
entrada1 = input("Digite o primeiro número: ")
# Solicita ao usuário que digite o segundo número e armazena a entrada do usuário na variável 'entrada2'
entrada2 = input("Digite o segundo número: ")

# Tenta executar o bloco de código a seguir
try:
    # Converte a primeira entrada do usuário para um número flutuante e armazena na variável 'numero1'
    numero1= float(entrada1)
    # Converte a segunda entrada do usuário para um número flutuante e armazena na variável 'numero2'
    numero2= float(entrada2)
    # Chama a função 'soma' com os números fornecidos pelo usuário e armazena o resultado na variável 'resultado'
    resultado = soma(numero1, numero2)
    # Imprime uma mensagem formatada no console informando a soma dos números fornecidos pelo usuário
    print(f'A soma de {numero1} e {numero2} é {resultado}')

# Se ocorrer um erro ao tentar executar o bloco de código acima (por exemplo, se o usuário digitar uma string em vez de um número),
# o bloco de código a seguir será executado
except:
    # Imprime uma mensagem de erro no console
    print("Entrada inválida")