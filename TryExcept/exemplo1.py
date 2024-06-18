# Tenta executar o bloco de código a seguir
try:
    # Define uma variável 'numero' e atribui o valor 10 a ela
    numero = 10
    # Define uma variável 'segundoNumero' e atribui o valor 0 a ela
    segundoNumero = 0
    # Tenta dividir 'numero' por 'segundoNumero' e armazena o resultado na variável 'resultado'
    resultado = numero / segundoNumero
    # Imprime uma mensagem formatada no console informando o resultado da divisão
    print(f"O resultado é {resultado}")
# Se ocorrer um erro ao tentar executar o bloco de código acima (por exemplo, se 'segundoNumero' for 0, o que causará um erro de divisão por zero),
# o bloco de código a seguir será executado
except:
    # Imprime uma mensagem de erro no console
    print("Segundo número não pode ser zero")