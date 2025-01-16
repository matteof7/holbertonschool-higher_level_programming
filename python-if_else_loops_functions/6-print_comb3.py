for i in range(0, 10):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:  # Dernière combinaison
            print(f"{i}{j}")
        else:
            print(f"{i}{j}, ", end="")
