#user ip
cars={}
cars["id"]=input("enter key model number:")
cars["color"]=input("Enter colour:")
cars["price"]=input("Enter price of car:")
cars["carsname"]=input("Enter car Name:")
print(cars)

print(cars["color"])

#----------------------------------------------------------------

players={
    "virat":99,
    "dhoni":97,
    "rohit":98,
    "sachin":100,
    "hardik":50
}
print(players)
max_score=0
name=""
for score in players.values():
    if score>max_score:
        max_score=score
print(max_score)

for player, score in players.items():
    if score > max_score:
        max_score = score
        name = player

print(f"Top performer is {name} & score is {max_score}")
    