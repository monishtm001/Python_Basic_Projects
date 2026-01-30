# import turtle

# screen = turtle.Screen()
# screen.title("Turtle Test")

# spinny = turtle.Turtle()
# spinny.shape("turtle")

# spinny.forward(100)

# turtle.done()

from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["Name", "Breakfast", "Dinner", "Night Wash"]
table.add_column("Name", ["Adelaide", "Brisbane", "Darwin", "Hobart", "Sydney", "Melbourne", "Perth"])
print(table)
table.align = "r"
print(table)