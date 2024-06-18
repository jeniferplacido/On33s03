# Define uma função chamada 'celsius_para_fahrenheit' que recebe um argumento: 'celsius'
def celsius_para_fahrenheit(celsius):
    # A função retorna a conversão da temperatura de graus Celsius para Fahrenheit
    return celsius * 9 / 5 + 32

# Solicita ao usuário que digite a temperatura em graus Celsius e armazena a entrada do usuário na variável 'entrada'
entrada = input('Digite a temperatura em graus Celsius: ')

# Tenta executar o bloco de código a seguir
try:
    # Converte a entrada do usuário para um número flutuante e armazena na variável 'celsius'
    celsius = float(entrada)
    # Chama a função 'celsius_para_fahrenheit' com a temperatura fornecida pelo usuário e armazena o resultado na variável 'fahrenheit'
    fahrenheit = celsius_para_fahrenheit(celsius)
    # Imprime uma mensagem formatada no console informando a conversão da temperatura de Celsius para Fahrenheit
    print(f'A temperatura de {celsius}°C corresponde a {fahrenheit}°F')

# Se ocorrer um erro ao tentar executar o bloco de código acima (por exemplo, se o usuário digitar uma string em vez de um número),
# o bloco de código a seguir será executado
except:
    # Imprime uma mensagem de erro no console
    print('Erro, digite um numero valido')