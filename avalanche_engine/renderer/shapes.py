from avalanche_engine.config import *
from ..components.mesh import Mesh

def get_square_mesh():
    positions = [
        # First triangle
        -0.5, -0.5, 0.0,  # Bottom left
        0.5, -0.5, 0.0,  # Bottom right
        0.5, 0.5, 0.0,  # Top right

        # Second triangle
        -0.5, -0.5, 0.0,  # Bottom left
        0.5, 0.5, 0.0,  # Top right
        -0.5, 0.5, 0.0,  # Top left
    ]

    return Mesh(
        positions=positions
    )