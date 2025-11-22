from classes.medicamento import Medicamento
from menus.utils.limpar_terminal import limpar_terminal
from menus.relatorios import MenuRelatorios
class MenuFarmaceutico:
    def exibir_menu(self):
        while True:
            print("====== Menu do Farmacêutico ======")
            print("1. Adicionar Medicamento")
            print("2. Remover Medicamento")
            print("3. Atualizar Estoque")
            print("4. Visualizar Medicamentos")
            print("5. Relatórios")
            print("6. Pesquisar Medicamento")
            print("0. Sair")
            op = input("Escolha uma opção: ")
        
            match op:
                case "1":
                    limpar_terminal()
                    print("\nAdicionar Medicamento selecionado.")
                    try:
                        nome = input("\nNome do Medicamento: ")
                        fabricante = input("Fabricante: ")
                        dosagem = input("Dosagem: ")
                        preco = float(input("Preço: "))
                        quantidade = int(input("Quantidade: "))
                        tipo = input("Tipo (genérico, similar, referência): ")
                    
                        prescricao_input = input("Requer prescrição? (s/n): ").strip().lower()
                        if prescricao_input == 's':
                            prescricao = 'Sim'
                        else:
                            prescricao = 'Não'
                        
                        tarjaPreta_input = input("É tarja preta? (s/n): ").strip().lower()
                        if tarjaPreta_input == 's':
                            tarjaPreta = 'Sim'
                        else:
                            tarjaPreta = 'Não'
                    
                        medicamento = Medicamento(nome, fabricante, dosagem, preco, quantidade, tipo, prescricao, tarjaPreta)
                        with open("database/medicamentos.txt", "a") as arquivo:
                            arquivo.write(f"nome:{medicamento.get_nome()}\n")
                            arquivo.write(f"fabricante:{medicamento.get_fabricante()}\n")
                            arquivo.write(f"dosagem:{medicamento.get_dosagem()}\n")
                            arquivo.write(f"preco:{medicamento.get_preco()}\n")
                            arquivo.write(f"quantidade:{medicamento.get_quantidade()}\n")
                            arquivo.write(f"tipo:{medicamento.get_tipo()}\n")
                            arquivo.write(f"prescricao:{medicamento.get_prescricao()}\n")
                            arquivo.write(f"tarjaPreta:{medicamento.get_tarjaPreta()}\n\n")
                    
                        print(f"\nMedicamento '{nome}' adicionado com sucesso!")
                    
                    except FileNotFoundError:
                        print("Erro: O arquivo 'database/medicamentos.txt' não foi encontrado.")
                case "2":
                    limpar_terminal()
                    print("\nRemover Medicamento selecionado.")
                    nome_deletar = input("\nDigite o nome do medicamento a ser deletado: ").strip()
    
                    linhas_para_manter = [] 
    
                    medicamento_encontrado = False

                    try:
                        with open("database/medicamentos.txt", "r") as arquivo:
                            linhas = arquivo.readlines()
        
                        i = 0
                        while i < len(linhas):
                            linha_atual = linhas[i].strip()
            
                            if linha_atual.startswith("nome:") and linha_atual.split(':', 1)[1].strip().lower() == nome_deletar.lower():
                                medicamento_encontrado = True
                                print(f"\nMedicamento '{nome_deletar}' encontrado. Excluindo...")
                
                                i += 9
                                continue
                            linhas_para_manter.append(linhas[i])
                            i += 1

                        if medicamento_encontrado:
                            with open("database/medicamentos.txt", "w") as arquivo:
                                arquivo.writelines(linhas_para_manter)
                                print(f"\nSucesso: O medicamento '{nome_deletar}' foi removido do estoque.")
                        else:
                            print(f"\nAviso: Medicamento '{nome_deletar}' não encontrado no arquivo.")
                    
                    except FileNotFoundError:
                        print("Erro: O arquivo 'database/medicamentos.txt' não foi encontrado.")
                case "3":
                    limpar_terminal()
                    print("Atualizar Estoque selecionado.")
                    nome_atualizar = input("\nDigite o nome do medicamento que deseja atualizar: ").strip()
    
                    medicamento_encontrado = False
                    novas_linhas = []

                    try:
                        with open("database/medicamentos.txt", "r") as arquivo:
                            linhas = arquivo.readlines()
        
                        i = 0
                        while i < len(linhas):
                            linha_atual = linhas[i].strip()

                            if linha_atual.startswith("nome:") and linha_atual.split(':', 1)[1].strip().lower() == nome_atualizar.lower():
                                medicamento_encontrado = True
                                print(f"\nMedicamento '{nome_atualizar}' encontrado. Por favor, insira os novos dados.")
                                
                                try:
                                    novo_preco = float(input(f"Digite o novo preço do medicamento (preço atual {linhas[i+3].split(':', 1)[1].strip()}): "))
                                    nova_quantidade = int(input(f"Digite a nova quantidade em estoque (estoque atual {linhas[i+4].split(':', 1)[1].strip()}): "))
                                except ValueError:
                                    print("Erro: Preço e Quantidade devem ser números válidos.")
                                    break 
                
                                fabricante = linhas[i+1].split(':', 1)[1].strip()
                                dosagem = linhas[i+2].split(':', 1)[1].strip()
                                tipo = linhas[i+5].split(':', 1)[1].strip()
                                prescricao = linhas[i+6].split(':', 1)[1].strip()
                                tarjaPreta = linhas[i+7].split(':', 1)[1].strip()


                                medicamento_atualizado = Medicamento(
                                    nome_atualizar, fabricante, dosagem, novo_preco, 
                                    nova_quantidade, tipo, prescricao, tarjaPreta
                                )
            
                                novas_linhas.append(f"nome:{medicamento_atualizado.get_nome()}\n")
                                novas_linhas.append(f"fabricante:{medicamento_atualizado.get_fabricante()}\n")
                                novas_linhas.append(f"dosagem:{medicamento_atualizado.get_dosagem()}\n")
                                novas_linhas.append(f"preco:{medicamento_atualizado.get_preco()}\n")
                                novas_linhas.append(f"quantidade:{medicamento_atualizado.get_quantidade()}\n")
                                novas_linhas.append(f"tipo:{medicamento_atualizado.get_tipo()}\n")
                                novas_linhas.append(f"prescricao:{medicamento_atualizado.get_prescricao()}\n")
                                novas_linhas.append(f"tarjaPreta:{medicamento_atualizado.get_tarjaPreta()}\n")
                                novas_linhas.append("\n")

                                i += 9 
                                continue
            
                            novas_linhas.append(linhas[i])
                            i += 1
                        if medicamento_encontrado:
                            with open("database/medicamentos.txt", "w") as arquivo:
                                arquivo.writelines(novas_linhas)
                                print(f"\nSucesso: Estoque e preço do medicamento '{nome_atualizar}' foram atualizados.")
                        else:
                            print(f"\nAviso: Medicamento '{nome_atualizar}' não encontrado no arquivo.")
                    
                    except FileNotFoundError:
                        print("Erro: O arquivo 'database/medicamentos.txt' não foi encontrado.")
            
                case "4":
                    limpar_terminal()
                    print("Visualizar Medicamentos selecionado.")
                    try:
                        with open("database/medicamentos.txt", "r") as arquivo:
                            conteudo = arquivo.read().strip()
                            if conteudo:
                                medicamentos = conteudo.split("\n\n")
                                print("\n=== Lista de Medicamentos ===")
                                for medicamento_str in medicamentos:
                                    linhas = medicamento_str.strip().split("\n")
                                    for linha in linhas:
                                        print(linha)
                                    print("\n")
                                print("=== Fim da Lista ===\n")
                            else:
                                print("\nNenhum medicamento cadastrado.")
                    except FileNotFoundError:
                        print("Erro: O arquivo 'database/medicamentos.txt' não foi encontrado.")
                case "5":
                    limpar_terminal()
                    print("Relatórios selecionado.")
                    relatorios = MenuRelatorios()
                    relatorios.exibir_menu()
                    
                case "6":
                    limpar_terminal()
                    print("Pesquisar Medicamento selecionado.")
                    nome_pesquisar = input("\nDigite o nome do medicamento a ser pesquisado: ").strip().lower()
                    medicamento_encontrado = False
                    try:
                        with open("database/medicamentos.txt", "r") as arquivo:
                            linhas = arquivo.readlines()
        
                        i = 0
                        while i < len(linhas):
                            linha_atual = linhas[i].strip()
            
                            if linha_atual.startswith("nome:") and linha_atual.split(':', 1)[1].strip().lower() == nome_pesquisar:
                                medicamento_encontrado = True
                                print(f"\nMedicamento '{nome_pesquisar}' encontrado:")
                                for j in range(9): 
                                    if i + j < len(linhas):
                                        print(linhas[i + j].strip())
                                print()
                
                                i += 9 
                                continue
            
                            i += 1

                        if not medicamento_encontrado:
                            print(f"\nAviso: Medicamento '{nome_pesquisar}' não encontrado no arquivo.")
                    
                    except FileNotFoundError:
                        print("Erro: O arquivo 'database/medicamentos.txt' não foi encontrado.")
                case "0":
                    print("Saindo")
                    break
                case _:
                    print("Opção inválida. Tente novamente.")
                    input("Pressione Enter para continuar")
                    
                    
