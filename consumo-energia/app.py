import math
import tkinter as tk
from tkinter import messagebox, ttk


def criar_interface():
    janela = tk.Tk()
    janela.title("Consumo de energia")
    janela.resizable(False, False)

    painel = ttk.Frame(janela, padding=24)
    painel.grid()

    ttk.Label(painel, text="Consumo mensal de energia", font=("Arial", 16, "bold")).grid(
        row=0, column=0, sticky="w", pady=(0, 8)
    )
    ttk.Label(painel, text="Informe os dados do aparelho. O cálculo considera 30 dias.").grid(
        row=1, column=0, sticky="w", pady=(0, 16)
    )

    campos = []
    for indice, rotulo in enumerate([
        "Nome do aparelho",
        "Potência em watts (W)",
        "Tempo médio de uso diário em horas (0 a 24)",
    ]):
        ttk.Label(painel, text=rotulo).grid(row=2 + indice * 2, column=0, sticky="w")
        campo = ttk.Entry(painel, width=45)
        campo.grid(row=3 + indice * 2, column=0, sticky="ew", pady=(4, 12))
        campos.append(campo)

    resultado = tk.StringVar(value="Preencha os campos e clique em Calcular.")

    def calcular(event=None):
        resultado.set("Preencha os campos e clique em Calcular.")
        nome = campos[0].get().strip()
        if not nome:
            messagebox.showerror("Dados inválidos", "Informe o nome do aparelho.", parent=janela)
            campos[0].focus_set()
            return

        try:
            potencia = float(campos[1].get().strip().replace(",", "."))
            horasDia = float(campos[2].get().strip().replace(",", "."))
            if not math.isfinite(potencia) or potencia <= 0:
                raise ValueError
            if not math.isfinite(horasDia) or not 0 <= horasDia <= 24:
                raise ValueError
            consumoMensal = (potencia * horasDia * 30) / 1000
            if not math.isfinite(consumoMensal):
                raise ValueError
        except ValueError:
            messagebox.showerror(
                "Dados inválidos",
                "Informe uma potência positiva e um tempo de uso entre 0 e 24 horas.\n"
                "Você pode usar vírgula ou ponto nos números decimais.",
                parent=janela,
            )
            return

        consumo_formatado = f"{consumoMensal:.2f}".replace(".", ",")
        resultado.set(f"{nome}\nConsumo mensal: {consumo_formatado} kWh")

    ttk.Button(painel, text="Calcular consumo", command=calcular).grid(
        row=8, column=0, sticky="ew", pady=(4, 16)
    )
    ttk.Label(painel, textvariable=resultado, wraplength=400, font=("Arial", 12)).grid(
        row=9, column=0, sticky="w"
    )
    janela.bind("<Return>", calcular)
    campos[0].focus_set()
    return janela


if __name__ == "__main__":
    criar_interface().mainloop()
