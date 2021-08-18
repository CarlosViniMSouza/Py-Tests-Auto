# pip install tabulate

from tabulate import tabulate
from termcolor import colored

print("\n"*3)

def content():
    header = ["Social Medias", "Address"]
    return [colored(c, 'yellow', attrs=['bold']) for c in header]

def create_table():
    table = [
        ["LinkedIn", "https://www.linkedin.com/in/carlosvinimsouza/"],
        ["GitHub", "https://github.com/CarlosViniMSouza"],
        ["Instagram", "https://www.instagram.com/carlosvinimsouza/"],
        ["Twitter", "https://twitter.com/CarlosViniMS1"],
        ["Blog", "https://carlosblog2021.herokuapp.com/"],
        ["HackerRank", "https://www.hackerrank.com/vinicius_souza51"]
    ]

    return [[colored(d[0], 'green', attrs=['bold']), d[1]] for d in table]

print(tabulate(create_table(), headers=content(), tablefmt="fancy_grid"))