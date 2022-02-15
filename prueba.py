""" Hay dos formas para la conversión de Divisas
1. Es ver cuánto tenemos en cántidad respecto de la Moneda1 a las Moneda2 sería con una múltiplicación
2.Pero si queremos convertir el monto de la Moneda2 a la Moneda1 sería con una división

"""
class Divisa():
    """Representa el nombre y sibolo de la Divisa"""
    def __init__(self, name, simbolo, factor):
        self.name = name
        self.simbolo = simbolo
        self.factor = factor

    def convertir_a_base_divisa(self,numero):
        return numero * self.factor
    
    def convertir_desde_base_divisa(self, numero):
        return numero / self.factor

    def __repr__(self):
        return self.name

class Dinero():
    """Represennta la cantidad de dinero """
    def __init__(self, monto,divisa):
        self.monto = monto
        self.divisa =divisa

    def monto_base_divisas(self):
        return self.divisa.convertir_a_base_divisa(self.monto)
    
    def _add_ (self, montoDeDinero): 
        amount = self.monto_base_divisas() + montoDeDinero.monto_base_divisas()
        amount = self.divisa.convertir_desde_base_divisa(amount)
        return Dinero(amount, self.divisa) 
    
    def __sub__(self, montoDeDinero):
        amount = self.monto_base_divisas() - montoDeDinero.monto_base_divisas()
        amount = self.divisa.convertir_desde_base_divisa(amount)
        return Dinero(amount, self.divisa)

dolar = Divisa('dolar', 'USD', 3250)

one_dolar = Dinero(1,dolar)

