from random import choice


def make_laugh_at_func(person):
    def get_laugh():
        laugh = choice(('HAHAHAH', 'lol', 'tehehe'))
        return f"{laugh} {person}"
    return get_laugh


laugh_at = make_laugh_at_func("Linda")

print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())
