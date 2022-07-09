aquarium_length = int(input())
aquarium_width = int(input())
aquarium_hight = int(input())
aquarium_volume_taken_percent = float(input())

aquarium_volume_whole = aquarium_hight * aquarium_width * aquarium_length
aquarium_volume_taken = aquarium_volume_taken_percent * (aquarium_volume_whole / 1000) / 100
aquarium_volume = (aquarium_volume_whole / 1000) - aquarium_volume_taken

print(aquarium_volume)