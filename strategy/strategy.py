class StrategyMove:

    def __init__(self, strategy=None):
        self.strategy = strategy

    def move(self, arg1):
        self.strategy.move(arg1)


class StrategyMoveGround:
    def move(self, arg1):
        print("advance walkin - " + arg1)


class StrategyMoveWater:
    def move(self, arg1):
        print("just keep swimming - " + arg1)


class StrategyMoveAir:
    def move(self, arg1):
        print("advance flying - " + arg1)
