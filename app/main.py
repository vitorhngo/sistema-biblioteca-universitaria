import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from app.controller.sistema_controller import SistemaController

if __name__ == "__main__":
    app = SistemaController()
    app.executar()
