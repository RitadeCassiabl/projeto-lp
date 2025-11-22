import classes.menus.menu_farmaceutico as menu_farmaceutico
import classes.menus.menu_caixa as menu_caixa
from classes.menus.utils.limpar_terminal import limpar_terminal
class Menu:
    def exibir_menu(self):
        print("=== Entrar ===")
        
        nome_input = input("Digite seu nome de usuário: ").strip()
        senha_input = input("Digite sua senha: ").strip()
        
        login_sucesso = False 

        try:
            with open("database/usuarios.txt", "r") as arquivo:
                
                while True:
                    linha_nome = arquivo.readline().strip() 
                    
                    if not linha_nome:
                        break 
                        
                    linha_senha = arquivo.readline().strip()
                    linha_papel = arquivo.readline().strip()
                    
                    arquivo.readline() 

                    usuario_nome = linha_nome.split(':', 1)[1].strip()
                    usuario_senha = linha_senha.split(':', 1)[1].strip()
                    papel = linha_papel.split(':', 1)[1].strip()

                    if nome_input == usuario_nome and senha_input == usuario_senha:
                        print("\nLogin bem-sucedido")
                        login_sucesso = True
                        
                        if papel == "farmaceutico":
                            limpar_terminal()
                            menu_farmaceutico.MenuFarmaceutico().exibir_menu()
                        elif papel == "caixa":
                            limpar_terminal()
                            menu_caixa.MenuCaixa().exibir_menu()
                        break

            if not login_sucesso:
                print("\nErro: Nome de usuário ou senha incorretos.")

        except FileNotFoundError:
            print("Erro: O arquivo 'database/usuarios.txt' não foi encontrado.")
