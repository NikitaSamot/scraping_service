from persons.models import Person, Color


def add_color():
    colors = ["Red, Green, Blue, Yellow"]
    person = Person.objects.get(id=1)
    for color_name in colors:
        color = Color.objects.create(name=color_name)
        person.favorite_colors.add(color)
        person.save()
