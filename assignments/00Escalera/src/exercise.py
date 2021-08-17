import math
def main():
    altura=float(input("Altura de la casa: "))
    angulo=int(input("Angulo en grados: "))
    
    aradians=math.radians(angulo)

    largo=round(altura/math.sin(aradians))

    print(f"Largo de la escalera: {largo}")


if __name__ == '__main__':
    main()

