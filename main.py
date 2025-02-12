import mysql.connector
import os
import time            
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
def exibir_requisitos(pais):
    db = conectar_db()
    cursor = db.cursor()
    cursor.execute(f"SELECT requisitos FROM Paises_Requisitos WHERE nome_pais = '{pais}'")
    paises = cursor.fetchone()

    if resultado:
        print(f"\nRequisitos para o porte de armas no {pais}: {resultado[0]}")
    else:
        print("\nPais não encontrado!")
        time.sleep(1)

    cursor.close()
    db.close()
    cls()  # Limpar tela
    
# Função para verificar requisitos de porte de arma de um país
def pedir_porte_de_arma():
    idade = int(input("\nDigite sua idade: "))
    
    if idade < 18:
        print("\nNão é possível efetuar pedido de porte de armas. Idade mínima para pedido são 18 anos.\n")
        time.sleep(1)
        return
    
    pais = input("Para qual país você deseja pedir o porte de armas? (Escolha entre os 20 países)\n").strip().lower()
    
    paises_validos = ['alemanha', 'argentina', 'brasil', 'colômbia', 'espanha', 'estados unidos', 
                      'frança', 'grécia', 'hungria', 'israel', 'itália', 'méxico', 'peru', 'polônia', 
                      'portugal', 'república tcheca', 'romênia', 'suécia', 'suíça', 'venezuela']
    
    if pais not in paises_validos:
        print("\nNão é um dos 20 países válidos. Insira um país válido.\n")
        return 
    
    pais = pais.title()  # Deixar o nome do país com as iniciais maiúsculas
    exibir_requisitos(pais)

# Função para homologar o porte de arma
def homologar_porte_de_arma():
    idade = int(input("\nDigite sua idade: "))
    
    if idade < 18:
        print("\nNão é possível efetuar pedido de homologação de porte de armas. Idade mínima para pedido são 18 anos.\n")
        time.sleep(1)
        return
    
    pais = input("Para qual país você deseja homologar o porte de armas? (Escolha entre os 20 países)\n").strip().lower()
    
    paises_validos = ['alemanha', 'argentina', 'brasil', 'colômbia', 'espanha', 'estados unidos', 
                      'frança', 'grécia', 'hungria', 'israel', 'itália', 'méxico', 'peru', 'polônia', 
                      'portugal', 'república tcheca', 'romênia', 'suécia', 'suíça', 'venezuela']
    
    if pais not in paises_validos:
        print("\nNão é um dos 20 países válidos. Insira um país válido.\n")
        time.sleep(1)
        return
    
    pais = pais.title()  # Deixar o nome do país com as iniciais maiúsculas
    exibir_requisitos(pais)

# Função principal do programa
def main():
    while True:
        cls()  # Limpar tela
        print("########################################")
        print("#                                      #")
        print("#     HOMOLOGAÇÃO DE PORTE DE ARMAS    #")
        print("#                                      #")
        print("# Escolha uma das opções;              #")
        print("# 1 - Pedir porte de Arma;             #")
        print("# 2 - Homologar porte de Arma;         #")
        print("# 3 - Sair;                            #")
        print("#                                      #")
        print("########################################")
        
        opcao = input("Escolha uma opção (1, 2, ou 3): ")
        
        if opcao == "1":
            pedir_porte_de_arma()
        elif opcao == "2":
            homologar_porte_de_arma()
        elif opcao == "3":
            print("\n Saindo do programa...\n")
            time.sleep(1)
            break
        else:
         print("\n Opção inválida! Tente novamente.\n")
         time.sleep(1)  # Pausa por 1 segundo
         
main()
