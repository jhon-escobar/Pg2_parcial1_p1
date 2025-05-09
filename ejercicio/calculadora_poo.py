class Calculadora:
    def __init__(self):
        
        self.cm = 0
        self.mt = 100

    def cm_a_mt(self,a,b):
        self.cm = "cm_a_mt"
        
        self.mt = a / b
        return self.mostrar_operacion(a,b)
    
    def mostrar_operacion(self,a,b):
        return f"{self.operacion}: {a} y {b} = {self.resultado}"
def cm_a_metros(cm):
  metros = cm / 100
  return metros