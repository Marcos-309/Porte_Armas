import mysql.connector
import os

# Função para limpar o console
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para conectar ao banco de dados MySQL
def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Substitua pelo seu usuário MySQL
        password="Marcos_309",  # Substitua pela sua senha MySQL
        database="porte_arma"
    )

# Função para listar os países disponíveis
def listar_paises():
    db = conectar_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM pais")
    paises = cursor.fetchall()
    db.close()

    cls()  # Limpar tela
    print("Escolha um país para homologação do porte de arma:")
    for i, pais in enumerate(paises):
        print(f"{i + 1}. {pais[1]}")
    
    return paises

# Função para verificar requisitos de porte de arma de um país
def verificar_requisitos(pais_id):
    db = conectar_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM requisitos WHERE pais_id = %s", (pais_id,))
    requisito = cursor.fetchone()
    db.close()
    return requisito

# Função para verificar se o usuário tem idade mínima para obter porte de arma
def verificar_idade(idade, idade_minima):
    if idade >= idade_minima:
        return True
    return False

# Função principal do programa
def main():
    cls()  # Limpar tela
    
    # Parte 1: Perguntar se o usuário tem porte de arma
    tem_porte = input("Você tem porte de arma? (sim/não): ").strip().lower()

    if tem_porte == "sim":
        # Perguntar de qual país o usuário tem o porte
        paises = listar_paises()
        pais_origem = input("\nDe qual país você tem o porte de armas? ").strip()

        # Perguntar para qual país deseja homologar
        pais_destino = input("Para qual país você deseja homologar o porte de armas? ").strip()

        # Buscar IDs dos países
        pais_origem_id = next((pais[0] for pais in paises if pais[1].lower() == pais_origem.lower()), None)
        pais_destino_id = next((pais[0] for pais in paises if pais[1].lower() == pais_destino.lower()), None)

        # Verificar requisitos do país de destino
        if pais_destino_id:
            requisito_destino = verificar_requisitos(pais_destino_id)
            if requisito_destino:
                print(f"\nRequisitos para homologação do porte de arma em {pais_destino}:")
                print(f"Idade mínima: {requisito_destino[2]} anos")
                print(f"Documentos necessários: {requisito_destino[3]}")
            else:
                print(f"\nNão foram encontrados requisitos para o país {pais_destino}.")
        else:
            print(f"\nPaís {pais_destino} não encontrado.")
    
    elif tem_porte == "não":
        # Parte 2: Se o usuário não tem porte, perguntar se é cidadão de algum país
        cls()
        cidadania = input("Você é cidadão de algum dos países que permitem porte de arma? (sim/não): ").strip().lower()

        if cidadania == "sim":
            paises = listar_paises()
            pais_cidadania = input("\nDe qual país você é cidadão? ").strip()
            idade = int(input("Qual sua idade? "))
            
            pais_cidadania_id = next((pais[0] for pais in paises if pais[1].lower() == pais_cidadania.lower()), None)

            if pais_cidadania_id:
                requisito_cidadania = verificar_requisitos(pais_cidadania_id)
                if requisito_cidadania and verificar_idade(idade, requisito_cidadania[2]):
                    print(f"\nVocê pode obter porte de arma no seu país de origem ({pais_cidadania}).")
                    
                    #TESTE TEST Perguntar para qual país deseja homologar o porte
                    pais_destino = input("Para qual país você deseja homologar o porte de armas? ").strip()
                    pais_destino_id = next((pais[0] for pais in paises if pais[1].lower() == pais_destino.lower()), None)

                    if pais_destino_id:
                        requisito_destino = verificar_requisitos(pais_destino_id)
                        if requisito_destino:
                            print(f"\nRequisitos para homologação do porte de arma em {pais_destino}:")
                            print(f"Idade mínima: {requisito_destino[2]} anos")
                            print(f"Documentos necessários: {requisito_destino[3]}")
                        else:
                            print(f"\nNão foram encontrados requisitos para o país {pais_destino}.")
                    else:
                        print(f"\nPaís {pais_destino} não encontrado.")
                else:
                    print("Você não tem a idade mínima para obter porte de arma neste país.")
            else:
                print(f"\nPaís {pais_cidadania} não encontrado.")
        else:
            print("\nVocê não pode obter porte de arma se não for cidadão de um país que permita.")

if __name__ == "__main__":
    main()
