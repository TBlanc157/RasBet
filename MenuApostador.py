import time
import re
from Menu import Menu
from CheckStructure import CheckStruct

jogosfutebol = ["Benfica - Chaves", "Sporting - Varzim", "Palmeiras - São Paulo"]

class MenuApostador:
    def __init__(self):
        self.obj = Menu("  Bem Vindo à RASBET.\n",["Desportos", "Carteira","Notificações","Boletim","Alterar informações de perfil","Sair"])

    # NO CONTROLLER 

    # Editar ===============================================================
    def menuEditar(self):
        edit = Menu(f"  Editar Conta\n", ["Email","Nome","Sair"])
        sels = []
        data = []
        while not edit.exit:
            sel = edit.menu.show()
            if sel == 0:
                print("Insira o novo email: ")
                novo_email = input()
                if CheckStruct.check(novo_email):
                    sels.append(sel)
                    data.append(novo_email)
                else:
                    Menu.showMessage("Aviso -> Email inválido.\n", 1)
            elif sel == 1:
                print("Insira o novo nome: ")
                novo_nome = input()
                sels.append(sel)
                data.append(novo_nome)
            elif sel == 2:
                edit.exit = True
        return sels, data

    # Desportos ============================================================
    def menuDesportos(self, sportsList):
        desportos = Menu("  Desportos.\n", sportsList + ["Sair"])
        sel = desportos.menu.show()
        if sel == len(sportsList):
            desportos.exit = True
            return False
        else:
            return sportsList[sel]

    def menuJogos(self, names, info):
        jogos = Menu(" Jogos.\n", names + ["Sair"])
        boletim = []
        while not jogos.exit:
            sel = jogos.menu.show()
            if sel == len(names):
                jogos.exit = True
            else:
                res,odd = self.menuEvento(info[sel], names[sel])
                if res!=None and odd:
                    boletim += [(info[sel][0],names[sel],res,odd)]
        return boletim

    # (id,nome,odd,jogaEmcasa)
    def menuEvento(self, gameInfo, name):
        opcoes = []
        for res in gameInfo:
            opcoes.append(f"{res[1]} : {res[2]}")
        evento = Menu(f" {name}\n" , opcoes + ["Sair"])
        sel = evento.menu.show()
        if sel == len(opcoes):
            return None,0
        res,odd = opcoes[sel].split(':')
        return res,float(odd)
            
            

    # Carteira =============================================================
    #INCOMPLETO
    def menuCarteira(self, usrId, saldo):
        carteira = Menu(f"  Saldo :: {saldo} .\n",["Histórico de Apostas","Histórico de transações","Depositar dinheiro","Levantar dinheiro","Sair"])        

        sel = carteira.menu.show()
        if sel == 0:
            return None,"A"
        elif sel == 1:
            return None,"T"
        elif sel == 2:
            valor = self.menuDepositar()
            if float(valor) > 0:
                return float(valor),"D"
        elif sel == 3:
            valor = self.menuLevantar()
            if float(valor) > 0:
                return float(valor),"L"
        elif sel == 4:
            carteira.exit = True
            return None,None

    # PT50000000000000000000000
    # Boletim ==============================================================
    def menuBoletim(self, boletim, saldo):
        txt = []
        odd_total = 1
        if boletim == []:
            odd_total = 0
        else:
            for aposta in boletim:
                txt += [f"{aposta[1]} {aposta[2]} {aposta[3]}"]
                odd_total *= float(aposta[3])

        bol = Menu(f"  Boletim | Odd Total: {'%.2f' % odd_total} | Saldo: {saldo}", txt + ["Apostar","Sair"])
        while not bol.exit:
            sel = bol.menu.show()
            if sel == len(txt):
                print("Insira montante a apostar: ")
                valor = input()
                if valor.isdecimal() and float(valor) < saldo:
                    Menu.showMessage(" -> Aposta realizada com sucesso.\n", 1)
                else:
                    Menu.showMessage("Aviso -> Saldo insuficiente", 1)
            elif sel == len(txt)+1:
                bol.exit = True

    #INCOMPLETO
    def menuNotif(self, email, notifs): 
        notif = Menu("  Notificações.\n",notifs+["Sair"])
        

    # FORA DO CONTROLLER

    # (id,nome,aposta,odd)


    def menuHistTransac(self,trans):
        lista_transac = []
        for elem in trans:
            lista_transac += [f"Data: {elem[1]} , Saldo antes: {elem[2]} , Transacao: {elem[3]}"]
        transac = Menu(f" Histórico de Transações .\n",lista_transac+["Sair"])

        while not transac.exit:
            sel = transac.menu.show()

            if sel == len(lista_transac):
                transac.exit = True


    def menuHistApostas(self,apostas):
        lista_aposta = []
        for elem in apostas:
            lista_aposta += [f"Data: {elem[1]} , Saldo antes: {elem[2]} , Transacao: {elem[3]}"]
            oi = 1
        hist_aposta = Menu(f" Histórico de Apostas .\n",lista_aposta+["Sair"])
        print(apostas)
        time.sleep(5)
        #[Row(idAposta=1, dataAposta=datetime.datetime(2022, 11, 4, 15, 34, 49), valorApostado=Decimal('10.00'))]

        while not hist_aposta.exit:
            sel = hist_aposta.menu.show()
            print(apostas)
            if sel == len(lista_aposta):
                hist_aposta.exit = True

    def menuDepositar(self):
        print("Prima Ctr+D para cancelar\n\n")
        print("-- Depositar Dinheiro\n")
        try:
            print("Quanto pretende transferir?\n")
            valor = input()
            if(valor.isdecimal or valor.isnumeric):
                metodo = self.menuTransf()
                if metodo == 1:
                    self.menuIBAN()
                return valor
            else:
                print("Aviso -> Valor inválido.")
                return -1
        except EOFError as e:
            return -2

    def checkIBAN(self,iban):
        if re.fullmatch(r'PT50\d{21}', iban):
            return True
        else:
            return False


    def menuLevantar(self):
        print("Prima Ctr+D para cancelar\n\n")
        print("-- Levantar Dinheiro  \n")
        try:
            while True:
                print("Quanto pretende transferir?\n")
                valor = input()
                print("Instira IBAN (PT50 + 21 digitos)\n")
                iban = input()
                if valor.isdecimal:
                    if self.checkIBAN(iban): 
                        return float(valor)
                    else:
                        print("Aviso -> IBAN inválido!\n")
                        time.sleep(1)
                        return 0
                else:
                    print("Aviso -> Valor inválido.\n")
                    time.sleep(1)
                    return 0
        except EOFError as e:
            return 0


    def menuTransf(self):
        metodos = ["MBWay","Transferência Bancária"]
        metodo = Menu(f" Método de Transferência.\n",metodos+["Sair"])
        sel = metodo.menu.show()
        if sel == 1:
            print("Instira IBAN (PT50 + 21 digitos)\n")
            iban = input()
            if self.checkIBAN(iban) == False: 
                print("Aviso -> IBAN inválido!\n")
                time.sleep(1)