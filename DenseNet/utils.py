#!/usr/bin/env python

def load_dict(dictFile):
    with open(dictFile) as fp:
        stuff=fp.readlines()
    lexicon={}
    for l in stuff:
        w=l.strip().split()
        lexicon[w[0]]=int(w[1])

    print('total words/phones',len(lexicon))
    return lexicon

worddicts = load_dict('lexicon.txt')
worddicts_r = [None] * len(worddicts)
for kk, vv in worddicts.items():
    worddicts_r[vv] = kk
