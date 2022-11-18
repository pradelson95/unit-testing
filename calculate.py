
def add(Num1, Num2):

  return Num1 + Num2
  

def subtract(Num1, Num2):

  return Num1 - Num2
  

def multiply(Num1, Num2):

  return Num1 * Num2


def divide(Num1, Num2):

  if Num2 == 0:
    raise ZeroDivisionError("cannot divide by zero!")

  return Num1 // Num2 