from classes.menus.utils.limpar_terminal import limpar_terminal
from classes.venda import Venda
from classes.venda import Pagamento

def _mapear_medicamentos_para_venda():
    medicamentos_map = {}
    try:
        with open("database/medicamentos.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            i = 0
            while i < len(linhas):
                linha_atual = linhas[i].strip()
                
                if linha_atual.startswith("nome:"):
                    nome = linha_atual.split(':', 1)[1].strip().lower()

                    if i + 3 < len(linhas) and linhas[i+3].strip().startswith("preco:"):
                        preco_str = linhas[i+3].split(':', 1)[1].strip()
                        
                        if i + 4 < len(linhas) and linhas[i+4].strip().startswith("quantidade:"):
                            qtd_str = linhas[i+4].split(':', 1)[1].strip()
                            
                            try:
                                preco = float(preco_str)
                                quantidade = int(qtd_str)
                                
                                medicamentos_map[nome] = {
                                    'preco': preco,
                                    'quantidade': quantidade
                                }
                            except ValueError:
                                print(f"Aviso: Dado inválido para '{nome}'. Preço: '{preco_str}', Qtd: '{qtd_str}'. Ignorando.")
                                pass
                            
                    i += 9 
                else:
                    i += 1
    except FileNotFoundError:
        print("Erro: O arquivo 'database/medicamentos.txt' não foi encontrado.")
        return None
    
    return medicamentos_map


def _atualizar_medicamentos_estoque(itens_vendidos):
    try:
        with open("database/medicamentos.txt", "r") as arquivo:
            linhas = arquivo.readlines()
        
        novas_linhas = []
        i = 0
        while i < len(linhas):
            linha_atual = linhas[i]
            
            if linha_atual.strip().startswith("nome:"):
                nome = linha_atual.split(':', 1)[1].strip().lower()
                
                if nome in itens_vendidos and i + 4 < len(linhas) and linhas[i+4].strip().startswith("quantidade:"):
                    
                    qtd_line_index = i + 4
                    
                    novas_linhas.extend(linhas[i:qtd_line_index])
                    
                    try:
                        qtd_atual_str = linhas[qtd_line_index].split(':', 1)[1].strip()
                        qtd_atual = int(qtd_atual_str)
                        qtd_vendida = itens_vendidos[nome]
                        
                        nova_qtd = qtd_atual - qtd_vendida
                        
                        if nova_qtd < 0:
                             nova_qtd = 0 
                             print(f"Aviso: Estoque de '{nome.capitalize()}' não pode ser negativo. Definido para 0.")

                        nova_linha_qtd = f"quantidade: {nova_qtd}\n"
                        novas_linhas.append(nova_linha_qtd)
                        
                        i = qtd_line_index + 1
                        continue
                        
                    except ValueError:
                        print(f"Erro ao processar quantidade para '{nome.capitalize()}'. Mantendo original.")
                        novas_linhas.append(linhas[qtd_line_index])
                
            novas_linhas.append(linha_atual)
            i += 1
            
        with open("database/medicamentos.txt", "w") as arquivo:
            arquivo.writelines(novas_linhas)
            
        return True
    
    except Exception as e:
        print(f"Erro ao atualizar o estoque: {e}")
        return False


class MenuCaixa:
    def exibir_menu(self):
        while True:
            limpar_terminal()
            print("=== Menu Caixa ===")
            print("1. Nova venda")
            print("0. Sair")
            op = input("Escolha uma opção: ").strip()
            
            match op:
                case "1":
                    self.processar_nova_venda()
                case "0":
                    print("Saindo do menu do Caixa.")
                    break
                case _:
                    print("Opção inválida.")
                    input("Pressione Enter para continuar...")
    
    def processar_nova_venda(self):
        limpar_terminal()
        print("Nova venda selecionada.")
        
        pagamento_input = input("\nDigite o método de pagamento (dinheiro, pix, debito, credito): ").strip().upper()
        
        try:
            pagamento_metodo = Pagamento[pagamento_input]
            print(f"\nPagamento via {pagamento_metodo.value} registrado com sucesso.")
        except KeyError:
            print("\nErro: Método de pagamento inválido.")
            input("Pressione Enter para continuar...")
            return

        itens_input = input("Itens da venda (ex: nome do medicamento:quantidade, nome2:quantidade2, ...): ").strip()
        
        itens_venda = {}
        try:
            pares = itens_input.split(',')
            for par in pares:
                if ':' in par:
                    nome, qtd_str = par.split(':', 1)
                    itens_venda[nome.strip().lower()] = int(qtd_str.strip())
        except ValueError:
            print("Erro: A quantidade de um item deve ser um número inteiro válido.")
            input("Pressione Enter para continuar...")
            return

        if not itens_venda:
            print("Erro: Nenhuma quantidade de item válida fornecida.")
            input("Pressione Enter para continuar...")
            return

        medicamentos_data = _mapear_medicamentos_para_venda()
        if medicamentos_data is None:
            input("Pressione Enter para continuar...")
            return

        total_venda = 0.0
        comprovante_itens = []
        itens_para_atualizar_estoque = {}
        
        for nome_item, quantidade_pedida in itens_venda.items():
            if nome_item in medicamentos_data:
                item_info = medicamentos_data[nome_item]
                
                if quantidade_pedida > item_info['quantidade']:
                    print(f"Erro: Estoque insuficiente para '{nome_item.capitalize()}'. Pedido: {quantidade_pedida}, Estoque: {item_info['quantidade']}")
                    input("Pressione Enter para cancelar a venda...")
                    return
                    
                preco_unitario = item_info['preco']
                subtotal = preco_unitario * quantidade_pedida
                total_venda += subtotal
                
                comprovante_itens.append({
                    "nome": nome_item.capitalize(), 
                    "qtd": quantidade_pedida, 
                    "preco_unit": preco_unitario, 
                    "subtotal": subtotal
                })
                itens_para_atualizar_estoque[nome_item] = quantidade_pedida
            else:
                print(f"Aviso: O medicamento '{nome_item.capitalize()}' não foi encontrado no estoque e será ignorado.")
                
        if total_venda == 0.0 and itens_venda:
            print("Aviso: Nenhum item válido foi processado. Venda cancelada.")
            input("Pressione Enter para continuar...")
            return
            
        venda = Venda(comprovante_itens, total_venda, pagamento_metodo) 

        print("\n" + "="*50)
        print("COMPROVANTE DE VENDA")
        print("="*50)
        print(f"Pagamento: {venda.get_pagamento()}")
        print("-" * 50)
        print(f"{'ITEM':<30}{'QTD':<5}{'UNIT.':>7}{'TOTAL':>8}")
        for item in venda.get_comprovante_itens():
            print(f"{item['nome']:<30}{item['qtd']:<5}{item['preco_unit']:>7.2f}{item['subtotal']:>8.2f}")
        print("-" * 50)
        print(f"{'VALOR FINAL':<41}R$ {venda.get_total():>6.2f}")
        print("="*50)

        try:
            with open("database/vendas.txt", "a") as arquivo:
                arquivo.write(f"pagamento:{venda.get_pagamento()}\n")
                arquivo.write(f"itens:{venda.get_itens_para_gravar()}\n")
                arquivo.write(f"total:{venda.get_total():.2f}\n\n")
            
            print(f"\nVenda registrada com sucesso!")
            
            if _atualizar_medicamentos_estoque(itens_para_atualizar_estoque):
                 print("Estoque atualizado com sucesso!")
            else:
                 print("Falha na atualização de estoque. Verifique o log de erros.")
                 
        except Exception as e:
            print(f"Erro ao gravar a venda: {e}")
            
        input("Pressione Enter para retornar ao menu do Caixa...")