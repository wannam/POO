

from car import Car
from person import Person
from color import Color
from engine import Engine
import pickle

list_of_persons = []
list_of_engines = []
list_of_cars = []
list_of_colors = []

def main():

    global list_of_persons
    global list_of_engines
    global list_of_cars
    global list_of_colors

    while True:
    

        print("Menu")
        print("1 - New Person")
        print("2 - List Persons")

        print("3 - New Engine")
        print("4 - List Engines")

        print("5 - New Color")
        print("6 - List Colors")

        print("7 - New Car")
        print("8 - List Cars")

        print("S - Save lists")
        print("L - Load lists")


        op = input("Op? ").lower()

        match op:
            case "1":
                firstname = input('First name: ').capitalize()
                lastname = input('Last name: ').capitalize()
                address = input('Address: ')
                cc = input('CC: ')
                phone = input('Phone Number: ')
                personid = (len(list_of_persons)) + 1
                new_person = Person(firstname, lastname, address, cc, phone, personid)
                list_of_persons.append(new_person)

            case "2":
                print_list(list_of_persons)
                print(list_of_persons[0].__dict__)

            case "3":
                fuel = input('Fuel: ')
                power = input('Horsepower: ')
                torque = input('Torque: ')
                displacement = input('Displacement: ')
                clylinders = input('Number clylinders: ')
                system = input('Starting system: ')
                weight = input('Weight: ')
                manufacturer = input('Manufacturer: ')
                engineid = f'{(len(list_of_engines)) + 1}'
                new_engine = Engine(fuel, power, torque, displacement, clylinders, system, weight, manufacturer, engineid)
                list_of_engines.append(new_engine)

            case "4":
                print_list(list_of_engines)

            case "5":
                namecolor = input('Color: ')
                rgb = int(input('RGB: '))
                colorid = f'{(len(list_of_colors)) + 1}'
                new_color = Color(namecolor, rgb, colorid)
                list_of_colors.append(new_color)

            case "6":
                print_list(list_of_colors)
                print('d - Delete item in list')
                print('e - Edit item in list')
                print('enter - exit list')
                ask = input('(d, e): ')
                if ask == 'd':
                    delete_fromlist(list_of_colors)
                elif ask == 'e':
                    edit_list(list_of_colors)
                else:
                    continue

            case "7":
                new_vehicle()

            case "8":
                print_list(list_of_cars)

            case "s":
                with open("persons_list.pkl", "wb") as f:
                    pickle.dump(list_of_persons, f)
                with open("colors_list.pkl", "wb") as f:
                    pickle.dump(list_of_colors, f)
                with open("engines_list.pkl", "wb") as f:
                    pickle.dump(list_of_engines, f)
                with open("cars_list.pkl", "wb") as f:
                    pickle.dump(list_of_cars, f)
                print('Lists saved')

            case "l":
                with open("persons_list.pkl", "rb") as f:
                    list_of_persons = pickle.load(f)
                with open("colors_list.pkl", "rb") as f:
                    list_of_colors = pickle.load(f)
                with open("engines_list.pkl", "rb") as f:
                    list_of_engines = pickle.load(f)
                with open("cars_list.pkl", "rb") as f:
                    list_of_cars = pickle.load(f)
                print('Lists loaded')



def print_list(list_of):
    i = 1
    if list_of == list_of_colors:
        for cores in list_of_colors:
            print(f'{i} - {cores}')
            i += 1
    if list_of == list_of_persons:
        for person in list_of_persons:
            print(f'{i} - {person}')
            i += 1
    if list_of == list_of_engines:
        for engine in list_of_engines:
            print(f'{i} - {engine}')
            i += 1
    if list_of == list_of_cars:
        for car in list_of_cars:
            print(f'{i} - {car}')
            i += 1
    
        



def ask_id(msg, input_list):
    
    print_list(input_list)
    while True:
        try:
            id = int(input(msg))
            if id in input_list:
                return id
            else:
                print("Invalid id. Please enter one of the following:")
                print_list(input_list)
        except ValueError:
            print("Invalid input. Please enter a number.")


def new_vehicle():
    person_id = ask_id("Person id? ", list_of_persons)
    color_id = ask_id("What is the Color? ", list_of_colors)
    engine_id = ask_id("Engine id? ", list_of_engines)
    brand = input('Brand: ')
    model = input('Model: ')
    consumption = float(input('Consumption: '))
    kms = float(input('KMS: '))

    new_car = Car(
        owner=list_of_persons[person_id],
        color=list_of_colors[color_id],
        engine=list_of_engines[engine_id],
        brand= brand,
        model= model,
        consumption= consumption,
        kms= kms
    )

    list_of_cars.append(new_car)

def delete_fromlist(del_list):
    print_list(del_list)
    delitem = int(input('choose item to delete: '))
    item = del_list[delitem]
    del del_list[item]



def edit_list(edit_list):
    if edit_list == list_of_colors:
        print_list(list_of_colors)
        edit_color = input('Choose item to edit: ')
        rgb = int(input('RGB: '))
        Color(edit_color, rgb)





        



    



# Only runs if this file is executed directly
if __name__ == "__main__":
    main()
