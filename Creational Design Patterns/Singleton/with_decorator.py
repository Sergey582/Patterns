def singleton(class_):
    instances_ = {}

    def filter(*args, **kwargs):
        if class_ not in instances_:
            instances_[class_] = class_(*args, **kwargs)
        return instances_[class_]

    return filter


@singleton
class Singleton:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
