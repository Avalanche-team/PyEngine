from avalanche_engine.config import *
from ..components.mesh import Mesh

def get_square_mesh():
    positions = [
        -0.5, -0.5, 0.0,
        0.5, -0.5, 0.0,
        0.5, 0.5, 0.0,

        -0.5, -0.5, 0.0,
        0.5, 0.5, 0.0,
        -0.5, 0.5, 0.0,
    ]

    texture_coords = [
        0.0,0.0,
        1.0,0.0,
        1.0,1.0,
        0.0,0.0,
        1.0,1.0,
        0.0,1.0
    ]

    return Mesh(
        positions=positions,
        texture_coord=texture_coords
    )