"""CIS189 Python
Author: Greg Tarr
Created: 11/18/2019"""
from abc import ABC, abstractmethod


class Rider(ABC):

    @abstractmethod
    def ride(self):
        pass

    @abstractmethod
    def riders(self):
        pass


class Bicycle(Rider):

    def __init__(self):
        self.ride_type = 'Human powered'
        self.num_riders = 1

    def ride(self):
        return self.ride_type

    def riders(self):
        return self.num_riders

    def __str__(self):
        return f'{self.ride()} vehicle with {self.riders()} rider.'


class Motorcycle(Rider):

    def __init__(self):
        self.ride_type = 'Engine powered'
        self.num_riders = '1 or 2'

    def ride(self):
        return self.ride_type

    def riders(self):
        return self.num_riders

    def __str__(self):
        return f'{self.ride()} vehicle with {self.riders()} riders.'


class Car(Rider):

    def __init__(self):
        self.ride_type = 'Engine or Battery powered'
        self.num_riders = "Up to 5"

    def ride(self):
        return self.ride_type

    def riders(self):
        return self.num_riders

    def __str__(self):
        return f'{self.ride()} vehicle with {self.riders()} riders.'


if __name__ == '__main__':

    b = Bicycle()
    print(str(b))
    m = Motorcycle()
    print(str(m))
    c = Car()
    print(str(c))
