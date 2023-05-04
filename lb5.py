import random

class Passenger:
    def __init__(self, id):
        self.id = id

class Tram:
    def __init__(self, capacity, stops):
        self.capacity = capacity
        self.stops = stops
        self.passengers = []

    def add_passenger(self, passenger):
        if len(self.passengers) < self.capacity:
            self.passengers.append(passenger)

    def remove_passenger(self, passenger):
        if passenger in self.passengers:
            self.passengers.remove(passenger)

# Згенерувати кілька пасажирів
passengers = [Passenger(i+1) for i in range(300)]

# Створити трамвай місткістю 30 пасажрів та 10 зупинок
tram = Tram(30, 10)

# Імітація пасажирів, що заходять та виходять з трамваю на кожній зупинці
for stop in range(tram.stops):
    # Посадка пасажирів
    passengers_to_board = random.sample(passengers, random.randint(0, tram.capacity - len(tram.passengers)))
    for passenger in passengers_to_board:
        tram.add_passenger(passenger)
        passengers.remove(passenger)

    # Пасажири виходять
    passengers_to_exit = random.sample(tram.passengers, random.randint(0, len(tram.passengers)))
    for passenger in passengers_to_exit:
        tram.remove_passenger(passenger)

    # Вивести кількість пасажирів у трамваї на кожній зупинці
    print(f"На зупинці {stop + 1} {len(tram.passengers)} пасажирів у трамваї.")

print("Кінець симуляції")
