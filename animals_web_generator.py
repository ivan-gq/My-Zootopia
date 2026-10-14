import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(data):
    '''Generate serialized HTML tags per animal
    '''
    output_str = ''
    output_str += '<li class="cards__item">\n'
    output_str += f'\t<div class="card__title"> {data['name']}</div>\n'
    output_str += '\t<div class="card__text">\n'
    output_str += '\t\t<ul>\n'
    output_str += f"\t\t\t<li><strong>Diet:</strong> {data['characteristics']['diet']}</li>\n"
    output_str += f"\t\t\t<li><strong>Location: </strong>"
    for i in range(len(data['locations'])):
        output_str += f"{data['locations'][i]}"
        if len(data['locations']) > 1:
            output_str += ", "
    output_str += "</li>\n"
    animal_type = data['characteristics'].get('type')
    if animal_type:
        output_str += f"\t\t\t<li><strong>Type: </strong>{animal_type}</li>\n"
    output_str += "\t\t</ul>\n\t</div>\n</li>\n"
    return output_str


def main():
    '''Main fucntion'''
    animals_data = load_data('animals_data.json')

    with open("animals_template.html", "r", encoding="utf-8") as file:
        html_content = file.read()

    output_str = ''
    for animal in animals_data:
        output_str += serialize_animal(animal)

    new_page = html_content.replace("__REPLACE_ANIMALS_INFO__", output_str)

    with open("animals.html", "w", encoding="utf-8") as file:
        html_content = file.write(new_page)


if __name__ == "__main__":
    main()
