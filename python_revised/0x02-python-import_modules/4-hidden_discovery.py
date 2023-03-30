"""
* import the modulee
* using the dir function, print all the defined names except the ones with __
"""

if __name__ == "__main__":

    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[0:2] != '__':
            print("{:s}".format(name))
