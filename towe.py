def move_tower(height, from_rod, to_rod, with_rod):
    if height < 1:
        return
    move_tower(height - 1, from_rod, with_rod, to_rod)
    print(f"Move disk from rod {from_rod} to rod {to_rod}")
    move_tower(height - 1, with_rod, to_rod, from_rod)
N = 3  
move_tower(N, 1, 3, 2)