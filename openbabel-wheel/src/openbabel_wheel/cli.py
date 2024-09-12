import os
import pathlib
import subprocess
import sys
from openbabel import __version__

ROOT = pathlib.Path(__file__).parent.parent

def obabel() -> None:
    return _run("obabel")

def _bin(filename: str) -> str:
    return (ROOT / "openbabel" / "bin" / filename).as_posix()

def _run(name: str) -> None:
    env = dict(os.environ) | {
            "BABEL_LIBDIR": (ROOT / "openbabel" / "lib" / "openbabel" / __version__).as_posix(),
            "BABEL_DATADIR": (ROOT / "openbabel" / "share" / "openbabel" / __version__).as_posix(),
    }
    subprocess.run([_bin(name), *sys.argv[1:]], check=False, env=env)
