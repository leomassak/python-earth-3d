import os

BASE_PATH = 'output'

def get_path(filename):
    return os.path.join(BASE_PATH, filename)

def write_mesh_object(verts, faces, uvtex, filename, mtlfile='sphere.mtl'):
    with open(get_path(filename), 'w') as meshfile:
        meshfile.write(f'mtllib {mtlfile}\n')
        for (x,y,z) in verts:
            meshfile.write(f'v {x} {y} {z}')
        for (u, v) in uvtex:
            meshfile.write(f'vt {u} {v}\n')
        meshfile.write('usemtl material_1\n')
        for (a, b, c) in faces:
            meshfile.write(f'f {a}/{a} {b}/{b} {c}/{c}\n')

if __name__ == '__main__':
    v, f, uv = sphere(1, 50, 100)
    write_mesh_object(v, f, uv. 'earth.obj')

