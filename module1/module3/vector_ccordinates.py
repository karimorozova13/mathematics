import numpy as np
import matplotlib.pyplot as plt

def calculate_vectors_components(vectors):
    """
    Функція для визначення компонент декількох векторів.


    Параметри:
    - vectors: Список кортежів (start_point, end_point), де start_point та end_point - це координати початкової та кінцевої точок вектора.


    Повертає:
    - components: Список кортежів (x_components, y_components), де x_components та y_components - це компоненти по X та Y для кожного вектора.
    """
    components = []


    for start_point, end_point in vectors:
        x_component = end_point[0] - start_point[0]
        y_component = end_point[1] - start_point[1]
        components.append((x_component, y_component))


    return components


vectors = [((1, 2), (4, 6)), ((2, 3), (5, 2)), ((0, 0), (-2, 4))]


vector_components = calculate_vectors_components(vectors)
print(vector_components)

def draw_vectors(vectors):
    colors = ['green', 'red', 'purple']
 
    fig, ax = plt.subplots()

    for i in range(len(vectors)):
        start_point, end_point = vectors[i]

        # Визначення вектора та його довжини
        vector = np.array([end_point[0] - start_point[0], end_point[1] - start_point[1]])

        # Нормалізація вектора
        length = np.linalg.norm(vector)
        
        # normalized_vector = vector / length
        normalized_vector = vector

        # Додавання стрілки до осей
        ax.arrow(start_point[0], start_point[1], normalized_vector[0], normalized_vector[1], head_width=0.1, head_length=0.1, fc=colors[i], ec=colors[i])


    ax.set_title('Some vectors in a plane')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid(True)
    
    plt.show()

vectors = [((0, 0), (1, 3)), ((0, 0), (2, 6))]
print(calculate_vectors_components(vectors))

draw_vectors(vectors)
