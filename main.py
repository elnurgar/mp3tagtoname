from tinytag import TinyTag
import os

unsupported_symbols = ['"', '*', '<', '>', '?', '\\', '|', '/', ':']
list = []
new_list = []
last_list = []
exclude_list = []
directory = input("Please input the directory name: ")
for i in os.listdir(directory + '/'):
    if ".mp3" in i:
        list.append(i)
for i in list:
    try:
        tag = TinyTag.get(directory + "/" + i, encoding="cp1251")
    except:
        new_list.append([i, i])
    if tag.artist == None and tag.title == None:
        new_list.append([i, i])
    elif tag.title == None:
        new_list.append([i, tag.artist + ".mp3"])
    elif tag.artist == None:
        new_list.append([i, tag.title + ".mp3"])
    else:
        new_list.append([i, tag.artist + "-" + tag.title + ".mp3"])
for i in new_list:
    if [True for a in unsupported_symbols if a in i[1]] or i[1] == "-.mp3":
        exclude_list.append(i)
    else:
        last_list.append(i)
for i in last_list:
    os.rename(f"{directory}/{i[0]}", f"{directory}/{i[1]}")
with open("failed.txt", "w", encoding="utf-8") as file:
    for i in exclude_list:
        file.write(i[0] + "\n")
