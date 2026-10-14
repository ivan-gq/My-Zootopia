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
    output_str += '<li class="cards__item">\n'
    output_str += f'\t<div class="card__title"> {animal['name']}</div>\n'
    output_str += '\t<p class="card__text">\n'
    output_str += f"\t\t<strong>Diet:</strong> {animal['characteristics']['diet']}<br/>\n"
    output_str += f"\t\t<strong>Location: </strong>"
    for i in range(len(animal['locations'])):
        output_str += f"{animal['locations'][i]}"
        if len(animal['locations']) > 1:
           output_str += ", "
    output_str += "<br/>\n"
    animal_type = animal['characteristics'].get('type')
    if animal_type:
       output_str += f"\t<strong>Type: </strong>{animal_type}<br/>\n"
    output_str += "\t</p>\n</li>\n"

new_page = html_content.replace("__REPLACE_ANIMALS_INFO__", output_str)
print(output_str)

with open("animals.html", "w", encoding="utf-8") as file:
     html_content = file.write(new_page)