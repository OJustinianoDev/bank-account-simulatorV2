class Conta:

    ids_existentes = set()

    def __init__(self, cursor, conexao, titular = 'usuario_desconhecido', saldo = 0):
        self.cursor = cursor
        self.conexao = conexao
        self._titular = titular
        self.__saldo = saldo
        self.id = None

    def __str__(self):
        return f'A conta {self.id} de {self._titular} tem R${self.__saldo:.2f} de saldo.'

    def criar_no_banco(self):
        self.cursor.execute("INSERT INTO contas (nome, saldo) VALUES (%s, %s);", (self._titular, self.__saldo))
        self.conexao.commit()
        self.id = self.cursor.lastrowid

    def depositar(self, valor):
        if valor <= 0:
            print('[ERRO] Valor inválido.')
            return False
        self.__saldo += valor
        self.cursor.execute("UPDATE contas SET saldo = %s WHERE id = %s;", (self.__saldo, self.id))
        self.cursor.execute("INSERT INTO transacoes (conta_id, tipo, valor) VALUES (%s, %s, %s);", (self.id, 'deposito', valor))
        self.conexao.commit()
        return True

    def sacar(self, valor):
        if valor > self.__saldo:
            print(f'Saque NEGADO de R${valor:.2f} na conta de {self.id}: SALDO INSULFICIENTE')
            return False
        self.__saldo -= valor
        self.cursor.execute("UPDATE contas SET saldo = %s WHERE id = %s;", (self.__saldo, self.id))
        self.cursor.execute("INSERT INTO transacoes (conta_id, tipo, valor) VALUES (%s, %s, %s);", (self.id, 'saque', valor))
        self.conexao.commit()
        print(f'Saque de R${valor:.2f} autorizado na conta {self.id}')
        return True

    def obter_saldo(self):
        return self.__saldo

    def consultar_saldo_banco(self):
        self.cursor.execute("SELECT saldo FROM contas WHERE id = %s;", (self.id,))
        resultado = self.cursor.fetchone()
        return resultado[0]

    def extrato(self):
        self.cursor.execute("SELECT * FROM transacoes WHERE conta_id = %s;", (self.id,))
        resultado = self.cursor.fetchall()
        return resultado