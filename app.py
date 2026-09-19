# Programa Alerta de Consumo de Água
# Autora: Mojarri Macena

# ===== Entrada de dados =====
# Aqui o programa pede ao usuário que digite o tipo de imóvel.
# O valor digitado será usado para decidir se é necessário informar o consumo.
tipo_imovel = input("Digite o tipo de imóvel (comercial, casa ou apartamento): ")

# ===== Processamento =====
# Usamos o comando match para organizar as decisões.
# Cada case representa uma possibilidade de tipo de imóvel.
# O símbolo | significa "ou", permitindo aceitar variações de escrita.
match tipo_imovel:
    # Caso seja comercial, não pedimos consumo de água.
    case "comercial" | "Comercial":
        mensagem = "Tarifa comercial aplicada - consulte o plano corporativo."

    # Caso seja apartamento, pedimos o consumo e aplicamos as regras.
    case "apartamento" | "Apartamento":
        # O valor digitado é convertido para float (número decimal).
        consumo_agua = float(input("Digite o consumo mensal de água em metros cúbicos: "))

        # Se o consumo for menor que 10 m³ → consumo econômico.
        if consumo_agua < 10:
            mensagem = "Consumo econômico - excelente controle de água!"
        # Se o consumo for até 25 m³ → consumo moderado.
        elif consumo_agua <= 25:
            mensagem = "Consumo moderado - dentro do padrão residencial."
        # Se passar de 25 m³ → consumo excessivo.
        else:
            mensagem = "Consumo excessivo - adote medidas de economia e verifique vazamentos."

    # Caso seja casa, também pedimos o consumo e aplicamos as regras.
    case "casa" | "Casa":
        consumo_agua = float(input("Digite o consumo mensal de água em metros cúbicos: "))

        # Se o consumo for até 25 m³ → consumo moderado.
        if consumo_agua <= 25:
            mensagem = "Consumo moderado - dentro do padrão residencial."
        # Se passar de 25 m³ → consumo excessivo.
        else:
            mensagem = "Consumo excessivo - adote medidas de economia e verifique vazamentos."

    # Qualquer outra entrada é inválida.
    case _:
        mensagem = "Opção inválida! Escolha apenas entre comercial, casa ou apartamento."

# ===== Saída =====
# Aqui o programa mostra a mensagem final escolhida no processamento.
print(mensagem)