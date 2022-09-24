from datetime import date
import sqlite3
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QFileDialog
from arquivos_py.telaPrincipal import *
from arquivos_py.telaCadastro import *
from arquivos_py.telaPesquisa import *

class TelaCadastro(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Cadastro()
        self.ui.setupUi(self)
        #
        data = date.today()
        self.ui.inputData.setDate(data)
        #
        self.ui.btnCadastrar.clicked.connect(self.cadastra)
        #
    def cadastra(self):
        erro = []
        p = self.ui.cbProduto.currentText()
        data = self.ui.inputData.text()
        
        try:
            cxP = int(self.ui.inputPrimeiras.text())
            if (cxP < 0):
                raise
        except:
            erro.append("Primeiras")

        try:
            cxS = int(self.ui.inputSegundas.text())
            if(cxS < 0):
                raise
        except:
            erro.append("Segundas")

        try:
            preco = int(self.ui.inputPreco.text())
            if( preco < 0):
                raise
        except:
            erro.append("Preco")

        try:
            desc = int(self.ui.inputDesconto.text())
            if (desc < 0):
                raise
        except:
            erro.append("Desconto")
        
        if(len(erro) == 0):
            try:
                #Capturando mais dados
                precoLiquido = (cxP * (preco - 4)) + ((cxS / 2) * (preco - 4))
                precoTotal = (cxP * preco) + ((cxS / 2) * preco)
                #Criando banco de Dados
                banco = sqlite3.connect("Mercadorias.db")
                c = banco.cursor()
                c.execute("CREATE TABLE IF NOT EXISTS hortalica (id INTEGER PRIMARY KEY AutoIncrement , produto text, cxPrimeira text , cxSegunda text, preco text, desconto text, precoTotal text, precoLiquido text, data text);")
                c.execute("INSERT INTO hortalica (produto, cxPrimeira, cxSegunda, preco, desconto, precoTotal, precoLiquido, data) VALUES ('"+p+"', "+str(cxP)+", "+str(cxS)+", "+str(preco)+", "+str(precoTotal)+", "+str(desc)+", "+str(precoLiquido)+", '"+data+"')")
                banco.commit()

                #Limpando Tela
                self.ui.inputPrimeiras.setText("")
                self.ui.inputSegundas.setText("")
                self.ui.inputPreco.setText("")
                self.ui.inputDesconto.setText("")

                msg = QMessageBox()
                msg.setWindowTitle("Concluído!")
                msg.setText("\nDados Inseridos com Sucesso!")
                msg.setIcon(QMessageBox.Information)
                r = msg.exec()

            except:
                msg = QMessageBox()
                msg.setWindowTitle("ERRO!")
                msg.setText("\nERROR: Erro ao inserir dados!")
                msg.setIcon(QMessageBox.Information)
                r = msg.exec()
        
        else:
            x = ''
            n = 2
            msg = QMessageBox()
            msg.setWindowTitle("Aviso!")
            for i in erro:
                x = x + (i + ", ")
            x = x[:-n]

            msg.setText("\nInserção invalida para os campos: "+ x)
            msg.setIcon(QMessageBox.Information)

            retorno = msg.exec()        
        
    
    def closeEvent(self, e):
        self.o = Tela()
        self.o.show()
        self.o.move(QApplication.desktop().screen().rect().center()- self.o.rect().center())
        e.accept()

class TelaPesquisa(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Pesquisa()
        self.ui.setupUi(self)

        self.ui.btnPesquisar.clicked.connect(self.ExibeDados)
        self.ui.btnExcluir.clicked.connect(self.ExcluiDados)
        self.ui.pushButton.clicked.connect(self.Relatorio)

    def ExibeDados(self):
        #Ativando banco de dados
        banco = sqlite3.connect("Mercadorias.db")
        c = banco.cursor()
        filtro = self.ui.cbProduto.currentText()

        #pega dados
        if( filtro == "Todos"):
            x = c.execute("SELECT * FROM hortalica")
        else:
            x = c.execute("SELECT * FROM hortalica WHERE produto = '"+ filtro +"' ")
        y = list(x.fetchall())
        qtdLinhas = len(y)

        #Cria tabela de saída
        self.ui.tabela.clearContents()
        self.ui.tabela.setRowCount(qtdLinhas)

        #imprime dados
        for i in range(0, qtdLinhas, 1):
            for u in range(0, 9, 1):
                z = y[i][u]
                if(u == 0):
                    z = str(z)

                self.ui.tabela.setItem(i, u, QTableWidgetItem(z))

    def Relatorio(self):
        saida = []
        total = 0
        qtd = self.ui.tabela.rowCount()
        for i in range(0, qtd, 1):
            var = []
            for u in range(0, 9, 1):
                y = str(self.ui.tabela.item(i, u).text())
                var.append(y)
            
            x = var[2]+" Caixa(s) Primeira(s) e "+ var[3] +" Segunda(s) a "+ var[4] +" Reais, No dia "+ var[8]+"          Total: R$ "+ var[7]
            saida.append(x)

            total = total + float(var[7])


        conteudo = "                                            RELATÓRIO\n\n" 
        for i in saida :
            conteudo = conteudo + i +"\n"
        
        conteudo = conteudo + "\n\n\nTOTAL GERAL: "+ str(total)

        caminho,_ = QFileDialog.getSaveFileName(self, "Salvar", "relatorio.txt")
        arquivo = open(caminho, 'w')
        arquivo.write(conteudo)
        arquivo.close()
    
    def ExcluiDados(self):
        #Ativando banco de dados
        banco = sqlite3.connect("Mercadorias.db")
        c = banco.cursor()

        try:
            ID = int(self.ui.tabela.currentItem().text())
            c.execute("DELETE FROM hortalica WHERE id = %i" %ID )
            banco.commit()
            banco.close()
            self.ExibeDados()

            #Mensagem
            msg = QMessageBox()
            msg.setWindowTitle("Concluído!")
            msg.setText("\nDados Excluidos com Sucesso!")
            msg.setIcon(QMessageBox.Information)
            r = msg.exec()

        except:
            msg = QMessageBox()
            msg.setWindowTitle("Concluído!")
            msg.setText("\nERRO: Erro ao Excluir dados!")
            msg.setIcon(QMessageBox.Critical)
            r = msg.exec()
        
    def closeEvent(self, e):
        self.o = Tela()
        self.o.show()
        self.o.move(QApplication.desktop().screen().rect().center()- self.o.rect().center())
        e.accept()

class Tela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_TelaPrincipal()
        self.ui.setupUi(self)
        self.janela = TelaCadastro()
        self.janela2 = TelaPesquisa()

        self.ui.btnCadastra.clicked.connect(self.cadastra)
        self.ui.btnPesquisa.clicked.connect(self.pesquisa)
    
    def cadastra(self):
        self.janela.show()
        self.hide()
    
    def pesquisa(self):
        self.janela2.show()
        self.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Tela()
    w.show()
    sys.exit(app.exec_())
