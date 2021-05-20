unwanted_targets = {
        'Alexandre Dumas-fils': ["Her agony"],
        'André Gide': ['by the same ethos'],
        'Charles M. Schulz': ['the syndicate'],
        'George Bernard Shaw': ['considered it', 'requesting it', 'accepted it'],
        'Haruki Murakami': ['Facebook'],
        'Jane Austen': ['A Memoir of Jane Austen'],
        'J.K. Rowling': ['the pen name', 'caricature of me', 'based on me'],
        'J.R.R. Tolkien': ['wrote them'],
        'Mark Twain': ['his calling', 'travelogues'],
        'Martin Luther King Jr.': ['he raised public consciousness'],
        'Pablo Neruda': ['pen name was derived']
    }

def unwanted_target_removeal_local(n, key):
    if key in unwanted_targets.keys():
        doesnt_contain_unwanted_targets = not any(map(n.__contains__, unwanted_targets[key]))
        return doesnt_contain_unwanted_targets
    return n