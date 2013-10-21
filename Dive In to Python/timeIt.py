import timeit
t = timeit.Timer("soundex.soundex('Pilgrim')","import soundex")
t.timeit()
t.repeat(3,2000000)
