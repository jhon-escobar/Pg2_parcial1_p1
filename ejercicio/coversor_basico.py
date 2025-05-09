class metodo_conversor_generico:
    def centimetros_a_metros(self, a):
        b = a / 100
        return b

conversor = metodo_conversor_generico()

a1 = 150
b1 = conversor.centimetros_a_metros(a1)
print(f"{a1} centímetros son {b1} metros.")

a2 = 235.75
b2 = conversor.centimetros_a_metros(a2)
print(f"{a2} centímetros son {b2} metros.")

a3 = 50
b3 = conversor.centimetros_a_metros(a3)
print(f"{a3} centímetros son {b3} metros.")
