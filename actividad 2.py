import tkinter as tk
import random

# Opciones del juego
opciones = ["Piedra", "Papel", "Tijera"]

# Marcadores
victorias = 0
derrotas = 0
empates = 0


def jugar(eleccion_jugador):
    global victorias, derrotas, empates

    eleccion_cpu = random.choice(opciones)

    if eleccion_jugador == eleccion_cpu:
        resultado = "Empate 🤝"
        empates += 1

    elif (
        (eleccion_jugador == "Piedra" and eleccion_cpu == "Tijera") or
        (eleccion_jugador == "Papel" and eleccion_cpu == "Piedra") or
        (eleccion_jugador == "Tijera" and eleccion_cpu == "Papel")
    ):
        resultado = "Ganaste 🎉"
        victorias += 1

    else:
        resultado = "Perdiste 😢"
        derrotas += 1

    # Actualizar interfaz
    etiqueta_resultado.config(
        text=f"Tú: {eleccion_jugador} | CPU: {eleccion_cpu}\n{resultado}"
    )

    marcador.config(
        text=f"Victorias: {victorias}  |  Derrotas: {derrotas}  |  Empates: {empates}"
    )


def reiniciar():
    global victorias, derrotas, empates
    victorias = 0
    derrotas = 0
    empates = 0

    etiqueta_resultado.config(text="Elige una opción")
    marcador.config(text="Victorias: 0  |  Derrotas: 0  |  Empates: 0")


ventana = tk.Tk()
ventana.title("Piedra, Papel o Tijera")
ventana.geometry("420x320")

# TIULO
titulo = tk.Label(
    ventana,
    text="🎮 Piedra, Papel o Tijera",
    font=("Arial", 16, "bold")
)
titulo.pack(pady=10)

# Botones
frame = tk.Frame(ventana)
frame.pack(pady=10)

tk.Button(frame, text="🪨 Piedra", width=12,
          command=lambda: jugar("Piedra")).grid(row=0, column=0, padx=5)

tk.Button(frame, text="📄 Papel", width=12,
          command=lambda: jugar("Papel")).grid(row=0, column=1, padx=5)

tk.Button(frame, text="✂ Tijera", width=12,
          command=lambda: jugar("Tijera")).grid(row=0, column=2, padx=5)

# Resultado
etiqueta_resultado = tk.Label(
    ventana,
    text="Elige una opción",
    font=("Arial", 12)
)
etiqueta_resultado.pack(pady=20)

# Marcador
marcador = tk.Label(
    ventana,
    text="Victorias: 0  |  Derrotas: 0  |  Empates: 0",
    font=("Arial", 12)
)
marcador.pack(pady=10)

# Botón reiniciar
tk.Button(
    ventana,
    text="🔄 Reiniciar",
    command=reiniciar
).pack(pady=10)

# Ejecutar
ventana.mainloop()
