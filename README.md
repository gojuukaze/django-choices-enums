# django-choices-enums
The enum type used for Django choices enables Django's choices to support code prompts!!  
 
用于django choices的枚举类型，使得django的choices支持代码提示！！   

* doc : https://github.com/gojuukaze/django-choices-enums#Usage

# feature

* the human-readable name of choices not missing. 不缺失 choices 的可读说明
* code hints. 能支持代码提示
* Lightweight, easy to use. 方便使用、轻量、无侵入

# 依赖

* python3+

# Installation
``` 
pip install django-choices-enums
```


# Usage

```python
from django_choices_enums import DjangoChoicesEnum

class TypeChoices(DjangoChoicesEnum):
    Created = (1,'created')
    Finished = (2,'finished')

class Foo(models.Model):
    type = models.IntegerField(choices=TypeChoices.to_django_choices())

```

* use enum like this:

```python
f = Foo.create(type=TypeChoices.Created)

```

* get all values:

```python
print(TypeChoices.all_values())
# Out: (1, 2) 
```

* anonymous values:

```python
from django_choices_enums import DjangoChoicesEnum

class MyEnum(DjangoChoicesEnum):
    A = (1, 'xxx')
    B = (2, 'xxx')

    anonymous = ((3, 'xx'),
                 (4, 'xx'),
                 )

print(MyEnum.to_django_choices())
# Out: ((1, 'xxx'), (2, 'xxx'), (3, 'xx'), (4, 'xx'))
```

* get verbose:

```python
from django_choices_enums import DjangoChoicesEnum

class MyEnum(DjangoChoicesEnum):
    A = (1, 'A ...')
    B = (2, 'B ...')

    anonymous = ((3, '33'),
                 (4, '44'),
                 )
print(MyEnum.A.verbose)
# Out: A ...
print(MyEnum.get_verbose(2))
# Out: B ...
print(MyEnum.get_verbose(3))
# Out: 33
print(MyEnum.get_verbose(MyEnum.B))
# Out: B ...

```
