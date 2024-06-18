# Define a função soma que recebe dois parâmetros: a e b
def soma(a, b):
    # A variável resultado recebe a soma de a e b
    resultado =  a + b
    # A função retorna o valor de resultado
    return resultado

# Define a variável x com o valor 10
x = 10
# Define a variável y com o valor 5
y = 5
# A variável z recebe o valor retornado pela função soma quando passamos x e y como argumentos
z = soma(x, y)
# Imprime no console o valor de z formatado em uma string
print(f'O resultado é {z}')