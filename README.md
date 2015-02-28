# Worder
Calculate possible words and corresponding points in *Scrabble* for given letters.

```
$ python worder.py
Enter letters: abcdef*  # "*" for blank character
Enter language (en):
Enter regex (optional):^m.*$  # Apparently there is an "m" on the board and we want to use it.
mazed  -  17  points
madefy  -  15  points
maze  -  15  points
max  -  12  points
maybe  -  12  points
mack  -  12  points
mafic  -  12  points
malfed  -  12  points
macled  -  11  points
medoc  -  10  points
mobed  -  10  points
madoc  -  10  points
make  -  10  points
meak  -  10  points
medic  -  10  points
madge  -  9  points
macle  -  9  points
mabel  -  9  points
macer  -  9  points
mwa  -  8  points
mew  -  8  points
...

```

# Word Sources

* English: /usr/share/dict/words :) (lowercased)
* Turkish: [zemberek](https://code.google.com/p/zemberek/downloads/detail?name=full.txt.tr.tar.gz&can=2&q=)
