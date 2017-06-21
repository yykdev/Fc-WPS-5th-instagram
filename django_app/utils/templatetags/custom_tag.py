from django import template

register = template.Library()

@register.filter
def query_string(q):
    # value에는 QueryDict가 옴
    # ret = '?'
    # for k, v_list in q.lists():
    #     for v, v_list in v_list:
    #         ret += '&{}={}'.format(k, v)

    ret = '?' + '&'.join(['{}={}'.format(k, v) for k, v_list in q.lists() for v in v_list])
    return ret