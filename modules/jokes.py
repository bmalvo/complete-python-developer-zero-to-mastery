import pyjokes # type: ignore

joke = pyjokes.get_joke('pl', 'neutral')
print(joke)