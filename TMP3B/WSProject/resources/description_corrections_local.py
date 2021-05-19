from re import sub

local_correction_pairs = {
    "William Nicholson": [
        ('children.from', 'children. From'),
        ('.He lives', '. He lives')
    ],
    "Ralph Waldo Emerson": [
        (', who takes up such Emersonian themes as power, fate, the uses of poetry and history, and the critique of Christianity. D. 1882', '')
    ],
    "Mother Teresa": [
        ('Blessed Teresa of Calcutta, or ', '')
    ],
    "Mark Twain": [
        (', better known by his pen name Mark Twain,', ''),
        ('\(1876\).Twain ', '\(1876\). Twain '),
        ('.Excerpted', '. Excerpted')
    ],
    "Marilyn Monroe": [
        ('\(born Norma Jeane Mortenson; June 1, 1926 – August 5, 1962\) ', 'born on June 1, 1926 '),
        (', Marilyn Monroe Productions,', '')
    ],
    "Madeleine L'Engle": [
        ('.\"Madeleine ', '. Madeleine '),
        ('.\"http', '. Http')
    ],
    'Jorge Luis Borges': [
        ('1986.J. M. Coetzee', '1986. J. M. Coetzee')
    ],
    'John Lennon': [
        (".Lennon revealed", ". Lennon revealed"),
        ("As the group began", "As The Beatles began"),
        (', including John Lennon/Plastic Ono Band and Imagine, and iconic songs such as "Give Peace a Chance" and "Imagine"', '')
    ],
    'J.R.R. Tolkien': [
        ('2009.Religious', '2009. Religious'),
        ('influencesJ.R.R. Tolkien', 'influences J.R.R. Tolkien'),
        ('Rings\n.Tolkien', 'Rings. Tolkien'),
        (', was born', ' was born'),
    ],
    'J.K. Rowling': [
        ('See also: Robert Galbraith', '')
    ],
    'J.D. Salinger': [
        ('followed Catcher', 'followed his 1951 novel The Catcher in the Rye')
    ],
    'Jim Henson': [
        (', and the founder of The Jim Henson Company, the Jim Henson Foundation, and Jim Henson\'s Creature Shop', '')
    ],
    "Khaled Hosseini": [
        ('the Khaled Hosseini Foundation', 'his foundation')
    ],
    'Haruki Murakami': [
        ('.Since childhood', '. Since childhood'),
        ('\(Japanese: 村上 春樹\) ', '')
    ],
    'Harper Lee': [
        ('continued as', 'was')
    ],
    'George R.R. Martin': [
        ('http', 'Http')
    ],
    'George Eliot': [
        ('adopting the nom de plume \"George Eliot,\"', 'adopting a nom de plume,' )
    ],
    'Garrison Keillor': [
        ('\(born Gary Edward Keillor on August 7, 1942 in Anoka, Minnesota\)', 
        'born on August 7, 1942 in Anoka, Minnesota'),
        ('.Keillor was born', '. Keillor was born'),
        ('."In 2004', '. "In 2004'),
        ('\(Keillor also appears in the movie.\)', '')
    ],
    'E.E. Cummings': [
        ('.\”During', '. During'),
        ('source:', 'Source:'),
        ("But, primarily, ", "")
    ],
    'Douglas Adams': [
        ('.In addition', '. In addition'),
        ('other written', 'written'),
    ],
    'Charles Bukowski': [
        ('.He died', '. He died'),
        ('\(born as Heinrich Karl Bukowski\) ', ''),
        ('booksCharles', 'books. Charles')
    ],
    'Bob Marley': [
        (': The Wailers \(1964 – 1974\) and Bob Marley & the Wailers \(1974 - 1981\)', ''),
        ('och', 'and')
    ],
    'Ayn Rand': [
        ('.She', '. She'),
    ],
    'Allen Saunders': [
        (', John Allen Saunders,', ''),
        (" \(John Phillip Saunders, 1924–2003\),", ",")
    ],
    'Alfred Tennyson': [
        ('plays. he', 'plays. He')
    ],
    'Albert Einstein': [
        ('the word "Einstein"', 'his name'),
        (', however,', ''),
        ('continued to deal', 'dealt'),
    ]
}

def description_corrections_local(string, key):
    if key in local_correction_pairs.keys():
        for pair in local_correction_pairs[key]:
            [before, after] = pair
            string = sub(before, after, string)
    return string