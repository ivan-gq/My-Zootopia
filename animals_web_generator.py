import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

print(len(animals_data))

for animal in animals_data:
    print(f"Name: {animal['name']}")
    print(f"Diet: {animal['characteristics']['diet']}")
    print(f"Location: ", end="")
    for i in range(len(animal['locations'])):
        print(f"{animal['locations'][i]}", end="")
        if len(animal['locations']) > 1:
           print(", ", end="")
    print()
    animal_type = animal['characteristics'].get('type')
    if animal_type:
       print(f"Type: {animal_type}")
    print()
#   if animal['characteristics']['type']:
#     print(f"Type: {animal['characteristics']['type']}")