def tacofy(word):
    taco_bell_dict = {'a':'beef', 'e':'beef', 'i':'beef', 'o':'beef', 'u':'beef', 'l':'lettuce', 't':'tomato', 'g':'guacamole', 'c':'cheese','s':'salsa'}
    my_taco = []
    word_lower = word.lower()
    if len(word_lower) > 0:
    	for char in range(0, len(word_lower)):
    		current_char = word_lower[char]
    		if current_char in taco_bell_dict.keys():
    			my_taco.append(taco_bell_dict[current_char])
    my_taco = ['shell'] + my_taco + ['shell']
    return my_taco

print tacofy("asdfAsd")
