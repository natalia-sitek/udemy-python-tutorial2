st = 'Print only the words that start with s in this sentence'
slowa = st.split(' ')
print(slowa)

for item in slowa:
    if item.startswith('s'):
        print(item)

numbers = range(0, 10)
for liczba in numbers:
    if liczba % 2 == 0:
        print(liczba)

listcomprehension = [x for x in range(1, 50) if x % 3 == 0]
print(listcomprehension)

sentence = 'Print every word in this sentence that has an even number of letters'
for word in sentence.split(' '):
    if word.__len__() % 2 == 0:
        print("even")
st = 'Create a list of the first letters of every word in this string'
first_letters = [x[0] for x in st.split(' ')]
print(first_letters)
