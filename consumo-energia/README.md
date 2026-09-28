# ⚡ Sistema de Cálculo do Consumo de Energia

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Interface-Tkinter-2C5E1A?style=for-the-badge)
![Sustentabilidade](https://img.shields.io/badge/Energia-Sustentável-00A86B?style=for-the-badge)

## 🎯 Objetivo do sistema

O **Sistema de Cálculo do Consumo de Energia** estima o consumo mensal de um aparelho elétrico a partir de sua potência e do tempo médio de uso diário.

O usuário informa:

- Nome do aparelho (ex.: Geladeira).
- Potência do aparelho em watts (W).
- Tempo médio de uso diário em horas.

Ao clicar em **Calcular consumo**, o sistema apresenta o consumo mensal estimado em quilowatt-hora (kWh), considerando um mês de 30 dias.

## 🛠️ Tecnologias utilizadas

- **Python 3**: linguagem utilizada para desenvolver o programa.
- **Tkinter e ttk**: bibliotecas usadas para criar a interface gráfica.
- **math**: biblioteca utilizada na validação dos valores numéricos.

## ▶️ Como executar

### 1. Verifique se o Python está instalado

No terminal, execute:

```bash
python3 --version
```

O ambiente Python também deve ter o Tkinter disponível e acesso a uma tela gráfica.

### 2. Execute o programa

Abra o terminal na pasta `projetos/consumo-energia`, onde está o arquivo `app.py`, e execute:

```bash
python3 app.py
```

### 3. Calcule o consumo

Preencha os campos e clique em **Calcular consumo** ou pressione **Enter**.

## 📋 Regras de cálculo

O consumo mensal é calculado pela fórmula:

```python
consumoMensal = (potencia * horasDia * 30) / 1000
```

| Informação | Descrição |
|---|---|
| `potencia` | Potência do aparelho em watts (W) |
| `horasDia` | Tempo médio de uso diário em horas |
| `30` | Quantidade de dias considerada no mês |
| `1000` | Fator de conversão de Wh para kWh |
| `consumoMensal` | Consumo mensal estimado em kWh |

### Exemplo de cálculo

| Aparelho | Potência | Uso diário | Consumo mensal estimado |
|---|---:|---:|---:|
| Televisor | 150 W | 8 horas | 36,00 kWh |

```text
Consumo mensal = (150 × 8 × 30) / 1000 = 36 kWh
```

## ✅ Validação dos dados

- O nome do aparelho deve ser preenchido.
- A potência deve ser um número finito maior que zero.
- O tempo de uso diário deve estar entre 0 e 24 horas.
- Os campos numéricos aceitam vírgula ou ponto como separador decimal.
- Caso os dados sejam inválidos, o programa apresenta uma mensagem de erro.

## 🌱 Sustentabilidade

O projeto incentiva o uso consciente da energia elétrica, ajudando o usuário a compreender como a potência dos aparelhos e o tempo de uso influenciam o consumo mensal.

O resultado é uma estimativa que considera a potência informada constante durante as horas de uso. O consumo real pode variar, especialmente em aparelhos que ligam e desligam automaticamente, como geladeiras.

## 👤 Autor

Desenvolvido por **Derick Prado**.
