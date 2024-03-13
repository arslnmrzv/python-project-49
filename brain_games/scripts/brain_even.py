#!/usr/bin/env python3
from brain_games.games import even
from brain_games.engine import engine


def main():
    """Start brain-even game"""
    engine(even)


if __name__ == '__main__':
    main()
