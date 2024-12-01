import sys
import pygame
from Modules.game import Game


def get_game_settings(difficulty):
    if difficulty == "easy":
        return 0.18, (8, 8)
    elif difficulty == "medium":
        return 0.21, (12, 12)
    elif difficulty == "hard":
        return 0.27, (16, 16)
    else:
        raise ValueError("Invalid difficulty. Choose 'easy', 'medium', or 'hard'.")


def main():
    try:
        if len(sys.argv) < 2:
            raise ValueError("Not enough arguments. Usage: python main.py <difficulty>")

        difficulty = sys.argv[1]
        prob, size = get_game_settings(difficulty)
        print(f"Selected difficulty: {difficulty.capitalize()}, Probability: {prob}, Grid Size: {size}")

        g = Game(size, prob)
        g.run()

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    main()
