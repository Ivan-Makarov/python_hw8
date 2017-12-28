def get_cook_book(link):
    cook_book = {}
    with open(link, encoding='utf8') as recipes:
        for line in recipes:
            dish = line.strip().lower()
            ingredients = []
            ingredients_count = int(recipes.readline())
            for i in range(0, ingredients_count):
                ingredient = recipes.readline().strip().split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient[0],
                    'quantity': int(ingredient[1]),
                    'measure': ingredient[2]
                    })
            cook_book[dish] = ingredients
            recipes.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count, cookbook):
    shop_list = {}
    cook_book = get_cook_book(cookbook)
    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_shop_list_item = dict(ingredient)

            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingredient_name'], shop_list_item['quantity'], shop_list_item['measure']))


def create_shop_list(cookbook):
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count, cookbook)
    print_shop_list(shop_list)


create_shop_list('recipes.txt')
