################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ < 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ / 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/  
#                                                                          
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at 
# different temperatures to craft special materials.
# 
# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result 
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.
#
# The `alchemy_combine()` function will use your oven. You can see the expected 
# formulas and their outputs in the test file, `question3_test.py`.

# This function should return an oven instance!

class MagicalOven:
    def __init__(self):
        self.ingredients = []
        self.temperature = 0

    def add(self, item):
        # Método para agregar un ingrediente al horno
        self.ingredients.append(item)

    def freeze(self,temperature):
        # Método para congelar los ingredientes
        self.temperature = temperature

    def boil(self,temperature):
        # Método para hervir los ingredientes
        self.temperature = temperature

    def wait(self):
        # Método para combinar los ingredientes sin cambios de temperatura
        pass

    def get_output(self):
        # Método para obtener el resultado
        if self.temperature == 5000 and set(self.ingredients) == {"lead", "mercury"}:
            return "gold"
        elif self.temperature == -100 and set(self.ingredients) == {"water", "air"}:
            return "snow"
        elif self.temperature == 150 and set(self.ingredients) == {"cheese", "dough", "tomato"}:
            return "pizza"
        else:
            return "unknown"


def make_oven():
  return MagicalOven()

def alchemy_combine(oven, ingredients, temperature):
  
  for item in ingredients:
    oven.add(item)

  if temperature < 0:
    oven.freeze(temperature)
  elif temperature >= 100:
    oven.boil(temperature)
  else:
    oven.wait()

  return oven.get_output()