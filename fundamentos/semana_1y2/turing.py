class TuringMachine:
    def __init__(self, tape):
        self.tape = list(tape)  # Convertimos la cadena en una lista para facilitar la manipulación
        self.head = 0           # Posición inicial del cabezal
        self.state = 'q0'       # Estado inicial

    def step(self):
        # Comprobamos el estado actual y el símbolo en la cinta
        if self.state == 'q0':
            if self.head < len(self.tape):
                if self.tape[self.head] == '0':
                    self.state = 'q1'  # Si encontramos un 0, cambiamos al estado q1
                # Mover el cabezal a la derecha
                self.head += 1
            else:
                self.state = 'halt'  # Si llegamos al final de la cinta, detenemos la máquina

        elif self.state == 'q1':
            if self.head < len(self.tape):
                if self.tape[self.head] == '0':
                    self.state = 'q0'  # Si encontramos otro 0, regresamos al estado q0
                # Mover el cabezal a la derecha
                self.head += 1
            else:
                self.state = 'halt'  # Detener si llegamos al final de la cinta

    def run(self):
        while self.state != 'halt':
            self.step()

    def is_even_zeros(self):
        return self.state == 'q0'  # Si terminamos en el estado q0, hay un número par de ceros

# Ejemplo de uso
input_string = "001100"  # Cambia esta cadena para probar diferentes entradas
tm = TuringMachine(input_string)
tm.run()

if tm.is_even_zeros():
    print("La cadena tiene un número par de ceros.")
else:
    print("La cadena tiene un número impar de ceros.")
