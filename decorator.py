# Q6. Decorator - Function Execution

# Creating a decorator
def execution_time(fn):

    def wrapper(n):
        print("Execution is started....")

        fn(n)

        print("Execution finished !!!")

    return wrapper


# Applying decorator
@execution_time
def fact(n):

    f = 1

    for i in range(n, 1, -1):
        f *= i

    print(f)


# Function call
fact(5)