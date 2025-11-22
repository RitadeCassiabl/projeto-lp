from menus.utils.limpar_terminal import limpar_terminal
class MenuRelatorios: 
    def exibir_menu(self):
        print("\n=== Menu Relatórios ===")
        print("1. Medicamentos tarja preta")
        print("2. Medicamentos que necessitam de prescrição")
        print("3. Medicamentos que não precisam de prescrição")
        print("0. Voltar")
        op = input("Escolha uma opção: ").strip()
        
        match op:
            case "1":
                limpar_terminal()
                self.gerar_relatorio_tarja_preta()
            case "2":
                limpar_terminal()
                self.gerar_relatorio_prescricao()
            case "3":
                limpar_terminal()
                self.gerar_relatorio_sem_prescricao()
            case "0":
                print("Saindo do menu de Relatórios.")
            case _:
                print("Opção inválida.")

    def gerar_relatorio_tarja_preta(self):
        limpar_terminal()
        print("=== Relatório de Medicamentos Tarja Preta ===")
        medicamentos_tarja_preta = []

        try:
            with open("database/medicamentos.txt", "r") as arquivo:
                linhas = arquivo.readlines()

            i = 0
            while i < len(linhas):
                linha_tarja_preta_index = i + 7

                if linha_tarja_preta_index < len(linhas):
                    linha_tarja_preta = linhas[linha_tarja_preta_index].strip()

                    if linha_tarja_preta.startswith("tarjaPreta:"):
                        valor_tarja_preta_str = linha_tarja_preta.split(':', 1)[1].strip().lower()

                        if valor_tarja_preta_str == 'Sim' or valor_tarja_preta_str =='sim':
                            try:
                                nome = linhas[i].split(':', 1)[1].strip()
                                fabricante = linhas[i+1].split(':', 1)[1].strip()
                                dosagem = linhas[i+2].split(':', 1)[1].strip()
                                quantidade_str = linhas[i+4].split(':', 1)[1].strip()

                                quantidade = int(quantidade_str)
                            except (IndexError, ValueError):
                                print(f"Aviso: Bloco de medicamento incompleto/inválido encontrado na linha {i+1}. Ignorado.")
                                quantidade = 0

                            medicamentos_tarja_preta.append({
                                'nome': nome,
                                'fabricante': fabricante,
                                'dosagem': dosagem,
                                'quantidade': quantidade
                            })

                    i += 9
                else:
                    break
        except FileNotFoundError:
            print("Erro: O arquivo 'database/medicamentos.txt' não foi encontrado.")
            return

        if medicamentos_tarja_preta:
            print("\n" + "=" * 75)
            print("RELATÓRIO DE MEDICAMENTOS TARJA PRETA EM ESTOQUE")
            print("=" * 75)
            print(f"{'NOME':<25}{'FABRICANTE':<20}{'DOSAGEM':<15}{'QTD. EM ESTOQUE':>15}")
            print("-" * 75)
            for med in medicamentos_tarja_preta:
                print(f"{med['nome']:<25}{med['fabricante']:<20}{med['dosagem']:<15}{med['quantidade']:>15}")
            print("-" * 75)
            print(f"Total de medicamentos tarja preta encontrados: {len(medicamentos_tarja_preta)}")
        else:
            print("\nNenhum medicamento tarja preta foi encontrado no estoque.")

        input("\nPressione Enter para voltar ao menu")

    def gerar_relatorio_prescricao(self):
        limpar_terminal()
        print("=== Relatório de Medicamentos Com Prescrição médica ===")
        medicamentos_prescricao = []

        try:
            with open("database/medicamentos.txt", "r") as arquivo:
                linhas = arquivo.readlines()

            i = 0
            while i < len(linhas):
                linha_prescricao_index = i + 6

                if linha_prescricao_index < len(linhas):
                    linha_prescricao = linhas[linha_prescricao_index].strip()

                    if linha_prescricao.startswith("prescricao:"):
                        valor_prescricao_str = linha_prescricao.split(':', 1)[1].strip().lower()

                        if valor_prescricao_str == 'Sim' or valor_prescricao_str == 'sim':
                            try:
                                nome = linhas[i].split(':', 1)[1].strip()
                                fabricante = linhas[i+1].split(':', 1)[1].strip()
                                dosagem = linhas[i+2].split(':', 1)[1].strip()
                                quantidade_str = linhas[i+4].split(':', 1)[1].strip()

                                quantidade = int(quantidade_str)
                            except (IndexError, ValueError):
                                print(f"Aviso: Bloco de medicamento incompleto/inválido encontrado na linha {i+1}. Ignorado.")
                                quantidade = 0

                            medicamentos_prescricao.append({
                                'nome': nome,
                                'fabricante': fabricante,
                                'dosagem': dosagem,
                                'quantidade': quantidade
                            })

                    i += 9
                else:
                    break
        except FileNotFoundError:
            print("Erro: O arquivo 'database/medicamentos.txt' não foi encontrado.")
            return

        if medicamentos_prescricao:
            print("\n" + "=" * 75)
            print("RELATÓRIO DE MEDICAMENTOS QUE NECESSITAM DE PRESCRIÇÃO MÉDICA EM ESTOQUE")
            print("=" * 75)
            print(f"{'NOME':<25}{'FABRICANTE':<20}{'DOSAGEM':<15}{'QTD. EM ESTOQUE':>15}")
            print("-" * 75)
            for med in medicamentos_prescricao:
                print(f"{med['nome']:<25}{med['fabricante']:<20}{med['dosagem']:<15}{med['quantidade']:>15}")
            print("-" * 75)
            print(f"Total de medicamentos que precisam de prescrição médica encontrados: {len(medicamentos_prescricao)}")
        else:
            print("\nNenhum medicamento que precisa de prescrição médica foi encontrado no estoque.")

        input("\nPressione Enter para voltar ao menu")

    def gerar_relatorio_sem_prescricao(self):
        limpar_terminal()
        print("=== Relatório de Medicamentos Sem Prescrição médica ===")
        medicamentos_prescricao = []

        try:
            with open("database/medicamentos.txt", "r") as arquivo:
                linhas = arquivo.readlines()

            i = 0
            while i < len(linhas):
                linha_prescricao_index = i + 6

                if linha_prescricao_index < len(linhas):
                    linha_prescricao = linhas[linha_prescricao_index].strip()

                    if linha_prescricao.startswith("prescricao:"):
                        valor_prescricao_str = linha_prescricao.split(':', 1)[1].strip().lower()

                        if valor_prescricao_str == 'Não' or valor_prescricao_str == 'não':
                            try:
                                nome = linhas[i].split(':', 1)[1].strip()
                                fabricante = linhas[i+1].split(':', 1)[1].strip()
                                dosagem = linhas[i+2].split(':', 1)[1].strip()
                                quantidade_str = linhas[i+4].split(':', 1)[1].strip()

                                quantidade = int(quantidade_str)
                            except (IndexError, ValueError):
                                print(f"Aviso: Bloco de medicamento incompleto/inválido encontrado na linha {i+1}. Ignorado.")
                                quantidade = 0

                            medicamentos_prescricao.append({
                                'nome': nome,
                                'fabricante': fabricante,
                                'dosagem': dosagem,
                                'quantidade': quantidade
                            })

                    i += 9
                else:
                    break
        except FileNotFoundError:
            print("Erro: O arquivo 'database/medicamentos.txt' não foi encontrado.")
            return

        if medicamentos_prescricao:
            print("\n" + "=" * 75)
            print("RELATÓRIO DE MEDICAMENTOS QUE NÃO NECESSITAM DE PRESCRIÇÃO MÉDICA EM ESTOQUE")
            print("=" * 75)
            print(f"{'NOME':<25}{'FABRICANTE':<20}{'DOSAGEM':<15}{'QTD. EM ESTOQUE':>15}")
            print("-" * 75)
            for med in medicamentos_prescricao:
                print(f"{med['nome']:<25}{med['fabricante']:<20}{med['dosagem']:<15}{med['quantidade']:>15}")
            print("-" * 75)
            print(f"Total de medicamentos que não precisam de prescrição médica encontrados: {len(medicamentos_prescricao)}")
        else:
            print("\nNenhum medicamento que não precisa de prescrição médica foi encontrado no estoque.")

        input("\nPressione Enter para voltar ao menu")