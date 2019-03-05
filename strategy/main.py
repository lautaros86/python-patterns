from strategy import StrategyMoveGround
from strategy import StrategyMoveWater
from strategy import StrategyMoveAir


class Animal:

    def __init__(self, strategy):
        self.strategy = strategy

    def move(self, arg1):
        self.strategy.move(self, arg1)


dog = Animal(StrategyMoveGround)
fish = Animal(StrategyMoveWater)
bird = Animal(StrategyMoveAir)

dog.move("wof wof")
fish.move("bloop bloop")
bird.move("pio pio")
