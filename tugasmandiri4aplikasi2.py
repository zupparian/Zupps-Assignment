import random

#print random emotion
def print_random_emotions(num_times):
    emotions = ["Joyful","Melancholic", "Radiant","Gloomy",
                "Blissful","Mournful","Elated","Sorrowful","Jubilant","Pensive"]

    for _ in range(num_times):
        emotion = random.choice(emotions)
        print(emotion)

# Memanggil fungsi untuk mencetak emosi acak x kali
print_random_emotions(12)