from random import choice


def make_laugh_func():
    def get_laugh():
        sound = choice(('HAHAHAH', 'lol', 'tehehe'))
        return sound
    return get_laugh


laugh = make_laugh_func()
print(laugh())
