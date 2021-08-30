# Рисуем рекурсивный квадрат с помощью graphics 

import graphics as gr 

window = gr.GraphWin("Фрактальный квадрат", 600, 600) 
alfa = 0.1

def fractalRectangle(A, B, C, D, deep=30) :
    if deep < 1 : 
        return
    for M, N in (A, B), (B, C), (C, D), (D, A) :
        gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)     # *M *N - разворвоваричивание картежа в параметры функции 
    A1 = (A[0] * (1 - alfa) + B[0] * alfa, A[1] * (1 - alfa) + B[1] * alfa)
    B1 = (B[0] * (1 - alfa) + C[0] * alfa, B[1] * (1 - alfa) + C[1] * alfa)
    C1 = (C[0] * (1 - alfa) + D[0] * alfa, C[1] * (1 - alfa) + D[1] * alfa)
    D1 = (D[0] * (1 - alfa) + A[0] * alfa, D[1] * (1 - alfa) + A[1] * alfa)

    fractalRectangle(A1, B1, C1, D1, deep-1)


fractalRectangle((100, 100), (500, 100), (500, 500), (100, 500))

window.getMouse()
window.close() 