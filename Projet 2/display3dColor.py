import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot3D(255, 0, 0, color='red')
ax.plot3D(0, 255, 0, color='green')
ax.plot3D(0, 0, 255, color='blue')

# # ax.plot3D(217, 51, 73, '.', color=(200/255, 35/255, 70/255))#cherry
# ax.plot3D(181,13,0, '.', color=(200/255, 35/255, 70/255))#cherry-guess

# # ax.plot3D(78, 116, 189, '.', color=(78/255, 116/255, 189/255))#Royal blue
# ax.plot3D(24,48,189, '.', color=(78/255, 116/255, 189/255))#Royal blue


# # ax.plot3D(178, 158, 47, '.', color=(178/255, 158/255, 47/255))#olive
# ax.plot3D(150,205,11, '.', color=(178/255, 158/255, 47/255))#olive

# ax.quiver(
#         # 217, 51, 73, # <-- starting point of vector
#         0, 0, 0, # <-- starting point of vector
#         217,51,73, # <-- vector direction
#         color = (200/255, 35/255, 70/255), #cherry
#     )
# cherryDist = 89.83

# ax.quiver(
#         78, 116, 189, # <-- starting point of vector
#         24-78, 48-116, 0, # <-- vector direction
#         color = (78/255, 116/255, 189/255), #royal blue
#     )
# royalBlueDist = 86.83

# ax.quiver(
#         0, 0, 0, # <-- starting point of vector
#         178, 158, 47, # <-- starting point of vector
#         # 150-178,205-158,11-47, # <-- vector direction
#         color = (178/255, 158/255, 47/255), #olive
#     )
# oliveDist = 65.49

ax.quiver(
        0, 0, 0, # <-- starting point of vector
        255, 0, 0, # <-- vector direction
        color = 'red',
    )

ax.quiver(
        0, 0, 0, # <-- starting point of vector
        0, 0, 255, # <-- vector direction
        color = 'blue',
    )

ax.quiver(
        0, 0, 0, # <-- starting point of vector
        0, 255, 0, # <-- vector direction
        color = 'green',
    )

plt.savefig('colorsGeo.pdf')
plt.show()