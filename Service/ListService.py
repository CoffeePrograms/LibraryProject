def get_index_by_item(lst, item):
    for i, e in enumerate(lst):
        if e.id == item.id:
            return i
    return -1


def get_index_by_id(lst, id_object):
    """
    Найти индекс объекта в списке по идентификатору

    :param lst: список
    :param id_object: идентификтор объекта
    :return: индекс объекта
    """
    for i, e in enumerate(lst):
        if e.id == id_object:
            return i
    return -1


def get_item_by_id(lst, id_object):
    """
    Найти объект по идентификатору

    :param lst: список
    :param id_object: идентификтор объекта
    :return: объект
    """
    for e in lst:
        if e.id == id_object:
            return e
    return None
