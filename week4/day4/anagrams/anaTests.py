from ana import anagrams
import test

@test.describe("anagrams")
def sample_tests():

    @test.it('The Smallest Possible Test')
    def smallest():
        subjects = ('apex',)
        alice = ('apex',)
        bob   = ('beak',)
        carol = ('cere',)
        dan   = ('defy',)
        memories = (alice, bob, carol, dan)
        players = (3, 0)
        expected = 0
        submitted = anagrams(subjects, memories, players)
        test.assert_equals(submitted, expected)

    @test.it('Everyone Goes First Once')
    def everybody():
        subjects = ('alef', 'late', 'ears', 'taws')
        dan   = ('eras', 'late', 'rase', 'tael')
        carol = ('sear', 'leaf', 'tale', 'teal')
        bob   = ('swat', 'taws', 'twas', 'wats')
        alice = ('ares', 'ears', 'feal', 'flea')
        memories = (alice, bob, carol, dan)
        players = (2, 1)
        expected = 1
        submitted = anagrams(subjects, memories, players)
        test.assert_equals(submitted, expected)

    @test.it('Complete Order of Rounds')
    def rounds():
        subjects = ('spam', 'tsar', 'apse', 'swan', 'alps', 'name', 'ales', 'last')
        alice = ('lats', 'rats', 'sale', 'pals', 'swan', 'amen', 'lase', 'salp', 'samp', 'apes', 'pams', 'spam', 'alps', 'peas', 'sawn', 'tars', 'mean', 'last', 'snaw', 'pase', 'star', 'ales', 'alts', 'mane', 'tsar', 'awns', 'wans', 'slap', 'nema', 'amps', 'spae', 'laps')
        bob   = ('rats', 'pams', 'slap', 'ales', 'salt', 'snaw', 'slat', 'apes', 'mean', 'seal', 'alts', 'tars', 'lase', 'wans', 'sale', 'lats', 'mane', 'awns', 'sawn', 'laps', 'peas', 'amps', 'star', 'maps', 'tsar', 'spae', 'apse', 'swan', 'name', 'arts', 'amen', 'spam')
        carol = ('nema', 'arts', 'star', 'samp', 'laps', 'seal', 'pals', 'apes', 'mane', 'swan', 'lats', 'wans', 'alts', 'slap', 'leas', 'apse', 'sale', 'lase', 'tars', 'rats', 'ales', 'mean', 'salp', 'awns', 'pams', 'tsar', 'salt', 'amps', 'spam', 'slat', 'name', 'pase')
        dan   = ('last', 'name', 'ales', 'slat', 'amen', 'pals', 'salt', 'apse', 'star', 'peas', 'sale', 'salp', 'slap', 'spam', 'snaw', 'lats', 'leas', 'awns', 'alts', 'sawn', 'rats', 'tsar', 'spae', 'laps', 'amps', 'arts', 'nema', 'wans', 'maps', 'mean', 'swan', 'tars')
        memories = (alice, bob, carol, dan)
        players = (1, 3)
        expected = 1
        submitted = anagrams(subjects, memories, players)
        test.assert_equals(submitted, expected)

    @test.it('Comprehensive Scenarios')
    def scenarios():
        subjects = ('darb', 'bust', 'spot', 'calo', 'oaky', 'mite', 'meta', 'tael', 'gore', 'elan', 'code', 'demo')
        alice = ('bard', 'coal', 'cola', 'dome', 'drab', 'emit', 'ergo', 'goer', 'gore', 'loca', 'mode', 'okay', 'stop', 'stub', 'tame')
        bob   = ('buts', 'code', 'coed', 'lean', 'leat', 'mate', 'meat', 'post', 'pots', 'spot', 'stop', 'stub', 'tale', 'tame', 'tela')
        carol = ('brad', 'bust', 'darb', 'ergo', 'gore', 'item', 'lane', 'mate', 'meta', 'ogre', 'okay', 'tame', 'team', 'time', 'tubs')
        dan   = ('calo', 'coal', 'code', 'cola', 'deco', 'demo', 'kayo', 'late', 'mode', 'oaky', 'opts', 'spot', 'tale', 'teal', 'tops')
        memories = (alice, bob, carol, dan)
        players = (0, 2)
        expected = -1
        submitted = anagrams(subjects, memories, players)
        test.assert_equals(submitted, expected)