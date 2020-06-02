# Define combine_words below:
def combine_words(word, **kwargs):
    for i, j in kwargs.items():
        if i == "suffix":
            return word + j
        if i == "prefix":
            return j + word
    return word

# correct way
# def combine_words(word,**kwargs):
    # if 'prefix' in kwargs:
    #     return kwargs['prefix'] + word
    # elif 'suffix' in kwargs:
    #     return word + kwargs['suffix']
    # return word
