import tkinter as tk
from datetime import datetime, timedelta

def calcular_uso_proporcional():
    try:
        valor_plano = float(entry_valor_plano.get())
        data_vencimento = datetime.strptime(entry_data_vencimento.get(), "%d/%m/%Y")
        data_ultima_conexao = datetime.strptime(entry_data_ultima_conexao.get(), "%d/%m/%Y")

        dias_utilizados = (data_ultima_conexao - data_vencimento).days
        dias_tolerancia = 10
        dias_utilizados = min(dias_utilizados, dias_tolerancia)

        valor_por_dia = valor_plano / 30
        valor_proporcional = valor_por_dia * dias_utilizados

        valor_total_boleto = valor_plano + valor_proporcional

        label_resultado.config(text=f"Valor proporcional: R$ {valor_proporcional:.2f} "
                                    f"({dias_utilizados} dias)\n"
                                    f"Valor total do boleto: R$ {valor_total_boleto:.2f}")
    except ValueError as e:
        label_resultado.config(text=str(e))
    except Exception:
        label_resultado.config(text="Por favor, insira valores válidos.")

# Configuração da interface
root = tk.Tk()
root.title("Calc. Consumo :) ")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label_valor_plano = tk.Label(frame, text="Valor do plano:")
label_valor_plano.grid(row=0, column=0)

entry_valor_plano = tk.Entry(frame)
entry_valor_plano.grid(row=0, column=1)

label_data_vencimento = tk.Label(frame, text="Data de vencimento (DD/MM/AAAA):")
label_data_vencimento.grid(row=1, column=0)

entry_data_vencimento = tk.Entry(frame)
entry_data_vencimento.grid(row=1, column=1)

label_data_ultima_conexao = tk.Label(frame, text="Data da última conexão (DD/MM/AAAA):")
label_data_ultima_conexao.grid(row=2, column=0)

entry_data_ultima_conexao = tk.Entry(frame)
entry_data_ultima_conexao.grid(row=2, column=1)

button_calcular = tk.Button(frame, text="Calcular", command=calcular_uso_proporcional)
button_calcular.grid(row=3, columnspan=2)

label_resultado = tk.Label(frame, text="")
label_resultado.grid(row=4, columnspan=2)

root.mainloop()
