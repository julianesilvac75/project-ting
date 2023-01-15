import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    list = txt_importer(path_file)

    for i in range(len(instance)):
        if instance.search(i)["nome_do_arquivo"] == path_file:
            return None

    file_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(list),
        "linhas_do_arquivo": [line for line in list]
    }

    instance.enqueue(file_dict)

    print(file_dict)


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos")
    else:
        file = instance.search(0)
        instance.dequeue()
        print(f"Arquivo {file['nome_do_arquivo']} removido com sucesso")


def file_metadata(instance, position):
    try:
        file = instance.search(position)
        print(file)

    except IndexError:
        print("Posição inválida", file=sys.stderr)
