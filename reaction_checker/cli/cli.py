import argparse


def parcer():
    parser = argparse.ArgumentParser(description='reaction_checker')
    parser.add_argument('-start', action='store_true', help='starts a program')
    result = parser.parse_args().address
    return result