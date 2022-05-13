from django import template

register = template.Library()


@register.filter(name='add_class')
def add_class(value, arg):
    return value.as_widget(attrs={'class': arg})


@register.filter(name="get_verbose_name")
def get_verbose_name(model, field):
    return model._meta.get_field(field).verbose_name
