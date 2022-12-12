import wikipedia

words = ['c++']

for word in words:
    urls = wikipedia.page(word).references
    txt = '\n'.join(urls)
    with open('readme.txt', 'a') as f:
        f.write(txt)
    print(len(urls))
