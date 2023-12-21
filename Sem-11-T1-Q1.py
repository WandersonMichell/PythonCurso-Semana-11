# Função para calcular quantos anos são necessários para o valor acumulado dobrar em relação ao depósito inicial
def calcula_anos_duplo_valor_inicial(deposito_inicial, taxa_de_juros):
    anos = 0
    valor_acumulado = deposito_inicial

    # Loop enquanto o valor acumulado for menor que o dobro do depósito inicial
    while valor_acumulado < 2 * deposito_inicial:
        # Atualiza o valor acumulado com base na taxa de juros
        valor_acumulado += valor_acumulado * (taxa_de_juros / 100)
        anos += 1  # Incrementa o contador de anos

    return anos

def main():
    # Solicita ao usuário que insira o depósito inicial e a taxa de juros
    deposito_inicial = float(input("Insira o valor do depósito inicial: ").strip())
    taxa_de_juros = float(input("Insira a taxa de juros (em porcentagem): ").strip())

    # Chama a função para calcular os anos necessários para dobrar o valor inicial
    anos_para_dobrar = calcula_anos_duplo_valor_inicial(deposito_inicial, taxa_de_juros)

    # Exibe o resultado
    print(f"São necessários {anos_para_dobrar} anos para o valor dobrar.")

# Verifica se o programa está sendo executado como script principal
if __name__ == "__main__":
    main()
