age = 16
has_ticket = True
with_adult = False
ticket_type = "student"

is_adult = age >= 18
can_enter = has_ticket and (is_adult or with_adult)
gets_discount = ticket_type == "student" or age < 12

print(f"Age {age}, adult: {is_adult}")
print(f"Has ticket: {has_ticket}, with adult: {with_adult}")
print(f"Can enter the late show: {can_enter}")
print(f"Gets a discount: {gets_discount}")
print(f"Needs an adult to come along: {not is_adult and not with_adult}")
