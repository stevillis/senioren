## Dev Instructions

### Django

- makemigrations

```shell
python manage.py makemigrations
```

- migrate

```shell
python manage.py migrate
```

- runserver

```shell
python manage.py runserver
```

---

### Translation

1. Gererate translations

```shell
python .\manage.py makemessages -l pt_BR -l en -i *.txt
```

2. Edit the .po files with Poedit

3. Compile the translations

```shell
python manage.py compilemessages
```
