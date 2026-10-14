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
    output_str += '<li class="cards__item">'
    output_str += f"Name: {animal['name']}<br/>\n"
    output_str += f"Diet: {animal['characteristics']['diet']}<br/>\n"
    output_str += f"Location: "
    for i in range(len(animal['locations'])):
        output_str += f"{animal['locations'][i]}"
        if len(animal['locations']) > 1:
           output_str += ", "
    output_str += "<br/>\n"
    animal_type = animal['characteristics'].get('type')
    if animal_type:
       output_str += f"Type: {animal_type}<br/>\n"
    output_str += "<br/></li>\n"

new_page = html_content.replace("__REPLACE_ANIMALS_INFO__", output_str)
print(new_page)

with open("animals.html", "w", encoding="utf-8") as file:
    html_content = file.write(new_page)