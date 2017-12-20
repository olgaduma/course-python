def song(word=3, count=3, wow=0):
    if wow == 1:
        print(word*count, '!')
    else:
        print(word*count, '.')
print(song(word='la', count=4, wow=1), sep='-')