import time
from typing import Optional
import typer
from display import tree

app = typer.Typer()

from logic.traverse import get_info


"""
python main.py "/home/kwaizer/Downloads/Telegram Desktop"
or
python main.py "/home/kwaizer/Downloads/Telegram Desktop" --thr 50 --ctg --rep
or
python main.py "/home/kwaizer/Desktop" --thr 1
or 
python main.py "/home/kwaizer/Desktop/folder"
or
python main.py "/home/kwaizer/Desktop/folder2"
or
python main.py "/home/kwaizer/CloudLinux/test"
"""
@app.command()
def perform(dir: str, 
            thr: Optional[int] = typer.Option(None, "--thr", help="Threshold value"),
            rep: bool = typer.Option(False, "--rep", help="Flag to get permission report"),
            ctg: bool = typer.Option(False, "--ctg", help="Flag to get categories report")):
        start_time = time.time()
        # directory_to_traverse = "/home/kwaizer/CloudLinux/test/.venv/lib"
        # for line in tree(Path.home() / dir):
        #     print(line)
        get_info(dir, thr, rep, ctg)
        print("--- %s seconds ---" % (time.time() - start_time))
        

if __name__ == "__main__":
    app()
    