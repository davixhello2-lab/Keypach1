import customtkinter as ctk
from tkinter import simpledialog as spc
import json
from datetime import datetime
import time

app = ctk.CTk()

app.geometry("400x400")
app.title("test kaypach")
tempo_inicial = time.time()

nome = spc.askstring(title="dijite seu nome", prompt="Digite seu nome")

def Keypach():
    # Mudámos o nome da variável para 'hora_atual' para não dar conflito com a biblioteca 'time'
    hora_atual = datetime.now().strftime("%H:%M:%S")

    global tempo_total
    tempo_total = time.time() - tempo_inicial
    
    # Verifica se é Bot ou Humano e define o resultado/ícone
    if tempo_total < 5:
        resultado = "Bot"
        icone = "❌"
    else:
        resultado = "Humano"
        icone = "✔"

    # Atualiza o botão com o ícone correspondente em vez de o destruir imediatamente
    Keypach_Button.configure(text=icone)

    dados = {
        "name": nome, 
        "tempo_click": hora_atual,
        "tempo_total_click": round(tempo_total, 2), # Arredondado para 2 casas decimais
        "verificacao": resultado
    }

    # Guarda os dados no ficheiro JSON
    with open(f"{nome}.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)

    # Opcional: Fecha a janela após 1.5 segundos para o utilizador conseguir ver o ícone mudar
    app.after(1500, app.destroy)

Keypach_Button = ctk.CTkButton(
    master=app, 
    command=Keypach, 
    text="✨", 
    corner_radius=15, 
    height=50, 
    width=50
)
Keypach_Button.place(x=175, y=175) # Ajustado ligeiramente para ficar mais centrado (janela é 400x400)

app.mainloop()
