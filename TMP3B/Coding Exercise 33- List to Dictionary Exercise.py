person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]

# use the person variable in your answer
answer = {value[0]: value[1] for value in person}
# alt1 : answer = {k:v for k,v in person}
# alt2 : answer = dict(person)
