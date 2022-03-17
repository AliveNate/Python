

# ---------------------------------------------
class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def sayHello(self):
        print("Hi, my name is " + self.name)
# ------------------------------------------
# ------------------------------------------
class Person:
    def __init__(self, n, p, i):
        self.name = n
        self.personality = p
        self.is_sitting = i

    def sit_down(self):
        self.is_sitting = True
    def stand_up(self):
        self.is_sitting = False
# ------------------------------------------
# ------------------------------------------
# Create objects, using Robot class
r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)
# -----------------------------
# Create objects using Person class
p1 = Person("Alice", "Aggressive", False)
p2 = Person("Becky", "Talkative", True)
# ------------------------------
# Call Robot class function, through individual object.
r1.sayHello() # Hi, my name is Tom
r2.sayHello() # Hi, my name is Jerry
# -----------
# -----------
# Show p1 owns r2, p2 owns r1
# This is a Person, new attribute, not stated in class.
p1.robot_owned = r2
p2.robot_owned = r1
# -----------------
# We can still call Robot functions, even from new Person attribute.
print("--------------------")
p1.robot_owned.sayHello() # Hi, my name is Jerry