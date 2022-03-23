from threading import Timer

'''A threading.Timer is a way to schedule a function to be called after a certain amount of time has passed. You create a Timer by passing in a number of seconds to wait and a function to call:'''
def my_function():
    print("My function")

t = Timer(5.0, my_function)
t.start()