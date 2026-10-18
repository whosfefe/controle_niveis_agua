# 💧 Controle de Níveis de Água

## 📌 Sobre o projeto

Este projeto consiste em um sistema simples de monitoramento de um reservatório de água, desenvolvido em Python. O programa simula o nível atual do reservatório e exibe uma mensagem de alerta colorida no terminal, de acordo com a situação identificada.

Para melhorar a visualização das mensagens, foi utilizada a biblioteca **Colorama**, que permite aplicar cores ao texto exibido no terminal.

## 🎯 Objetivo

Praticar conceitos fundamentais de programação em Python, como:

- Listas;
- Funções;
- Estruturas condicionais (`if`, `elif` e `else`);
- Estruturas de repetição e validação;
- Importação e utilização de bibliotecas;
- Exibição de mensagens coloridas no terminal.

## 🎨 Níveis do reservatório

| Nível | Situação | Cor |
|---|---|---|
| 1 | Muito baixo (crítico) | 🔴 Vermelho |
| 2 | Baixo | 🟡 Amarelo |
| 3 | Médio | 🟢 Verde |
| 4 | Alto | 🩵 Ciano |
| 5 | Muito alto (alerta) | 🔵 Azul |

## 🧪 Funcionamento

O programa utiliza uma lista para armazenar as situações do reservatório e uma função para definir a cor correspondente ao nível informado.

O nível atual é definido diretamente no código, sem a necessidade de entrada de dados pelo usuário. Em seguida, o sistema verifica se o nível é válido e exibe a mensagem correspondente com a cor apropriada.

Após a exibição, o estilo do terminal é restaurado para o padrão.
