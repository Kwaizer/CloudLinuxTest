import time
import typer
from typing import Optional
from display import display
from logic.traverse import get_info

app = typer.Typer()
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
            ctg: bool = typer.Option(False, "--ctg", help="Flag to get categories report"),
            dsp: bool = typer.Option(False, "--dsp", help="Flag to display file tree")):
        
        start_time = time.time()

        if dsp == True:
            display(dir)

        get_info(dir, thr, rep, ctg)
        print("--- %s seconds ---" % (time.time() - start_time))
        

if __name__ == "__main__":
    app()
    