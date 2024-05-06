from django import template

register = template.Library()


@register.inclusion_tag('mail/email.html')
def load_email_form(form):
    return {'form': form}
