# Crie uma função converter_temp que:
# Receba a temperatura em Celsius como parâmetro
# Retorne a temperatura em Fahrenheit

# (Fórmula: F = C * 1.8 + 32)

def converter_temp(celsius):
  f = celsius * 1.8 + 32
  return f

print(converter_temp(25))  # Exemplo de uso da função