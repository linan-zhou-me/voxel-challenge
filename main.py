import taichi as ti
from scene import Scene
from taichi.math import *

scene = Scene(voxel_edges=0, exposure=2)
scene.set_floor(0, (1, 1, 1))
scene.set_directional_light((-1, 1, 1), 0.2, (1, 0.9, 0.9))
scene.set_background_color((1, 0.9, 0.9))


@ti.func
def create_sphere(x, y, z, r):
    for i, j, k in ti.ndrange((-64, 63), (-64, 63), (-64, 63)):
        if ((i-x)**2 + (j-y)**2 + (k-z)**2)**0.5 <= r:
            scene.set_voxel(vec3(i, j, k), 1, vec3(1, 1*ti.random(), 1*ti.random()))


@ti.kernel
def initialize_voxels():
    create_sphere(-30, 10, 0, 10)
    create_sphere(-10, 9, 0, 9)
    create_sphere(8, 8, 0, 8)
    create_sphere(24, 7, 0, 7)
    create_sphere(38, 6, 0, 6)


initialize_voxels()
scene.finish()
