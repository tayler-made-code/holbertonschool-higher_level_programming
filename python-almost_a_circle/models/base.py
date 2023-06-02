#!/usr/bin/python3
''' Base class for all other classes '''


class Base:
    ''' Base class for all other classes '''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' Construction Junction, What's your function! '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' returns JSON srting representation of list_dictionaries '''
        import json
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' writes JSON string representation of list_objs to a file '''
        import json
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = []
                for obj in list_objs:
                    list_dicts.append(obj.to_dictionary())
                file.write(Base.to_json_string(list_dicts))
