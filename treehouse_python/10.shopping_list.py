shopping_list = []

def show_help():
    print("O que você comprar?")
    print("""
    Digite "MOSTRAR" para ver os itens da lista
    Digite 'FIM' para parar de adicionar items.
    Digite "HELP' para ajuda
    """)


def add_to_list(item):
    shopping_list.append(item)
    print("Um item foi adicionado!! Há {} item(s) na lista de compras".format(len(shopping_list)))

def show_list():
    print("Aqui está sua lista: ")
    for item in shopping_list:
        print(item)


show_help()
while True:
    new_item = input("> ")

    if new_item == "FIM":
        break
    elif new_item == "HELP":
        show_help()
        continue
    elif new_item == "MOSTRAR":
        show_list()
        continue
    add_to_list(new_item)
show_list()