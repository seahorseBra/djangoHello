from django import template

import datetime

register = template.Library()


@register.filter
def cut2(value, arg='aaa'):
    return value.replace(arg, "")


class CurrentTimeNode(template.Node):
    def __init__(self, format_string):
        self.format_string = str(format_string)

    def render(self, context):
        now = datetime.datetime.now()
        return '当前时间:' + now.strftime(self.format_string)


@register.tag('current_time2')
def current_time2(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, format_string = token.split_contents()
    except ValueError:
        msg = '%r tag requires a single argument' % token.split_contents()[0]
        raise template.TemplateSyntaxError(msg)
    return CurrentTimeNode(format_string)


@register.simple_tag
def test_tag():
    return '围殴我噶尔窝工'

# library.filter('current_time2', do_current_time)
# library.filter('cut2', cut2)
