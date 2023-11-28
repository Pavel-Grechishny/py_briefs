"""Компоновщик"""

from typing import Self

class Neuron:
    
    def __init__(self, name: str):
        self.name = name
        self.inputs: list[Neuron] = []
        self.outputs: list[Neuron] = []
        
    def connect_to(self, other: Self):
        self.outputs.append(other)
        self.inputs.append(self)
        
    def __iter__(self):
        yield self
        
    def __str__(self):
        return f'<{self.name}>'
        
    def show_connections(self):
        res = '\tinputs:\n'
        res += '\n'.join(f'\t\t{neuron}' for neuron in self.inputs)
        res += '\n\toutputs:\n'
        res += '\n'.join(f'\t\t{neuron}' for neuron in self.outputs)
        return res


class NeuronLayer(list):
    
    def __init__(self, name: str, count: int = 2):
        super().__init__()
        self.name = name
        for i in range(1, count+1):
            self.append(Neuron(f'{self.name} Нейрон {i}'))

    def connect_to(self, other: Neuron | Self):
        if self is other:
            return
            
        for neuron_out in self:
            for neuron_in in other:
                neiron_out.connect_to(neuron_in)


# >>> n1 = Neuron('Отдельный нейрон 1')
# >>> n2 = Neuron('Отдельный нейрон 2')
# >>> n3 = Neuron('Отдельный нейрон 3')
# >>>
# >>> n2.connect_to(n1)
# >>> n3.connect_to(n1)
# >>>
# >>> n1.show_connections()
# '\tinputs:\n\n\toutputs:\n'
# >>> n2.show_connections()
# '\tinputs:\n\t\t<Отдельный нейрон 2>\n\toutputs:\n\t\t<Отдельный нейрон 1>'
# >>> n3.show_connections()
# '\tinputs:\n\t\t<Отдельный нейрон 3>\n\toutputs:\n\t\t<Отдельный нейрон 1>'

