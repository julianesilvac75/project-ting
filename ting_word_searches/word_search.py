def exists_word(word, instance):
    result = []

    for file in instance.data:
        file_dict = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": []
        }

        for i in range(len(file["linhas_do_arquivo"])):
            if word.lower() in file["linhas_do_arquivo"][i].lower():
                file_dict["ocorrencias"].append({"linha": i + 1})

        if len(file_dict["ocorrencias"]):
            result.append(file_dict)

    return result


def search_by_word(word, instance):
    result = []

    for file in instance.data:
        file_dict = {
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": []
        }
        lines = file["linhas_do_arquivo"]

        for i in range(len(lines)):
            if word.lower() in lines[i].lower():
                file_dict["ocorrencias"].append({
                    "linha": i + 1, "conteudo": lines[i]
                })

        if len(file_dict["ocorrencias"]):
            result.append(file_dict)

    return result
