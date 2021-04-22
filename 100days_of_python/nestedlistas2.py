linha1 = ["𓀖", "𓀖", "𓀖"]
linha2 = ["𓀖", "𓀖", "𓀖"]
linha3 = ["𓀖", "𓀖", "*"]

map = [linha1, linha2, linha3]
print(f"{linha1}\n{linha2}\n{linha3}")

position = input("Where do yuo want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])
#selected_row = map[vertical - 1]
#selected_row[horizontal -1]= "X"

map[vertical - 1][horizontal - 1] = "X"

print(f"{linha1}\n{linha2}\n{linha3}")
