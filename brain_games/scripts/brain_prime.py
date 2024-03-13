#!/usr/bin/env python3
from brain_games.games import prime
from brain_games.engine import engine


def main():
    """Start brain-prime game"""
    engine(prime)


if __name__ == '__main__':
    main()
