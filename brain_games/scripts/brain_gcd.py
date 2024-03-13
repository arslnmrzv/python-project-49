#!/usr/bin/env python3
from brain_games.games import gcd
from brain_games.engine import engine


def main():
    """Start brain-gcd game"""
    engine(gcd)


if __name__ == '__main__':
    main()
