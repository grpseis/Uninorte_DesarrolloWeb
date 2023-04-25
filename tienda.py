def muestra_productos():
    print("1. Arroz                 $1.800")
    print("2. Carne                $12.500")
    print("3. Cocacola Litro 1/4    $4.600")
    print("4. Papas x libra         $6.300")
    print("5. Platanos verdes und   $2.200")
    print("  \n")
    return()


def cargar_por_teclado():
    muestra_productos()
    p = ""
    pr = 0
    option = 1
    cantS = 0
    while option >= 1 and option <= 5:
        option = int(input("Codigo Producto  o [otro número diferente] para salir: "))

        if option == 0:
            break
        elif option >= 1 and option <= 5:
            cantS = int(input("Cantidad a solicitar: "))
        if option == 1:
            p = "Arroz"
            pr = 1800 * cantS
        if option == 2:
            p = "Carne"
            pr = 12500 * cantS
        if option == 3:
            p = "Cocacola Litro 1/4"
            pr = 4600 * cantS
        if option == 4:
            p = "Papas x libra"
            pr = 6300 * cantS
        if option == 5:
            p = "Platanos verdes und"
            pr = 2200 * cantS
        if option >= 1 and option <= 5:
            t1 = (p ,pr)
            l1.append(t1)
    return()

def listar_productos_precios():
    print(l1)
    return()

def imprimir(productos):
    totCompra = 0
    print("Productos a Adquirir")
    for nombre, precio in productos:
        print(nombre, precio)
        totCompra += precio
    print("Total de la compra es de $ ", totCompra,"\n")
    return(totCompra)


## Principal
apruebaPedido = 'S'
l1=[]
t1=()
tootC = 0
cargar_por_teclado()
#listar_productos_precios()
tootC = imprimir(l1)
if tootC > 0:
    apruebaPedido = input("Desea Aprobar el pedido ? [s / n]  ")
    if apruebaPedido == "s" or apruebaPedido == "S":
        imprimir(l1)
        print("Compra Aprobada...\n")
    else:
        print("Compra Cancelada...\n")
print("presione enter para continuar...")
input()




