import customtkinter as ctk
import json
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

apartamentos = []

def calcular_preco_por_metro(preco, area):
    return preco / area


def exibir_recomendacao():
    if not apartamentos:
        resultado_label.configure(text="Nenhum apartamento cadastrado.")
        return

    melhor_apto = None
    melhor_preco_por_metro = float('inf')

    for apto in apartamentos:
        preco_por_metro = calcular_preco_por_metro(apto['preco'], apto['area'])
        if preco_por_metro < melhor_preco_por_metro:
            melhor_preco_por_metro = preco_por_metro
            melhor_apto = apto

    resultado = (
        f"Recomendação de Apartamento:\n"
        f"Localização: {melhor_apto['localizacao']}\n"
        f"Número de Quartos: {melhor_apto['quartos']}\n"
        f"Área: {melhor_apto['area']} m²\n"
        f"Preço Total: R$ {melhor_apto['preco']}\n"
        f"Preço por Metro Quadrado: R$ {melhor_preco_por_metro:.2f}"
    )
    resultado_label.configure(text=resultado)


def adicionar_apartamento(editing_index=None):
    try:
        localizacao = localizacao_entry.get()
        quartos = int(quartos_entry.get())
        area = float(area_entry.get())
        preco = float(preco_entry.get())

        if area <= 0 or preco <= 0:
            raise ValueError("Área e preço devem ser maiores que zero.")

        apartamento = {
            'localizacao': localizacao,
            'quartos': quartos,
            'area': area,
            'preco': preco
        }

        if editing_index is None:
            apartamentos.append(apartamento)
        else:
            apartamentos[editing_index] = apartamento

        atualizar_lista_apartamentos()
        limpar_campos()
        resultado_label.configure(text="Apartamento salvo com sucesso!")
    except ValueError as e:
        resultado_label.configure(text=f"Erro: {e}")


def carregar_apartamentos():
    try:
        with open("apartamentos.json", "r") as file:
            global apartamentos
            apartamentos = json.load(file)
            atualizar_lista_apartamentos()
            resultado_label.configure(text="Dados carregados com sucesso!")
    except FileNotFoundError:
        resultado_label.configure(text="Nenhum arquivo encontrado para carregar.")
    except json.JSONDecodeError:
        resultado_label.configure(text="Erro ao carregar dados: arquivo inválido.")


def salvar_apartamentos():
    with open("apartamentos.json", "w") as file:
        json.dump(apartamentos, file, indent=4)
    resultado_label.configure(text="Dados salvos com sucesso!")

def excluir_apartamento(index):
    del apartamentos[index]
    atualizar_lista_apartamentos()
    resultado_label.configure(text="Apartamento excluído.")


def editar_apartamento(index):
    apto = apartamentos[index]
    localizacao_entry.delete(0, ctk.END)
    localizacao_entry.insert(0, apto['localizacao'])
    quartos_entry.delete(0, ctk.END)
    quartos_entry.insert(0, apto['quartos'])
    area_entry.delete(0, ctk.END)
    area_entry.insert(0, apto['area'])
    preco_entry.delete(0, ctk.END)
    preco_entry.insert(0, apto['preco'])

    adicionar_button.configure(text="Salvar Alteração", command=lambda: adicionar_apartamento(index))

# Função para atualizar lista de apartamentos na interface
def atualizar_lista_apartamentos():
    for widget in frame_lista_apartamentos.winfo_children():
        widget.destroy()

    for i, apto in enumerate(apartamentos):
        apartamento_button = ctk.CTkButton(
            frame_lista_apartamentos,
            text=f"{apto['localizacao']} - R$ {apto['preco']}",
            command=lambda i=i: editar_apartamento(i),
            width=200
        )
        apartamento_button.grid(row=i, column=0, padx=5, pady=5, sticky="w")

        excluir_button = ctk.CTkButton(
            frame_lista_apartamentos,
            text="Excluir",
            command=lambda i=i: excluir_apartamento(i),
            width=50
        )
        excluir_button.grid(row=i, column=1, padx=5, pady=5, sticky="e")


def limpar_campos():
    localizacao_entry.delete(0, ctk.END)
    quartos_entry.delete(0, ctk.END)
    area_entry.delete(0, ctk.END)
    preco_entry.delete(0, ctk.END)
    adicionar_button.configure(text="Adicionar Apartamento", command=adicionar_apartamento)

def exibir_grafico():
    if not apartamentos:
        resultado_label.configure(text="Nenhum apartamento cadastrado.")
        return

    apartamentos_sorted = sorted(apartamentos, key=lambda x: x['preco'], reverse=True)
    locais = [apto['localizacao'] for apto in apartamentos_sorted]
    precos = [apto['preco'] for apto in apartamentos_sorted]
    precos_por_metro = [calcular_preco_por_metro(apto['preco'], apto['area']) for apto in apartamentos_sorted]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    ax1.bar(locais, precos, color="skyblue")
    ax1.set_title("Preços dos Apartamentos", fontsize=14)
    ax1.set_xlabel("Localização", fontsize=12)
    ax1.set_ylabel("Preço (R$)", fontsize=12)
    ax1.tick_params(axis='x', rotation=45, labelsize=10)
    ax1.grid(True, linestyle='--', alpha=0.7)

    ax2.bar(locais, precos_por_metro, color="lightgreen")
    ax2.set_title("Preço por Metro Quadrado", fontsize=14)
    ax2.set_xlabel("Localização", fontsize=12)
    ax2.set_ylabel("R$/m²", fontsize=12)
    ax2.tick_params(axis='x', rotation=45, labelsize=10)
    ax2.grid(True, linestyle='--', alpha=0.7)

    fig.tight_layout()

    for widget in frame_grafico.winfo_children():
        widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

app = ctk.CTk()
app.title("Sistema de Comparação de Preços de Imóveis")
app.geometry("1650x600")

botao_frame = ctk.CTkFrame(app)
botao_frame.grid(row=0, column=0, sticky="ns", padx=10, pady=10)

conteudo_frame = ctk.CTkFrame(app)
conteudo_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

frame_grafico = ctk.CTkFrame(app)
frame_grafico.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

adicionar_button = ctk.CTkButton(botao_frame, text="Adicionar Imóveis", command=adicionar_apartamento)
adicionar_button.pack(pady=5)

recomendacao_button = ctk.CTkButton(botao_frame, text="Exibir Recomendação", command=exibir_recomendacao)
recomendacao_button.pack(pady=5)

carregar_button = ctk.CTkButton(botao_frame, text="Carregar Imóveis", command=carregar_apartamentos)
carregar_button.pack(pady=5)

salvar_button = ctk.CTkButton(botao_frame, text="Salvar Imóveis	", command=salvar_apartamentos)
salvar_button.pack(pady=5)

grafico_button = ctk.CTkButton(botao_frame, text="Exibir Grafico", command=exibir_grafico)
grafico_button.pack(pady=5)

frame_lista_apartamentos = ctk.CTkFrame(conteudo_frame)
frame_lista_apartamentos.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

entrada_frame = ctk.CTkFrame(conteudo_frame)
entrada_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

localizacao_label = ctk.CTkLabel(entrada_frame, text="Localizacao:")
localizacao_label.pack()
localizacao_entry = ctk.CTkEntry(entrada_frame)
localizacao_entry.pack(pady=3)

quartos_label = ctk.CTkLabel(entrada_frame, text="Numero de Quartos:")
quartos_label.pack()
quartos_entry = ctk.CTkEntry(entrada_frame)
quartos_entry.pack(pady=3)

area_label = ctk.CTkLabel(entrada_frame, text="Area (m²):")
area_label.pack()
area_entry = ctk.CTkEntry(entrada_frame)
area_entry.pack(pady=3)

preco_label = ctk.CTkLabel(entrada_frame, text="Preco Total (R$):")
preco_label.pack()
preco_entry = ctk.CTkEntry(entrada_frame)
preco_entry.pack(pady=3)

resultado_label = ctk.CTkLabel(conteudo_frame, text="Recomendacao")
resultado_label.grid(row=2, column=0, pady=10)

app.mainloop()
