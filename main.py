import tkinter as tk
import requests
import json

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


def executeRequest(method, endpoint, data=None):
    """Función genérica para ejecutar solicitudes."""
    try:
        if method == "GET":
            response = requests.get(endpoint)
        elif method == "POST":
            response = requests.post(endpoint, json=data)
        elif method == "PUT":
            response = requests.put(endpoint, json=data)
        elif method == "DELETE":
            response = requests.delete(endpoint)
        else:
            raise ValueError("Método no válido")

        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, response.json())
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

# Handlers para CREATE
def handleCreateUsers():
    data = getJsonInput()
    if data:
        executeRequest("POST", f"{BASE_URL}/users", data)

def handleCreateCategories():
    data = getJsonInput()
    if data:
        executeRequest("POST", f"{BASE_URL}/categories", data)

def handleCreateXboxGames():
    data = getJsonInput()
    if data:
        executeRequest("POST", f"{BASE_URL}/xbox-games", data)

def handleCreatePs5Games():
    data = getJsonInput()
    if data:
        executeRequest("POST", f"{BASE_URL}/ps5-games", data)

# Handlers para UPDATE
def handleUpdateUsers():
    id_value, data = getIdAndJsonInput()
    if id_value and data:
        executeRequest("PUT", f"{BASE_URL}/users/{id_value}", data)

def handleUpdateCategories():
    id_value, data = getIdAndJsonInput()
    if id_value and data:
        executeRequest("PUT", f"{BASE_URL}/categories/{id_value}", data)

def handleUpdateXboxGames():
    id_value, data = getIdAndJsonInput()
    if id_value and data:
        executeRequest("PUT", f"{BASE_URL}/xbox-games/{id_value}", data)

def handleUpdatePs5Games():
    id_value, data = getIdAndJsonInput()
    if id_value and data:
        executeRequest("PUT", f"{BASE_URL}/ps5-games/{id_value}", data)

# Handlers para DELETE
def handleDelete(endpoint, id_value):
    if "categories" in endpoint or "game-info" in endpoint:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Error: Esta operación está prohibida.")
    else:
        executeRequest("DELETE", f"{endpoint}/{id_value}")

def handleDeleteUsers():
    id_value = getIdInput()
    if id_value:
        handleDelete(f"{BASE_URL}/users", id_value)

def handleDeleteXboxGames():
    id_value = getIdInput()
    if id_value:
        handleDelete(f"{BASE_URL}/xbox-games", id_value)

def handleDeletePs5Games():
    id_value = getIdInput()
    if id_value:
        handleDelete(f"{BASE_URL}/ps5-games", id_value)

# Helpers para obtener datos de entrada
def getJsonInput():
    try:
        data = json.loads(input_text.get("1.0", tk.END).strip())
        return data
    except json.JSONDecodeError:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Error: El input no es un JSON válido.")
        return None

def getIdAndJsonInput():
    id_value = input_text.get("1.0", tk.END).strip()
    if not id_value.isdigit():
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Error: Debes proporcionar un ID válido.")
        return None, None

    data = getJsonInput()
    return id_value, data

def getIdInput():
    id_value = input_text.get("1.0", tk.END).strip()
    if not id_value.isdigit():
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Error: Debes proporcionar un ID válido.")
        return None
    return id_value

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

# Botones CREATE
create_frame = tk.Frame(root)
create_frame.pack(pady=10)

create_label = tk.Label(create_frame, text="CREATE Endpoints", font=("Arial", 12, "bold"))
create_label.grid(row=0, column=0, columnspan=4, pady=5)

tk.Button(create_frame, text="Create User", command=handleCreateUsers, width=15, bg="lightgreen").grid(row=1, column=0, padx=5)
tk.Button(create_frame, text="Create Category", command=handleCreateCategories, width=15, bg="lightgreen").grid(row=1, column=1, padx=5)
tk.Button(create_frame, text="Create Xbox Game", command=handleCreateXboxGames, width=15, bg="lightgreen").grid(row=1, column=2, padx=5)
tk.Button(create_frame, text="Create PS5 Game", command=handleCreatePs5Games, width=15, bg="lightgreen").grid(row=1, column=3, padx=5)

# Botones UPDATE
update_frame = tk.Frame(root)
update_frame.pack(pady=10)

update_label = tk.Label(update_frame, text="UPDATE Endpoints", font=("Arial", 12, "bold"))
update_label.grid(row=0, column=0, columnspan=4, pady=5)

tk.Button(update_frame, text="Update User", command=handleUpdateUsers, width=15, bg="lightyellow").grid(row=1, column=0, padx=5)
tk.Button(update_frame, text="Update Category", command=handleUpdateCategories, width=15, bg="lightyellow").grid(row=1, column=1, padx=5)
tk.Button(update_frame, text="Update Xbox Game", command=handleUpdateXboxGames, width=15, bg="lightyellow").grid(row=1, column=2, padx=5)
tk.Button(update_frame, text="Update PS5 Game", command=handleUpdatePs5Games, width=15, bg="lightyellow").grid(row=1, column=3, padx=5)

# Botones DELETE
delete_frame = tk.Frame(root)
delete_frame.pack(pady=10)

delete_label = tk.Label(delete_frame, text="DELETE Endpoints", font=("Arial", 12, "bold"))
delete_label.grid(row=0, column=0, columnspan=4, pady=5)

tk.Button(delete_frame, text="Delete User", command=handleDeleteUsers, width=15, bg="lightcoral").grid(row=1, column=0, padx=5)
tk.Button(delete_frame, text="Delete Xbox Game", command=handleDeleteXboxGames, width=15, bg="lightcoral").grid(row=1, column=1, padx=5)
tk.Button(delete_frame, text="Delete PS5 Game", command=handleDeletePs5Games, width=15, bg="lightcoral").grid(row=1, column=2, padx=5)


# Área de resultados
result_label = tk.Label(root, text="Results:", font=("Arial", 12))
result_label.pack()
result_text = tk.Text(root, height=15, width=90, font=("Arial", 10), state="normal")
result_text.pack(pady=5)

# Loop principal de la aplicación
root.mainloop()
