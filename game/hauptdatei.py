


# ein Package ist ein Verzeichnis, das aus einem oder mehreren Modulen besteht. 
# In ein Package kommt normalerweise eine Datei namens __init__.py

#Im Package »functions« liegt ein Modul beispielsweise namens »distances.py«. 
# Ein Modul ist eine Python-Datei, die u.a. Funktionen/Klasse/Variablen

from tools.distances import (euclidian_distance, manhattan_distance)

    
def main():
    print("Das ist die »MAIN.PY«")
    p1 = (3,3)
    p2 = (3,3)
    dist = euclidian_distance(p1, p2)
    print(f"Distanz p1 p1: {dist}")

# __name__ ist eine variable die unabhänig vom namen er Datei belegt wird.
# __name__ = __main__ in der datei die ausgeführt wird

if __name__== "__main__":
    main()