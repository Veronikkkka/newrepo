def dyvo_insert(sentence, flag):
    """
    str, str -> str
    Inserting word "диво" before every word that starts with flag.

    >>> dyvo_insert("Кит кота по хвилях катав - кит у воді, кіт на киті", "ки")
    Диво кит кота по хвилях катав - диво кит у воді, кіт на диво киті
    """
    sentence_res = ""
    start_num = 0
    sentence = sentence.lower()
    # flag = sentence.lower()
    for i in sentence:
        # print(start_num)
        index = sentence.find(flag.lower(), start_num)
        # print(index)
        if index != -1:
            # print(start_num)
            for j in range(start_num, index):
                # print(sentence[j], index)
                sentence_res += sentence[j]
            sentence_res += "диво " + flag
            start_num = index + len(flag)

        else:
            break

    index_last = sentence.rfind(flag)
    # print(index_last, sentence[index_last])
    for j in range(index_last+len(flag), len(sentence)):
        sentence_res += sentence[j]
    print(sentence_res.capitalize())
dyvo_insert("Кит кота по хвилях катав - кит у воді, кіт на киті", "ки")
