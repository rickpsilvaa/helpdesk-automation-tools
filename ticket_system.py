import datetime
import os

CAMINHO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chamados.txt")

chamados = []

def registrar_chamado():
    print("\n===== Novo Chamado =====")
    usuario = input("Nome do usuário: ")
    problema = input("Descrição do problema: ")

    print("\nPrioridade:")
    print("1. Alta")
    print("2. Média")
    print("3. Baixa")
    prioridade_opcao = input("Escolha (1/2/3): ")

    prioridades = {"1": "Alta", "2": "Média", "3": "Baixa"}
    prioridade = prioridades.get(prioridade_opcao, "Média")

    categorias = {
        "1": "Acesso e Autenticação",
        "2": "Hardware/Dispositivo",
        "3": "Conectividade",
        "4": "Software/Aplicativo",
        "5": "Outro"
    }

    print("\nCategoria:")
    for k, v in categorias.items():
        print(f"{k}. {v}")
    cat_opcao = input("Escolha (1-5): ")
    categoria = categorias.get(cat_opcao, "Outro")

    agora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    chamado_id = f"TKT-{len(chamados)+1:03d}"

    chamado = {
        "id": chamado_id,
        "usuario": usuario,
        "problema": problema,
        "prioridade": prioridade,
        "categoria": categoria,
        "horario": agora,
        "status": "Aberto"
    }

    chamados.append(chamado)
    salvar_chamado(chamado)
    print(f"\n✅ Chamado {chamado_id} registrado com sucesso!")

def salvar_chamado(chamado):
    try:
        with open(CAMINHO, "a", encoding="utf-8") as f:
            f.write(f"\n[{chamado['horario']}] {chamado['id']} | "
                   f"Usuario: {chamado['usuario']} | "
                   f"Categoria: {chamado['categoria']} | "
                   f"Prioridade: {chamado['prioridade']} | "
                   f"Problema: {chamado['problema']} | "
                   f"Status: {chamado['status']}\n")
    except Exception as e:
        print(f"Erro ao salvar: {e}")

def gerar_relatorio():
    if not chamados:
        print("\nNenhum chamado registrado nessa sessao.")
        return

    print("\n========== RELATORIO DE CHAMADOS ==========")
    print(f"Total de chamados: {len(chamados)}")

    altas = [c for c in chamados if c['prioridade'] == 'Alta']
    medias = [c for c in chamados if c['prioridade'] == 'Média']
    baixas = [c for c in chamados if c['prioridade'] == 'Baixa']

    print(f"Alta prioridade:  {len(altas)}")
    print(f"Media prioridade: {len(medias)}")
    print(f"Baixa prioridade: {len(baixas)}")

    print("\n--- Chamados por Categoria ---")
    categorias_count = {}
    for c in chamados:
        cat = c['categoria']
        categorias_count[cat] = categorias_count.get(cat, 0) + 1
    for cat, count in categorias_count.items():
        print(f"{cat}: {count} chamado(s)")

    print("\n--- Lista de Chamados ---")
    for c in chamados:
        print(f"{c['id']} | {c['usuario']} | {c['prioridade']} | {c['status']}")
    print("===========================================")

def menu():
    print("\n===== Help Desk Ticket System =====")
    print("1. Registrar novo chamado")
    print("2. Gerar relatorio")
    print("3. Ver historico salvo")
    print("4. Sair")
    return input("\nEscolha uma opcao: ")

while True:
    opcao = menu()

    if opcao == "1":
        registrar_chamado()

    elif opcao == "2":
        gerar_relatorio()

    elif opcao == "3":
        print("\n📋 Historico de Chamados:\n")
        if os.path.exists(CAMINHO):
            with open(CAMINHO, "r", encoding="utf-8") as f:
                print(f.read())
        else:
            print("Nenhum historico encontrado.")

    elif opcao == "4":
        print("Encerrando sistema...")
        break
