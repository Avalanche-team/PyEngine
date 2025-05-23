from ..config import *
from .component import Component


def load_obj_model(filename: str) -> list[float]:
    """
        Load a mesh from an obj file.

        Parameters:

            filename: the filename.

        Returns:

            The loaded data, in a flattened format.
    """

    v = []
    vt = []
    vn = []

    vertices = []

    with open(filename, "r") as file:

        line = file.readline()

        while line:

            words = line.split(" ")
            match words[0]:

                case "v":
                    v.append(read_vertex_data(words))

                case "vt":
                    vt.append(read_texcoord_data(words))

                case "vn":
                    vn.append(read_normal_data(words))

                case "f":
                    read_face_data(words, v, vt, vn, vertices)

            line = file.readline()

    vertex_stride = 8  # 3 for position, 2 for texcoord, 3 for normal
    vertex_count = len(vertices) // vertex_stride

    positions = []
    texcoords = []

    for i in range(vertex_count):
        base = i * vertex_stride
        positions.extend(vertices[base:base + 3])  # x, y, z
        texcoords.extend(vertices[base + 3:base + 5])  # u, v
        # normals are skipped for now

    return Mesh(positions=positions, texture_coord=texcoords)


def read_vertex_data(words: list[str]) -> list[float]:
    """
        Returns a vertex description.
    """

    return [
        float(words[1]),
        float(words[2]),
        float(words[3])
    ]


def read_texcoord_data(words: list[str]) -> list[float]:
    """
        Returns a texture coordinate description.
    """

    u = float(words[1])
    v = float(words[2])
    return [u, 1.0 - v]


def read_normal_data(words: list[str]) -> list[float]:
    """
        Returns a normal vector description.
    """

    return [
        float(words[1]),
        float(words[2]),
        float(words[3])
    ]


def read_face_data(
        words: list[str],
        v: list[list[float]], vt: list[list[float]],
        vn: list[list[float]], vertices: list[float]) -> None:
    """
        Reads an edgetable and makes a face from it.
    """

    triangleCount = len(words) - 3

    for i in range(triangleCount):
        make_corner(words[1], v, vt, vn, vertices)
        make_corner(words[2 + i], v, vt, vn, vertices)
        make_corner(words[3 + i], v, vt, vn, vertices)


def make_corner(corner_description: str,
                v: list[list[float]], vt: list[list[float]],
                vn: list[list[float]], vertices: list[float]) -> None:
    """
    Composes a flattened description of a vertex.
    Handles cases where texture coordinates or normals may be missing.
    """

    v_vt_vn = corner_description.split("/")

    # Position is always present
    position_index = int(v_vt_vn[0]) - 1
    for element in v[position_index]:
        vertices.append(element)

    # Texture coordinate may be missing
    if len(v_vt_vn) > 1 and v_vt_vn[1] != '':
        texcoord_index = int(v_vt_vn[1]) - 1
        for element in vt[texcoord_index]:
            vertices.append(element)
    else:
        # Pad with default values if texcoords are missing
        vertices.extend([0.0, 0.0])

    # Normal may be missing
    if len(v_vt_vn) > 2 and v_vt_vn[2] != '':
        normal_index = int(v_vt_vn[2]) - 1
        for element in vn[normal_index]:
            vertices.append(element)
    else:
        # Pad with default values if normals are missing
        vertices.extend([0.0, 0.0, 0.0])



class Mesh(Component):
    def __init__(self,
                 positions: list[float] = None,
                 texture_coord: list[float] = None):
        super().__init__()

        self.type = "MESH"
        self.positions = positions or []
        self.texture_coord = texture_coord or []

        self.vao = None
        self.vbo = None
        self.ebo = None
        self.should_render = True

    def on_create(self):
        super().on_create()
        
        positions = np.array(self.positions, dtype='f4').reshape(-1, 3)
        texcoords = np.array(self.texture_coord, dtype='f4').reshape(-1, 2)

        vertex_data = np.hstack((positions, texcoords)).flatten().astype('f4')

        self.vbo = self.engine.ctx.buffer(vertex_data.tobytes())
        content = [(self.vbo, '3f 2f', 'in_position',"in_texcoord")]

        # Uses engine.shader (make sure it exists before mesh is created!)
        self.vao = self.engine.ctx.vertex_array(self.scene.shader.program, content)

    def on_render(self):
        if self.should_render and self.vao:
            self.vao.render(mode=self.engine.draw_method)

    def on_close(self):
        super().on_close()
        self.vao.release()