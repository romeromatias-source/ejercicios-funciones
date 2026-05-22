"""
UNIDAD 3 - FUNCIONES EN PYTHON
Ejercicios 3-1 al 3-7
"""

# ─────────────────────────────────────────────
# FUNCIONES AUXILIARES REUTILIZABLES
# ─────────────────────────────────────────────

def mostrar_numero(numero):
    """3-1: Muestra por pantalla el número recibido como parámetro."""
    print(f"El número es: {numero}")


def pedir_numero():
    """3-2: Pide el ingreso de un número y lo retorna."""
    numero = float(input("Ingrese un número: "))
    return numero


def es_par(numero):
    """3-3: Retorna True si el número es par, False si es impar."""
    return numero % 2 == 0


def mostrar_numero_validado(desde, hasta):
    """3-4a: Muestra un número validado en el rango [desde, hasta]."""
    numero = pedir_numero_validado(desde, hasta)
    print(f"El número ingresado y validado es: {numero}")


def pedir_numero_validado(desde, hasta):
    """3-4b: Pide y retorna un número validado en el rango [desde, hasta]."""
    while True:
        numero = float(input(f"Ingrese un número entre {desde} y {hasta}: "))
        if desde <= numero <= hasta:
            return numero
        print(f"  ⚠  Número fuera de rango. Debe estar entre {desde} y {hasta}.")


def realizar_descuento(valor, porcentaje=5):
    """3-6: Aplica un descuento (por defecto 5%) al valor recibido y lo retorna."""
    descuento = valor * porcentaje / 100
    return valor - descuento


def pedir_operacion():
    """3-7: Pide y valida la operación: 's' para sumar, 'r' para restar."""
    while True:
        operacion = input("Ingrese la operación ('s' para sumar / 'r' para restar): ").strip().lower()
        if operacion in ('s', 'r'):
            return operacion
        print("  ⚠  Operación inválida. Ingrese 's' o 'r'.")


def calcular(num1, num2, operacion):
    """3-7: Realiza la operación indicada entre num1 y num2."""
    if operacion == 's':
        return num1 + num2
    elif operacion == 'r':
        return num1 - num2


# ─────────────────────────────────────────────
# PROTOTIPOS DE RESTAR (Ejercicio 3-5)
# ─────────────────────────────────────────────

def restar1(a, b):
    """Recibe dos enteros, retorna su diferencia."""
    return a - b


def restar2():
    """No recibe parámetros, pide los valores al usuario y retorna la diferencia."""
    a = int(input("Restar2 - Ingrese el primer número entero: "))
    b = int(input("Restar2 - Ingrese el segundo número entero: "))
    return a - b


def restar3(a, b):
    """Recibe dos enteros, muestra el resultado pero no retorna nada."""
    print(f"Restar3 - Resultado: {a} - {b} = {a - b}")


def restar4():
    """No recibe parámetros, pide los valores al usuario y muestra el resultado."""
    a = int(input("Restar4 - Ingrese el primer número entero: "))
    b = int(input("Restar4 - Ingrese el segundo número entero: "))
    print(f"Restar4 - Resultado: {a} - {b} = {a - b}")


# ─────────────────────────────────────────────
# PROGRAMA PRINCIPAL
# ─────────────────────────────────────────────

def main():
    separador = "\n" + "═" * 50 + "\n"

    # ── Ejercicio 3-1 ──────────────────────────────
    print(separador)
    print("EJERCICIO 3-1: Mostrar un número")
    mostrar_numero(42)
    mostrar_numero(-7.5)

    # ── Ejercicio 3-2 ──────────────────────────────
    print(separador)
    print("EJERCICIO 3-2: Pedir un número al usuario")
    numero = pedir_numero()
    print(f"Número recibido: {numero}")

    # ── Ejercicio 3-3 ──────────────────────────────
    print(separador)
    print("EJERCICIO 3-3: Verificar si un número es par")
    for n in [4, 7, 0, -3]:
        resultado = es_par(n)
        print(f"  ¿{n} es par? → {resultado}")

    # ── Ejercicio 3-4 ──────────────────────────────
    print(separador)
    print("EJERCICIO 3-4: Mostrar y pedir números con validación de rango")
    print(">> mostrar_numero_validado(1, 10):")
    mostrar_numero_validado(1, 10)
    print(">> pedir_numero_validado(50, 200):")
    numero_validado = pedir_numero_validado(50, 200)
    print(f"Número retornado: {numero_validado}")

    # ── Ejercicio 3-5 ──────────────────────────────
    print(separador)
    print("EJERCICIO 3-5: Cuatro prototipos de la función Restar")

    print("\n→ Restar1(int, int) -> int  [recibe parámetros y retorna]")
    resultado1 = restar1(10, 3)
    print(f"  restar1(10, 3) = {resultado1}")

    print("\n→ Restar2() -> int  [pide datos y retorna]")
    resultado2 = restar2()
    print(f"  Resultado retornado: {resultado2}")

    print("\n→ Restar3(int, int)  [recibe parámetros, no retorna]")
    restar3(15, 6)

    print("\n→ Restar4()  [pide datos, no retorna]")
    restar4()

    # ── Ejercicio 3-6 ──────────────────────────────
    print(separador)
    print("EJERCICIO 3-6: Aplicar descuento del 5%")
    numero1 = pedir_numero_validado(10, 100)
    precio_final = realizar_descuento(numero1)
    print(f"  Valor original  : {numero1:.2f}")
    print(f"  Descuento (5%)  : {numero1 * 0.05:.2f}")
    print(f"  Valor con descuento: {precio_final:.2f}")

    # ── Ejercicio 3-7 ──────────────────────────────
    print(separador)
    print("EJERCICIO 3-7: Sumar o restar dos números validados")
    print("Ingrese el primer número (entre 10 y 100):")
    numero1 = pedir_numero_validado(10, 100)
    print("Ingrese el segundo número (entre 10 y 100):")
    numero2 = pedir_numero_validado(10, 100)
    operacion = pedir_operacion()
    resultado = calcular(numero1, numero2, operacion)
    simbolo = "+" if operacion == 's' else "-"
    print(f"\n  {numero1} {simbolo} {numero2} = {resultado}")

    print(separador)
    print("Fin del programa.")


if __name__ == "__main__":
    main()