import csv
import tkinter as tk
from operator import index
from tkinter import filedialog

if __name__ == '__main__':
    ap_er_tracker = filedialog.askopenfilename(
        title="Select AP ER tracker file",
        filetypes=[("CSV Files", "*.csv")]
    )

    nametracker = "nametracker.csv"

    with open(ap_er_tracker, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        ap_entrances = [line for line in reader]

    names = {}
    names_list= []
    with open(nametracker, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for line in reader:
            names[line["Archipelago"]] = line["Scipio"]
            names_list.append(line["Archipelago"])

    print(ap_entrances)
    print(names)
    print(names_list)

    worlds = {}
    prev_world = (None,1)
    for i,world in enumerate(names):
        if names[world] is not None:
            continue
        worlds[world] = [i+1,None]
        if prev_world[0] is not None:
            worlds[prev_world[0]][1] = i-1
        prev_world= (world,i)
    worlds[prev_world[0]][1] = i
    print(worlds)

    with open("output.csv", mode='w', newline='', encoding='utf-8') as file:
        file.write("#tunic\n")
        for entrance in ap_entrances:
            if entrance["To"] == "":
                continue
            try:
                entrance_translation = names[entrance["From"]]
                destination_translation = names[entrance["To"]]

                entrance_index = names_list.index(entrance["From"])
                destination_index = names_list.index(entrance["To"])
                for world_range in worlds:
                    if worlds[world_range][0] <= entrance_index <= worlds[world_range][1]:
                        entrance_world = world_range
                    if worlds[world_range][0] <= destination_index <= worlds[world_range][1]:
                        destination_world = world_range
                file.write(f"tunic,{entrance_world},{entrance_translation},warp,{destination_world},{destination_translation},\n")
            except:
                pass





