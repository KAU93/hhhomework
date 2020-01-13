class Car:
    # Реализовать класс машины Car, у которого есть поля: марка и модель автомобиля
    # Поля должны задаваться через конструктор
    def __init__(self, mark, model):
        self.mark = mark
        self.model = model


class Garage:
    # Написать класс гаража Garage, у которого есть поле списка машин
    # Поле должно задаваться через конструктор
    # По аналогии с классом Company из лекции реализовать интерфейс итерируемого
    # Реализовать методы add и delete(удалять по индексу) машин из гаража
    def __init__(self, listCar):
        if type(listCar) == type([]):
            self.listCar = listCar
        else:
            print("Передан не правильный тип данных")
            exit
    
    def __len__(self):
        return len(self.listCar)

    def __getitem__(self, position):
        return self.listCar[position]

    def add(self, car):
        self.listCar.append(car)
    
    def delete(self, index):
        del self.listCar[index]
