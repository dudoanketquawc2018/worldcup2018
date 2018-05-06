from django.template import Library
register = Library()
@register.filter
def running_total(summary):
     return - sum([sumuser.total_reward for sumuser in summary])