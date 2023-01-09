class GameStats:
    """Track statistics for Snake Game"""
    def __init__(self, settings):
        self.settings = settings
        self.reset_stats()
        self.active = False

    def reset_stats(self):
        self.score = 0