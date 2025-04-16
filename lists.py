# list

# l1 = [1,2,3,4,5]
# l2 = ['a','b','c']
# l3 = [1,'a',False]

# amazon_cart = [
#     'notebook', 
#     'sunglass',
#     'toy',
#     'grape'
#     ]

# amazon_cart.append('gum')

# print(amazon_cart)

# matrix

# matrix = [
#     [1,0,1],
#     [0,1,0],
#     [1,0,1]
# ]

# print(matrix[0][1])

# list methods

basket = [1,2,3,4,5]

#  adding

basket.append(6)
basket.insert(3, 3.5)
basket.extend([7,8])
basket.pop()
basket.remove(3.5)
# basket.clear()
basket.index(2)

print(basket)
print(9 if 2 in basket else 'nope')

not_sorted = ['b', 'e', 'y', 'x', 'm', 'a']
not_sorted.sort(reverse=True)
print(not_sorted)
