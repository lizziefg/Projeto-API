import requests
import json

# URL base da API que está rodando localmente
BASE_URL = "http://127.0.0.1:8000"


def exibir_resposta(response):
    try:
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    except json.JSONDecodeError:
        print(f"Erro ao decodificar a resposta: {response.text}")

def listar_todos_os_processos():
    print("\n--- Listando todos os processos ---")
    try:
        response = requests.get(f"{BASE_URL}/processos/")
        if response.status_code == 200:
            print("Processos encontrados:")
            exibir_resposta(response)
        else:
            print(f"Erro ao buscar processos: {response.status_code}")
    except requests.exceptions.ConnectionError as e:
        print(f"Não foi possível conectar ao servidor: {e}")

def criar_novo_processo():
    print("\n--- Cadastro de Novo Processo ---")
    try:
        numero = input("Número do processo: ")
        autor = input("Nome do autor: ")
        reu = input("Nome do réu: ")
        status = input("Status inicial: ")
    except EOFError:
        print("\nEntrada cancelada")
        return
    
    novo_processo = {
        "numero": numero,
        "autor": autor,
        "reu": reu,
        "status": status
    }

    try:
        response = requests.post(f"{BASE_URL}/processos/", json=novo_processo)
        if response.status_code == 201:
            print("\nProcesso criado com sucesso!")
            exibir_resposta(response)
        else:
            print(f"\nErro ao criar processo: {response.status_code}")
            exibir_resposta(response)
    except requests.exceptions.ConnectionError as e:
        print(f"Não foi possível conectar ao servidor: {e}")

def buscar_processo_por_numero():
    print("\n--- Buscar Processo por Número ---")
    try:
        numero = input("Digite o número do processo que deseja buscar: ")
        if not numero:
            print("Busca cancelada.")
            return
        
        response = requests.get(f"{BASE_URL}/processos/{numero}")

        if response.status_code == 200:
            print("Processo encontrado: ")
            exibir_resposta(response)
        elif response.status_code == 404:
            print("Erro: Processo não encontrado.")
            exibir_resposta(response)
        else:
            print(f"Erro ao buscar processo: {response.status_code}")
            exibir_resposta(response)
    
    except requests.exceptions.ConnectionError as e:
        print(f"Não foi possível conectar ao servidor: {e}")
    except EOFError:
        print("\nBusca cancelada.")

def deletar_processo():
    print("\n--- Deletar Processo ---")
    try:
        numero = input("Digite o número do processo que deseja deletar: ")
        if not numero:
            print("Deleção cancelada.")
            return
    
        response = requests.delete(f"{BASE_URL}/processos/{numero}")

        if response.status_code == 204:
            print(f"Processo '{numero}' deletado com sucesso!")
        elif response.status_code == 404:
            print("Erro: Processo não encontrado.")
            exibir_resposta(response)
        else:
            print(f"Erro ao deletar processo: {response.status_code}")
            exibir_resposta(response)
    
    except requests.exceptions.ConnectionError as e:
        print(f"Não foi possível concectar ao servidor: {e}")
    except EOFError:
        print("\nDeleção cancelada.")

def menu_principal():
    while True:
        print("\n=== Processo Judicial Eletrônico ===")
        print("1. Criar novo processo")
        print("2. Listar todos os processos")
        print("3. Buscar processo por número")
        print("4. Deletar processo")
        print("0. Sair")
        
        try:
            escolha = input("\nDigite sua escolha: ") 
            if escolha == '1':
                criar_novo_processo()
            elif escolha == '2':
                listar_todos_os_processos()
            elif escolha == '3':
                buscar_processo_por_numero()
            elif escolha == '4':
                deletar_processo()
            elif escolha == '0':
                print("Encerrando sistema.")
                break
            else:
                print("Opção inválida. Por favor, tente novamente.")
        
        except EOFError:
            print("\nSaída forçada.")
            break
        except KeyboardInterrupt:
            print("\nSaída forçada.")
            break

# --- Menu Principal do Cliente ---
if __name__ == "__main__":
    menu_principal()