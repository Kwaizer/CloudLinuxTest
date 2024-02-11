import time
import typer
from typing import Optional
from display import display
from logic.traverse import get_info


app = typer.Typer()


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
    