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
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
