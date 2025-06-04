import math
class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def reset(self):
        self.x = 0
        self.y = 0
class Line:
  def __init__(self, punto1:"Point", punto2:"Point"):
    self.punto1 = punto1 #Punto tendra 2 atributos (x, y)
    self.punto2 = punto2
  def compute_length(self):
    calculo2=math.dist((self.punto1.x, self.punto1.y), (self.punto2.x, self.punto2.y)) # Metodo con math
    return calculo2
  
class Shape:
    def __init__(self, puntos:list):
        self.vertices = puntos
    def ver_puntos(self):
        print(self.vertices)
    def distancias_vertices(self): 
        #Objetos tipo linea
        d_lado_1 = Line(self.vertices[0],self.vertices[1]).compute_length()
        d_lado_2 = Line(self.vertices[1],self.vertices[2]).compute_length()
        d_lado_3 = Line(self.vertices[2],self.vertices[0]).compute_length()
        return d_lado_1, d_lado_2, d_lado_3
    
    def es_cuadrilatero(self):
        return len(self.vertices)==4
    
class Triangle(Shape):
    def __init__(self, puntos):
        if len(puntos) != 3:
            raise ValueError("Un triangulo debe tener 3 vertices")
        super().__init__(puntos)
    def area_figura(self):
        lado1, lado2, lado3 = self.distancias_vertices()
        sp= (lado1 + lado2 + lado3)/2
        area_final= (sp*(sp-lado1)*(sp-lado2)*(sp-lado3))**(1/2)
        return area_final
    def es_triangulo(self):
        return len(self.vertices)==3
    
    
class Equilatero(Triangle):
    def es_equilatero(self):
        lado1, lado2, lado3 = self.distancias_vertices()
        if lado1==lado2==lado3:
            salida="es equilatero"
        else:
            salida="no es equilatero"
        return salida
class Isoceles(Triangle):
    def es_isoceles(self):
        lado1, lado2, lado3 = self.distancias_vertices()
        if lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
            salida="es Isoceles"
        else:
            salida="no es Isoceles"
        return salida
class Escaleno(Triangle):
    def es_escaleno(self):
        lado1, lado2, lado3 = self.distancias_vertices()
        if lado1 != lado2 and lado2 != lado3 and lado1 != lado3:
            salida="es escaleno"
        else:
            salida="no es escaleno"
        return salida

class T_Rectangulo(Triangle):
    def es_T_Rectangulo(self):
        lado1, lado2, lado3 = self.distancias_vertices()
        lados = sorted([lado1, lado2, lado3])  # Ordenamos para que el mayor esté al final
        a, b, c = lados
        if math.isclose(a**2 + b**2, c**2, abs_tol=1e-5): #Teorema de pitagoras con el abs_tol siendo el margen de error aceptado
            return True,"es triangulo rectangulo"
        else:
            return False, "no es triangulo rectangulo"
        # salida: Tupla con booleano y texto

def tipo_triangulo(puntos):
    t = Triangle(puntos)
    t_rec_comp = T_Rectangulo(puntos)
    l1, l2, l3 = t.distancias_vertices()
    #math.isclose se usa para evitar errores por decimales
    if t_rec_comp.es_T_Rectangulo()[0]:  # Checa primero si es rectángulo
        return T_Rectangulo(puntos)
    elif math.isclose(l1, l2) and math.isclose(l2, l3):
        return Equilatero(puntos)
    elif (math.isclose(l1, l2) or math.isclose(l2, l3) or math.isclose(l1, l3)):
        return Isoceles(puntos)
    elif not math.isclose(l1, l2) and not math.isclose(l2, l3) and not math.isclose(l1, l3): #l1 ≠ l2 / l2 ≠ l3 / l1 ≠ l3
        return Escaleno(puntos)
    else:
        return None

p1 = Point(0, 0)
p2 = Point(5, 0)
p3 = Point(2.5, 3)
tri = tipo_triangulo([p1, p2, p3]) #Ninguno
tri2= tipo_triangulo([Point(0, 0),Point(2, 0),Point(1, math.sqrt(3))]) #Equilatero
tri3= tipo_triangulo([Point(0, 0), Point(4, 0), Point(2, 3)]) # Isoceles
tri4= tipo_triangulo([Point(0, 0), Point(3, 0), Point(2, 1)]) # Escaleno
tri5= tipo_triangulo([Point(0, 0), Point(4, 0), Point(0, 3)]) # Rectangulo

triangulos=[tri,tri2,tri3,tri4,tri5]

contador= 1
for triangulo in triangulos:
    print(f"Triangulo numero {contador}:", end=" ")

    if isinstance(triangulo, T_Rectangulo):
        booleano, resultado = triangulo.es_T_Rectangulo() 
        print(resultado)
    elif isinstance(triangulo, Equilatero):
        print(triangulo.es_equilatero())
    elif isinstance(triangulo, Isoceles):
        print(triangulo.es_isoceles())
    elif isinstance(triangulo, Escaleno):
        print(triangulo.es_escaleno())
    else:
        print("Tu figura no es ningun tipo de triángulo en la base de datos")

    print("Su area es:", triangulo.area_figura())
    contador += 1
