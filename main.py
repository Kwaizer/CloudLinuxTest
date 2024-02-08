import time
from typing import Optional
import typer

app = typer.Typer()

from traverse import traverse

"""
python main.py "/home/kwaizer/Downloads/Telegram Desktop"
or
python main.py "/home/kwaizer/Downloads/Telegram Desktop" --thr 50
or
python main.py "/home/kwaizer/Desktop" --thr 1
or 
python main.py "/home/kwaizer/Desktop/folder"
or
python main.py "/home/kwaizer/CloudLinux/test"
"""
@app.command()
def perform(dir: str, thr: Optional[int] = None):
        start_time = time.time()
        traverse(dir, thr)
        print("--- %s seconds ---" % (time.time() - start_time))
        

if __name__ == "__main__":
    app()
    