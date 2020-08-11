from googlesearch import search

print("Google search: ", end = '')

search_string = input()

query = search_string

for i in search(query, tld="com", num=10, stop=10, pause=2):
    print(i)
