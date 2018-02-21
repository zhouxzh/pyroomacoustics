'''
CMU ARCTIC Corpus
=================

Pyroomacoustics includes a wrapper around the popular CMU ARCTIC corpus [1]
that can be handy in some situations. Here is a quick rundown of how
to use it.

The CMU ARCTIC database is open and can be downloaded automatically as demonstrated here.

[1] J. Kominek and A. W. Black, CMU ARCTIC: databases for speech synthesis, Tech. Rep., CMU, 2003.
'''

import pyroomacoustics as pra
import os, argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Example of using the CMUArcticCorpus wrapper')
    parser.add_argument('--noplot', action='store_true',
            help='Do not display any plot')
    parser.add_argument('--playsound', action='store_true',
            help='Play one example sentence')
    args = parser.parse_args()

    # Download the corpus, be patient
    corpus = pra.datasets.CMUArcticCorpus(download=True, speakers=['bdl'])

    # the corpus is split between train and test
    # let's pick a sentence from each
    print('A couple of sentences:')
    print(corpus.sentences[0])
    print(corpus.sentences[100])

    # let's find all the sentences from male speakers in the training set
    keyword = 'what'
    matches = list(filter(lambda x: keyword in x.text, corpus.sentences))
    print('The number of sentences containing "{}": {}'.format(keyword, len(matches)))
    for s in matches:
        print('  *', s)

    # play sound if required
    if args.playsound:
        matches[0].play()

    # show the spectrogram
    if not args.noplot:
        import matplotlib.pyplot as plt
    
        plt.figure()
        matches[0].plot()

        plt.show()
