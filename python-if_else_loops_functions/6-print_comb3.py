for i in range(0, 10):
    for j in range(i + 1, 10):
     print(f"{i}{j}", end=", " if i != 8 or j != 9 else "\n")
