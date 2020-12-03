"""Basic tests for proxiwrap."""

import pandas as pd

SIMPLE_DATA = [
    [1, 'cat cat dog'],
    [2, 'cat dog dog'],
    [3, 'mouse cat cat'],
]
SIMPLE_DF = pd.DataFrame(SIMPLE_DATA, columns=['id', 'text'])

DATA = [
    [223, 'Janet was looking forward to eating some delicious snakes'],
    [8, 'I love to talk like a snake when meeting new people'],
    [3, 'Wow, all those snakes sure do look smart'],
    [92, 'My first love was a mummified snake discovered in Egypt'],
    [11, 'You better get this snake out of my sight!'],
    [55, 'The most sophisticated attack is the one including buttered snakes'],
    [34, 'We need more armored cats to help with this alien invasion!'],
    [12, 'I love going to armadillo parties'],
    [76, 'New York has a larger snake population then Toronto'],
]
DF1 = pd.DataFrame(DATA, columns=['id', 'text'])


def test_base_vocab_tests():
    print("Dataframe length: {}".format(len(DF1)))
