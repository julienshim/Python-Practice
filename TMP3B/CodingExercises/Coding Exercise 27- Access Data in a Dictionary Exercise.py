artist = {
    "first": "Neil",
    "last": "Young",
}

# f string doesn't work on test
full_name = artist['first'] + " " + artist['last']
# full_name = "{} {}".format(artist["first"],artist["last"]) # format
