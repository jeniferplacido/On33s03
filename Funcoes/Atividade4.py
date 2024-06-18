# Define uma função chamada 'contarCaracteres' que recebe um argumento: 'texto'
def contarCaracteres(texto):
    # A função retorna o número de caracteres no 'texto'
    return len(texto)

# Solicita ao usuário que digite uma palavra ou frase e armazena a entrada do usuário na variável 'entrada'
entrada = input('Digite uma palavra ou uma frase: ')

# Tenta executar o bloco de código a seguir
try:
    # Chama a função 'contarCaracteres' com a entrada fornecida pelo usuário e armazena o resultado na variável 'caracteres'
    caracteres = contarCaracteres(entrada)
    # Imprime uma mensagem formatada no console informando o número de caracteres na entrada fornecida pelo usuário
    print(f'A string {entrada}, tem {caracteres} caracteres')

# Se ocorrer um erro ao tentar executar o bloco de código acima (por exemplo, se o usuário digitar um número em vez de uma string),
# o bloco de código a seguir será executado
except:
    # Imprime uma mensagem de erro no console
    print('Erro, digite uma palavra ou frase')