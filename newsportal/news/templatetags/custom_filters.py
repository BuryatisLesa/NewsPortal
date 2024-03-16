from django import template



register = template.Library()



@register.filter()
def censor(value, word='Геология'):
   w = value.split()
   for i, text in enumerate(w):
      if text == word:
         w[i] = text[0] + ('*' * (len(word) - 1))
   return ' '.join(w)

