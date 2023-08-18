import pygame

pygame.init()  # initialize pygame
screen = pygame.display.set_mode((800, 600))


class Cards:
    def __init__(self, card_value, reveal_value):
        self.card_value = card_value
        self.reveal_value = reveal_value


class Destinations:
    def __init__(self, payment_of_travel, reward):
        self.payment_of_travel = payment_of_travel
        self.reward = reward
        