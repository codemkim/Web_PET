from django import template
from django.templatetags.static import StaticNode

register = template.Library()


class CustomStaticNode(StaticNode):
    # StaticNode를 상속 받아 StaticNode에서 만들어진 url에다가 해당 쿼리스트링을 넣는다
    # 배포시 뒤에 버전을 바꾸어 사용
    def url(self, context):
        path = super().url(context) + '?version=1.0.0'
        return path


@register.tag('static')
def do_static(parser, token):
    # StaticNode를 상속받은 CustomStaticNode객체를 사용하여 StaticNode의 handle_token을 사용
    node = CustomStaticNode.handle_token(parser, token)
    return node