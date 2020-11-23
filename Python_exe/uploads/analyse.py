import re

with open("output.txt", "rb") as f :
    with open("output_analyzed.txt", "w") as f_final :
        line = str(f.readline())[2:-1]
        while(line != ""):
            
            if (line[-2:] == r"\n") :
                line = line[:-2]
            if (line[-2:] == r"\r") :
                line = line[:-2]
            line = line.replace("Key.esc", "\n[ESC]\n").replace(
                                "Key.enter", "\n[ENTER]\n").replace(
                                "Key.shift", "[SHIFT]").replace(
                                "Key.space", " ").replace(
                                "Key.ctrl_l","[CTRL]").replace(
                                "Key.tab", "\n")

            line = re.sub("\[SHIFT](.)","\g<1>",line)
            line = re.sub("Key.alt_gr(.)","\g<1>",line)
            while("Key.backspace" in line) :
                line = re.sub(".Key.backspace", "", line)

            if ("Key.left" in line) :
                cursor = line.index("Key.left")
                cursor_final = cursor
                size = 1
                while(line[cursor:cursor+size*8] == "Key.left"*size) :
                    cursor_final -= 1
                    size += 1
                size -=1
                # line_ahead = line[:cursor-size]
                # line_behind = line[cursor+size*8+1:]
                new_letter = line[cursor+size*8]
                # print(line[cursor-size] + " --- " + new_letter)
                # print(line_ahead[-10:])
                # print(line_behind[:10])
                # new_line = line_ahead + new_letter + line_behind
                line = re.sub("(.{%d})Key.left"%size,"%s\g<1>"%new_letter, line, 1)
                line = re.sub("(Key.left){%d}."%(size-1), "", line)
                print(line)

            f_final.write(line)

            line = str(f.readline())[2:-1]
