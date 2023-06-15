# from turtle import *
# import turtle
# t = turtle.Turtle()
# Window = turtle.Screen()
#
# Window.bgcolor('white')
#
# turtle.color('white')
# goto(-200, -200)
# def serp_tri(side, level):
#     if level == 1:
#         for i in range(3):
#             turtle.color('black')
#             turtle.ht()
#             turtle.fd(side)
#             turtle.left(120)
#             turtle.speed(100000)
#     else:
#         turtle.ht()
#         serp_tri(side / 2, level - 1)
#         turtle.fd(side / 2)
#         serp_tri(side / 2, level - 1)
#         turtle.bk(side / 2)
#         turtle.left(60)
#         turtle.fd(side / 2)
#         turtle.right(60)
#         serp_tri(side / 2, level - 1)
#         turtle.left(60)
#         turtle.bk(side / 2)
#         turtle.right(60)
#         turtle.speed(100000000000)
#
# def main():
#     serp_tri(400, 8)

def fill_massive(a, u):
    return add_number(a, u)


def add_number(a, u):
    a.append(u)
    return a

def abc():
    return "arv on massivis"

def number_of_cars(all_cars: str) -> list:
    """
    Create a list of tuples with make quantities.

    The result is a list of tuples.
    Each tuple is in the form: (make_name: str, quantity: int).
    The order of the tuples (makes) is the same as the first appearance in the list.
    """
    cars_and_models_in_string = all_cars.split(",")
    all_marks = []
    result = []
    for element in cars_and_models_in_string:
        cars_and_models_in_list = element.split(" ")
        mark = cars_and_models_in_list[0]
        if mark not in all_marks:
            all_marks.append(mark)
    for mark in all_marks:
        counter = 0
        for element in cars_and_models_in_string:
            cars_and_models_in_list = element.split(" ")
            if cars_and_models_in_list[0] == mark:
                counter += len(cars_and_models_in_list) - 1
        result.append((mark, counter))
    return result

def add_cars(car_list: list, all_cars: str) -> list:
    """
    Add cars from the list into the existing car list.

            The first parameter is in the same format as the output of the previous function.
            The second parameter is a string of comma separated cars (as in all the previous functions).
            The task is to add cars from the string into the list.

            Hint: This and car_make_and_models are very similar functions. Try to use one inside another.


            and
            "Audi A6,BMW A B C,Audi A4"

            =>

            [['Audi', ['A4', 'A6']], ['Skoda', ['Superb']], ['BMW', ['A B C']]]
            """
    all_cars_in_list = [[car.split(" ")[0], car.split(" ")[1:len(car)]] for car in all_cars.split(",")]

    print(all_cars_in_list)
    if len(car_list) != 0:
        cars = []
        for element in range(len(car_list)):
            cars.append(car_list[element][0])
        for car in all_cars_in_list:
            if car[0] in cars:
                element = cars.index(car[0])
                for model1 in car[1]:
                    if model1 not in car_list[element][1]:
                        car_list[element][1].append(model1)
            else:
                car_list.append(car)
    return car_list


def new_fun(a: list):
    u = list(set(a))
    u.sort(reverse=True)
    for e in u:
       if a.count(e) <= 1:
            continue
       else:
            return e


if __name__ == '__main__':
    a = [1,1,2,1,1,1,2,3]
    print(new_fun(a))