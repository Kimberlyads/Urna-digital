#importação de biblotecas
import random
import json
import os

if os.path.exists("votos.json"):
    with open ("votos.json", "r") as arquivo:
        dados_salvos = json.load(arquivo)
        candidatos = {int(chave): valor for chave, valor in dados_salvos["candidatos"].items()}
        nulos = dados_salvos["nulos"]
        brancos = dados_salvos["brancos"]
        print("[SISTEMA] Dados de votação anteriores carregados com sucesso!")
else:
    # Declaração da lista e das variaveis
    candidatos = {}
    nulos = 0
    brancos = 0

    print("Iniciando o Sistema...")


#configuração de senha
senha_admin = "1234"

def salvar_dados():
    dados_para_salvar = {
        "candidatos": candidatos,
        "nulos": nulos,
        "brancos": brancos
    }
    with open("votos.json", "w") as arquivo:
        json.dump(dados_para_salvar, arquivo, indent=4)

# Menu de Entrada
while True:
    print("\n__________Urna Digital_________")
    info = input("Você é Votante ou Colaborador?: ").strip().upper()
    encerrar = False

    # Menu do Colaborador
    if info == "COLABORADOR":
        autenticado = False
        tentativas = 3

        print("-----------------------------------------")
        print("Autenticação")
        while tentativas > 0:
            senha = input("Digite a senha: ")

            if senha == senha_admin:
               autenticado = True
               break
            else:
                tentativas -= 1
                print(f"Senha incorreta! Você tem mais {tentativas} tentativa(s)!")
                print("-----------------------------------------")
        if not autenticado:
            print("\n[Acesso negado] Limite de senhas excedido!")

        autenticado_mfa = False
        tentativas = 1

        while tentativas > 0:
            codigo_mfa = random.randint(1000, 9999)
            print(f"\n[MFA] Token de segurança enviada para o seu dispositivo: {codigo_mfa}")

            try:
                confirmando_mfa = int(input("Digite o Token: "))
            except ValueError:
                print("Entrada inválida!.")
                tentativas -= 1
                autenticado_mfa = True
                continue
            if confirmando_mfa == codigo_mfa:
                print("\nAutenticação concluida! Bem-vindo Colaborador(a)!")
                autenticado_mfa = True
                break
            else:
                print("Token incorreto!")
                tentativas -= 1

        if not autenticado_mfa:
            print("\n[Acesso Negado] Falha na Validação do Token!.")
            continue

        while True:
            print("-----------------------------------------")
            print("\nMenu Colaborador: ")
            try:
                menu = int(input("\nDigite a opção que deseja:\n"
                                 "\n1 = Adicionar Candidato\n"
                                 "\n2 = Excluir Candidato\n"
                                 "\n3 = Listar candidatos cadastrados\n"
                                 "\n4 = Ver Apuração de Votos\n"
                                 "\n5 = Voltar ao Menu inicial\n"
                                 "\n6 = Encerrar o programa\n"
                                 ""))
            except ValueError:
                print("Digite um número válido!")
                continue

            if menu == 1:
                # Cadastro de Candidatos (Nome; Número; Cargo)
                while True:
                    cand = input("Digite o nome do Candidato: ").strip().upper()
                    try:
                        num = int(input("Digite o número correspondente: "))
                    except ValueError:
                        print("Digite apenas números! Tente novamente!")
                        continue
                    cargo = input("Digite o Cargo: ").strip().upper()

                    if num in candidatos:
                        print(f"\nErro! Número já Cadastrado para {candidatos[num][0]}!")
                    else:
                        candidatos[num] = [cand, cargo, 0]
                        print(f"\nCandidato {cand} (n° {num}) cadastrado!")
                        salvar_dados()

                    while True:
                        info = input("Deseja adicionar um novo candidato? (S/N): ").strip().upper()
                        if info in ["S","N"]:
                            break
                        print("Opção inválida! ", end="")
                    if info == "N":
                        break

            elif menu == 2:
                # Exclusão de Algum Candidato
                if not candidatos:
                    print("Não há Candidatos cadastrados")
                    continue
                else:
                    print("\nCandidatos Cadastrados: ")
                    for num, dados in candidatos.items():
                        print(f"N° {num} - {dados[0]} {dados[1]}")
                    try:
                        exclui = int(input("Qual candidato você deseja exluir? (digite apenas o numero): "))
                    except ValueError:
                        print("Número invalido!")
                        continue
                    if exclui in candidatos:
                        nome_exclui = candidatos[exclui][0]
                        info = input(f"Deseja excluir esse Candidato: {nome_exclui} (n°{exclui})? (S/N) ")
                        if info == "S" or info == "s":
                            tentativa = 1
                            exclusao = False
                            while tentativa > 0:
                                confirmacao = random.randint(1000,9999)
                                print(f"Token de confirmação enviado para seu dispositivo! {confirmacao}")

                                try:
                                    confirmacao_exclui = int(input("Digite o Token: "))
                                except ValueError:
                                    print("Token incorreto! Cancelando ação!")
                                    tentativa -= 1
                                    exclusao = True

                                if confirmacao_exclui == confirmacao:
                                    del candidatos[exclui]
                                    print(f"Candidato excuido com Sucesso!")
                                    exclusao = True
                                    salvar_dados()
                                    break
                                else:
                                    print("\n Cancelando Ação!")
                                    tentativa -= 1
                            if not exclusao:
                                continue
                        else:
                            print("Exclusão Cancelada!")
                    else:
                        print("Número do Candidato não encontrado")

            elif menu == 3:
                if not candidatos:
                    print("Nenhum candidato cadastrado!")
                else:
                    print(f"Total de candidatos cadastrados: {len(candidatos)}")
                    for num,dados in candidatos.items():
                        print(f"N° {num} - {dados[0]} | Cargo: {dados[1]}")

            elif menu == 4:
                # Apuração dos Votos
                if not candidatos and nulos == 0 and brancos == 0:
                    print("Nenhum voto computado")
                    continue
                total = 0
                for dados in candidatos.values():
                    total += dados[2]

                total_geral = total + nulos + brancos

                print("-----------------------------------------")
                print("\nAPURAÇÃO DE VOTOS")
                print(f"\nTotal de Candidatos cadastrados: {len(candidatos)}")
                print(f"\nTotal de votos computados: {total_geral}")

                # Calculo do percentual dos votos nulos e em branco e a apuração dos votos
                if total_geral <= 0:
                    print(f"\nNenhum Voto computado!")
                    print("-----------------------------------------")
                else:
                    if nulos <= 0:
                        print(f"\nNenhum Voto Nulo computado!")
                    else:
                        percent_nulo = (nulos / total_geral) * 100
                        print(f"\nVotos Nulos: {nulos}\nPercentual: {percent_nulo: .2f}%")

                    if brancos <= 0:
                        print("\nNenhum voto branco computado!")
                    else:
                        percent_branco = (brancos / total_geral) * 100
                        print(f"\nVotos em Branco: {brancos}\nPercentual: {percent_branco:.2f}% ")

                    if total <= 0:
                        print("\nNenhum Voto válido computado!")
                        print("-----------------------------------------")
                    else:
                        percent_valido = (total/total_geral) * 100
                        print(f"\nVotos válidos: {total}\nPercentual: {percent_valido:.2f}%")
                        print("-----------------------------------------")

                # Calculo e apuração de votos dos candidatos
                print("VOTOS POR CANDIDATOS")
                maior_voto = 0
                ganhador = []

                for num, dados in candidatos.items():
                    nome = dados[0]
                    cargo = dados [1]
                    votos = dados [2]

                    if votos <= 0:
                        print("Nenhum voto computado!")
                    else:
                        percent = (votos/ total_geral) * 100
                        print(f"\nN° {num} - {nome} ({cargo})")
                        print(f"\nVotos: {votos}\nPercentual: {percent: .2f}%")

                    # Quem tem mais votos
                    if votos > maior_voto:
                        maior_voto = votos
                        ganhador = [nome]
                    elif votos == maior_voto and votos > 0:
                        ganhador.append(nome)

                    # Ganhador
                if total > 0 and len(ganhador) == 1:
                    print(f"\nGANHADOR(A)\n {ganhador[0]} com {maior_voto} votos!")
                elif total_geral >= 0 and len(ganhador) > 1:
                    print(f"\nEMPATE entre os candidatos: {', '.join(ganhador)} com {maior_voto} votos cada!")
                else:
                    print("NENHUM VOTO COMPUTADO")

            elif menu == 5:
                break
            elif menu == 6:
                print("\nEncerrando o programa....")
                encerrar = True
                break
            else:
                print("\nOpção inválida digite um número de 1 a 5")

    # Menu do Votante
    elif info == "VOTANTE":
        if not candidatos:
            print("\nNão há Candidatos cadastrados para voto!")
        else:
            print("\nCANDIDATOS DISPONIVEIS\n")
            for num, dados in candidatos.items():
                print(f"\nN°{num} - {dados[0]}({dados[1]})")
            print("\nN° 0 - Voto em Branco")
            print("\nN° -1 - Voto Nulo")

            voto = int(input("Digite seu Voto: "))

            # Contabilizando voto em branco
            if voto == 0:
                info = input("Você confirma Voto em Branco? (S/N)").strip().upper()
                if info == "S":
                    print("Contabilizando Voto em Branco")
                    brancos += 1
                    salvar_dados()
                    continue
                else:
                    print("Voto cancelado!")
            # Contabilizando voto em candidatos
            elif voto in candidatos:
                name_cand = candidatos[voto][0]
                info = input(f"Você deseja votar em {name_cand} (N° {voto})? (S/N)")
                if info == "S" or info == "s":
                    candidatos[voto][2] += 1
                    print("Voto computado com sucesso")
                    salvar_dados()
                else:
                    print("Voto cancelado")
                    continue
            else:
                info = input("Você confirma Voto Nulo? (S/N)")
                if info == "S" or info == "s":
                    print("Contabilizando Voto Nulo")
                    nulos += 1
                    salvar_dados()
                else:
                    print("Voto cancelado!")
                    continue

    else:
        print("\nERRO!\n Opção Inválida! Digite apenas 'Votante' ou 'Colaborador'")

    if 'encerrar' in locals() and encerrar:
        break
