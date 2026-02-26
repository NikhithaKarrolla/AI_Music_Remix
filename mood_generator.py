def get_mood_settings(mood):

    if mood == "Happy":
        return 1.3, 3
    elif mood == "Sad":
        return 0.8, -3
    elif mood == "Energetic":
        return 1.5, 4
    elif mood == "Calm":
        return 0.7, -2
    else:
        return 1.0, 0