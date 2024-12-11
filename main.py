import tkinter as tk
import requests

BASE_URL = "http://127.0.0.1:8000/api"  # URL base de la API de Laravel

def executeGetRequest(endpoint):
    """Función genérica para ejecutar solicitudes GET."""
    try:
        response = requests.get(endpoint)
        result_text.delete("1.0", tk.END)  # Limpia el área de resultados
        result_text.insert(tk.END, response.json())  # Muestra los resultados
    except Exception as e:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"Error: {str(e)}")

# Handlers para operaciones READ
def handleReadUsers():
    input_value = input_text.get("1.0", tk.END).strip()
    endpoint = f"{BASE_URL}/users" if not input_value else f"{BASE_URL}/users/{input_value}"
    executeGetRequest(endpoint)

def handleReadCategories():
    input_value = input_text.get("1.0", tk.END).strip()
    endpoint = f"{BASE_URL}/categories" if not input_value else f"{BASE_URL}/categories/{input_value}"
    executeGetRequest(endpoint)

def handleReadXboxGames():
    input_value = input_text.get("1.0", tk.END).strip()
    endpoint = f"{BASE_URL}/xbox-games" if not input_value else f"{BASE_URL}/xbox-games/{input_value}"
    executeGetRequest(endpoint)

def handleReadPs5Games():
    input_value = input_text.get("1.0", tk.END).strip()
    endpoint = f"{BASE_URL}/ps5-games" if not input_value else f"{BASE_URL}/ps5-games/{input_value}"
    executeGetRequest(endpoint)

def handleReadGameInfo():
    input_value = input_text.get("1.0", tk.END).strip()
    endpoint = f"{BASE_URL}/game-info" if not input_value else f"{BASE_URL}/game-info/{input_value}"
    executeGetRequest(endpoint)

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Administrador de Laravel API")
root.geometry("800x600")

# Título
title_label = tk.Label(root, text="Administrador", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Input para JSON o ID
input_label = tk.Label(root, text="Input (ID o JSON):", font=("Arial", 12))
input_label.pack()
input_text = tk.Text(root, height=5, width=80, font=("Arial", 10))
input_text.pack(pady=5)

# Botones para READ
read_frame = tk.Frame(root)
read_frame.pack(pady=10)

read_label = tk.Label(read_frame, text="READ Endpoints", font=("Arial", 12, "bold"))
read_label.grid(row=0, column=0, columnspan=5, pady=5)

read_users_button = tk.Button(read_frame, text="Users", command=handleReadUsers, width=15, bg="lightblue")
read_users_button.grid(row=1, column=0, padx=5)

read_categories_button = tk.Button(read_frame, text="Categories", command=handleReadCategories, width=15, bg="lightblue")
read_categories_button.grid(row=1, column=1, padx=5)

read_xbox_games_button = tk.Button(read_frame, text="Xbox Games", command=handleReadXboxGames, width=15, bg="lightblue")
read_xbox_games_button.grid(row=1, column=2, padx=5)

read_ps5_games_button = tk.Button(read_frame, text="PS5 Games", command=handleReadPs5Games, width=15, bg="lightblue")
read_ps5_games_button.grid(row=1, column=3, padx=5)

read_game_info_button = tk.Button(read_frame, text="Game Info", command=handleReadGameInfo, width=15, bg="lightblue")
read_game_info_button.grid(row=1, column=4, padx=5)

# Área de resultados
result_label = tk.Label(root, text="Results:", font=("Arial", 12))
result_label.pack()
result_text = tk.Text(root, height=15, width=90, font=("Arial", 10), state="normal")
result_text.pack(pady=5)

# Loop principal de la aplicación
root.mainloop()
