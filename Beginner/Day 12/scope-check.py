enemies = 1
print("Global Scope", enemies)

def increase_enemies():
    global enemies
    enemies = 2

    print("Local Scope", enemies)

increase_enemies()

print("Global Scope", enemies)

# Block Scope - Not in Python
game_level = 3
enemies = ["Skeleton","Zombies"]
if game_level == 3:
    new_enemy = enemies[0]
print(new_enemy)

#Comment line 15 to 19 before running line 22 to 27
game_level = 3
def create_enemy():
    enemies = ["Skeleton","Zombies"]
    if game_level == 3:
        new_enemy = enemies[0]
        print(new_enemy)

# print(new_enemy) - error- new_enemy not defined
create_enemy()


enemies = 1
print("Global Scope", enemies)

def increase_enemies():
    print("Local Scope", enemies)
    return enemies +1



enemies = increase_enemies()

print("Global Scope", enemies)
