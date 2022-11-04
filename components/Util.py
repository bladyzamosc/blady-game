from pathlib import Path


class Util:
    def path_to_asset(asset):
        parrent = Path(__file__).resolve().parent.parent
        return parrent.joinpath("assets", asset)
