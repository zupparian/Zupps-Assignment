import random

def generate_emotion_title(name):
    # Daftar adjective
    adjectives = ["Joyful", "Melancholic", "Radiant", "Gloomy", "Blissful", 
                  "Mournful", "Elated",  "Sorrowful", "Jubilant", "Pensive"]
    
    # Memilih adjective secara acak
    adjective = random.choice(adjectives)
    
    # Menghasilkan dan mengembalikan gelar emosi
    return f"{name} the {adjective}"

# Meminta input nama dari pengguna
user_name = input("Enter your name: ")

# Menghasilkan gelar emosi
emotion_title = generate_emotion_title(user_name)

# Mencetak hasil
print("Your emotion title is:",emotion_title)