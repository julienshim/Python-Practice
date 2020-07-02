from termcolor import colored

# print(dir(termcolor))

# help(termcolor)

text = colored("HI THERE!", color="magenta",
               on_color="on_cyan", attrs=["blink"])  # link works in terminal not in vscode # noqa

print(text)
