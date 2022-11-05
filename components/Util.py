from pathlib import Path

up = 'w'
down = 's'
left = 'a'
right = 'd'
pause = 'p'

class Util:
    @staticmethod
    def path_to_asset(asset):
        parrent = Path(__file__).resolve().parent.parent
        return parrent.joinpath("assets", asset)
