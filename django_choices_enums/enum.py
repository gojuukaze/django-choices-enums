__builtin_func__ = ['to_django_choice', 'anonymous', 'get_verbose']


def is_builtin(name) -> bool:
    return name.startswith('__') or name in __builtin_func__


class ChoiceItem(int):
    verbose = None


class DjangoChoiceEnumMeta(type):

    def __new__(cls, name, bases, attrs):
        return type.__new__(cls, name, bases, attrs)

    def __getattribute__(self, *args, **kwargs):
        name = args[0]
        r = super().__getattribute__(*args, **kwargs)
        if not is_builtin(name) and isinstance(r, tuple):
            foo = ChoiceItem(r[0])
            foo.verbose = r[1]
            return foo
        return r


class DjangoChoicesEnum(metaclass=DjangoChoiceEnumMeta):
    """
    django model choice的枚举

    Usage:

        class TypeChoices(DjangoChoicesEnum):
            Created = (1,'created')
            Finished = (2,'finished')

        class Foo(models.Model):
            type = models.IntegerField(choices=TypeChoices.to_django_choices())


        f = Foo()
        if f.type == TypeChoices.Created:
            pass



    """
    anonymous = ()

    @classmethod
    def to_django_choices(cls):
        r = []
        for k, v in cls.__dict__.items():
            if is_builtin(k):
                continue
            else:
                r.append(v)
        for a in cls.anonymous:
            r.append(a)
        return tuple(r)

    @classmethod
    def all_values(cls):
        r = []
        for k, v in cls.__dict__.items():
            if is_builtin(k):
                continue
            else:
                r.append(v[0])
        for a in cls.anonymous:
            r.append(a[0])
        return tuple(r)
    @classmethod
    def get_verbose(cls, value):
        for i in cls.to_django_choices():
            if i[0] == value:
                return i[1]
        return None
