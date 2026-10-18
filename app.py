
from colorama import Fore, Style, init

# Inicializa a biblioteca Colorama
init(autoreset=True)

# Lista com os níveis e suas situações
niveis = [
    "Nível 1 - Muito baixo (crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (alerta)"
]

# Função que define a cor de cada nível
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED       # Vermelho
    elif nivel == 2:
        return Fore.YELLOW    # Amarelo
    elif nivel == 3:
        return Fore.GREEN     # Verde
    elif nivel == 4:
        return Fore.CYAN      # Ciano
    elif nivel == 5:
        return Fore.BLUE      # Azul
    else:
        return Fore.WHITE     # Branco

# Simulação dos níveis do reservatório
for i in range(1, 6):
    cor = definir_cor(i)
    mensagem = niveis[i - 1]

    print(cor + mensagem + Style.RESET_ALL)
