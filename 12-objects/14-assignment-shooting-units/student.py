
class Unit:
    def __init__(self, health, firepower, armor):
        self.__health = health
        self.__firepower = firepower
        self.__armor = armor

        if health < 0 or firepower < 0 or armor < 0:
            raise ValueError("Values should all be positive")

    def health(self):
        return self.__health

    def firepower(self):
        return self.__firepower

    def armor(self):
        return self.__armor

    def shot_by(self, other):
        self.__health -= other.__firepower - self.__armor

        if self.__health < 0:
            raise ValueError("Health cannot go below 0 (Dead)")