# Define uma função chamada parImpar que recebe um argumento chamado numero
def parImpar(numero):
    # Se o número for divisível por 2 (ou seja, se o resto da divisão por 2 for 0), então o número é par
    if numero % 2 == 0:
        print('par')  # Imprime 'par' no console
    else:
        print('impar')  # Se o número não for divisível por 2, imprime 'impar' no console

# A função parImpar é chamada aqui sem nenhum argumento, o que causará um erro, pois a função espera um argumento
parImpar()

# Solicita ao usuário que digite um número inteiro e armazena a entrada do usuário na variável 'entrada'
entrada = input("Digite um número inteiro: ")

# Tenta executar o bloco de código a seguir
try:
    # Converte a entrada do usuário para um número inteiro e armazena na variável 'numero'
    numero = int(entrada)
    # Chama a função parImpar com o número fornecido pelo usuário e armazena o resultado na variável 'resultado'
    resultado = parImpar(numero)
    # Imprime uma mensagem formatada no console informando se o número fornecido pelo usuário é par ou ímpar
    print(f"O número {numero} é {resultado}")

# Se ocorrer um erro ao tentar executar o bloco de código acima (por exemplo, se o usuário digitar uma string em vez de um número),
# o bloco de código a seguir será executado
except:
    # Imprime uma mensagem de erro no console
    print("Erro: Você digitou uma string é necessário digitar um numero inteiro")

    