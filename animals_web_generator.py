import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

with open("animals_template.html", "r", encoding="utf-8") as file:
    html_content = file.read()

output_str = ''
for animal in animals_data:
    output_str += f"Name: {animal['name']}\n"
    output_str += f"Diet: {animal['characteristics']['diet']}\n"
    output_str += f"Location: "
    for i in range(len(animal['locations'])):
        output_str += f"{animal['locations'][i]}"
        if len(animal['locations']) > 1:
           output_str += ", "
    output_str += "\n"
    animal_type = animal['characteristics'].get('type')
    if animal_type:
       output_str += f"Type: {animal_type}\n"
    output_str += "\n"

new_page = html_content.replace("__REPLACE_ANIMALS_INFO__", output_str)
print(new_page)

with open("animals.html", "w", encoding="utf-8") as file:
    html_content = file.write(new_page)