import tkinter as tk
from datetime import datetime

def calcular_valor_boleto():
    try:
        valor_plano = float(entry_valor_plano.get())
        data_base = datetime.strptime(entry_data_base.get(), "%d/%m/%Y")
        data_vencimento = datetime.strptime(entry_data_vencimento.get(), "%d/%m/%Y")
        data_analise = datetime.now()

        dias_utilizados = (data_vencimento - data_base).days 
        valor_por_dia = valor_plano / 30

        valor_proporcional = valor_por_dia * dias_utilizados
        valor_total_boleto = valor_proporcional

        # Cálculo dos juros e multa após o vencimento, caso seja selecionado
        dias_atraso = (data_analise - data_vencimento).days 
        dias_atraso = dias_atraso if dias_atraso >= 0 else 0
        
        if check_var_juros.get() and data_vencimento < data_analise:
            juros_diarios = 0.03  # R$ 0,03 ao dia de atraso
            valor_juros = (juros_diarios * dias_atraso)
            multa_mensal = 0.02  # 2% do valor do plano ao mês de atraso
            valor_multa = (multa_mensal * valor_plano)
            valor_total_boleto += valor_juros + valor_multa

        label_resultado.config(text=f"Dias utilizados: {dias_utilizados}\n"
                                  f"Dias em atraso: {dias_atraso} \n"
                                  f"Valor total do boleto: R$ {valor_total_boleto:.2f}\n")
    except ValueError as e:
        label_resultado.config(text=str(e))
    except Exception:
        label_resultado.config(text="Por favor, insira valores válidos.")

# Configuração da interface
root = tk.Tk()
root.title("Calculadora Boleto (Ragtek - ©️ G.O)")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

label_valor_plano = tk.Label(frame, text="Valor do plano:")
label_valor_plano.grid(row=0, column=0)

entry_valor_plano = tk.Entry(frame)
entry_valor_plano.grid(row=0, column=1)

label_data_base = tk.Label(frame, text="Data base (DD/MM/AAAA):")
label_data_base.grid(row=1, column=0)

entry_data_base = tk.Entry(frame)
entry_data_base.grid(row=1, column=1)

label_data_vencimento = tk.Label(frame, text="Data de vencimento (DD/MM/AAAA):")
label_data_vencimento.grid(row=2, column=0)

entry_data_vencimento = tk.Entry(frame)
entry_data_vencimento.grid(row=2, column=1)

check_var_juros = tk.IntVar()
check_juros = tk.Checkbutton(frame, text="Incluir juros após o vencimento", variable=check_var_juros)
check_juros.grid(row=3, columnspan=2)

button_calcular = tk.Button(frame, text="Calcular", command=calcular_valor_boleto)
button_calcular.grid(row=4, columnspan=2)

label_resultado = tk.Label(frame, text="", font=("Arial", 14, "bold"))
label_resultado.grid(row=5, columnspan=2)

root.mainloop()
