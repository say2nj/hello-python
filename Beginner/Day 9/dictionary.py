var = {"Bug": "An error in a program.", "Function": "A piece of code that you can easily call over and over again."}
print("Length: ", len(var))
print("Type: ", type(var))

# Adding an item to existing dictionary
print("Adding an item to existing dictionary")
var["Loop"] = "The action of doing something over and over again."

print("Length: ", len(var))
print("Type: ", type(var))
print(var)
print(var["Loop"])
# print(var["bug"]) # KeyError
print(var.get("Bug"))

key = var.keys()
# print(key)    o/p- dict_keys(['Bug', 'Function', 'Loop'])
for i in key:
    print(i)
    print(var[i])
# print(var.keys()) o/p- dict_keys(['Bug', 'Function', 'Loop'])

value = var.values()
for i in value:
    print(i)

# Removing item
var.pop("Bug")
print(var.items())

var.update({"Bug": "An error in a program."})
print(var)
print(var.popitem())

for x in var:
    print(x)

[print(x) for x in var]

capitals = {"France": {"cities_visited" :["Paris", "Lille", "Dijon"], "total_visits": 12},
            "Germany": {"cities_visited" :["Berlin","Hamburg","Stuttgart"]}, "total_visits": 15}
print(capitals["France"]["total_visits"])

capitals = [{"country": "France", "cities_visited" :["Paris", "Lille", "Dijon"], "total_visits": 12},
            {"country": "Germany", "cities_visited" :["Berlin","Hamburg","Stuttgart"], "total_visits": 15}]

print(capitals[1]["country"])

starting_dictionary = {"a":9,"b":8}
final_dictionary = starting_dictionary["c"] =7

print(starting_dictionary, final_dictionary)

for key in starting_dictionary:
    starting_dictionary[key] += 1
print(starting_dictionary)