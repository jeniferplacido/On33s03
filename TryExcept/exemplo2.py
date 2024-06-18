try:
    # Define duas variáveis 'numero1' e 'numero2' e atribui os valores 10 e 0 a elas, respectivamente
    numero1 = 10
    numero2 = 0
    # Tenta dividir 'numero1' por 'numero2' e armazena o resultado na variável 'resultado'
    resultado = numero1 / numero2
    # Imprime uma mensagem formatada no console informando o resultado da divisão
    print("O resultado é: ", resultado)
# Se ocorrer um erro ao tentar executar o bloco de código acima (por exemplo, se 'numero2' for 0, o que causará um erro de divisão por zero),
# o bloco de código a seguir será executado
except:
    # Imprime uma mensagem de erro no console
    print("Segundo número não pode ser zero")
# Se não ocorrer nenhum erro ao tentar executar o bloco de código no 'try', o bloco de código a seguir será executado
else:
    # Imprime uma mensagem no console informando que a divisão foi realizada com sucesso
    print("Divisao realizada com sucesso")
# Independentemente de um erro ocorrer ou não ao tentar executar o bloco de código no 'try', o bloco de código a seguir será sempre executado
finally:
    # Imprime uma mensagem no console informando o fim da divisão
    print("Fim da divisão")