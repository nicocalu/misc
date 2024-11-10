import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def fibonacci_sphere(samples=1000):

    points = []
    phi = math.pi * (math.sqrt(5.) - 1.)  # golden angle in radians

    for i in range(samples):
        z = 1 - (i / float(samples - 1)) * 2  # y goes from 1 to -1
        radius = math.sqrt(1 - z * z)  # radius at y

        theta = phi * i  # golden angle increment

        x = math.cos(theta) * radius
        y = math.sin(theta) * radius

        points.append((x, y, z))

    return points

def plot_sphere_points(points):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Extract x, y, z coordinates from the points list
    x_coords = [point[0] for point in points]
    y_coords = [point[1] for point in points]
    z_coords = [point[2] for point in points]

    # Plot the points as a 3D scatter plot
    ax.scatter(x_coords, y_coords, z_coords, color='black')

    # Set labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Points on a Sphere')
    ax.set_aspect('equal')

    # Show the plot
    plt.show()


# Generate points on a sphere using fibonacci_sphere function
points = fibonacci_sphere(samples=1000)

# Plot the points on a sphere
plot_sphere_points(points)