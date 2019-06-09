import taglib as tl
import sys, osoptomization technique 
from shutil import copy2

#---------------------- || run through each artists and albums and add to a dictionary 
#optomization technique || once that is finished make the directory structure first
#---------------------- || that way you don't need to keep checking whether a directory exists for each song.
#                       || I don't know if this will be faster but it's worth a try 

def main():
    if len(sys.argv) != 3:
        print('Proper usage: itransfer.py <input path> <output path>')
        print('input path = path to your mounted ipod')
        print('output path = path to your desired output')
        exit(1) 

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    input_path = os.path.join(input_path, "iPod_Control/Music/")

    if not os.path.isdir(os.path.join(input_path)):
        print("There is no ipod mointed on ".format(syst.argv[1]))

    if not os.path.isdir(output_path): #Checks to see if the output directory exists and
        if output_path[0:2] == "~/":   #Creates the directory if it isn't already there
            os.mkdir(output_path)      
        else:
            output_path = os.path.join("~", output_path) #TODO: find why this is giving a FileNotFoundError
            os.mkdir(output_path)


    for path in os.listdir(input_path):
        tmp_path = os.path.join(input_path, path)
        for mp3 in os.listdir(tmp_path):
            song = tl.File(os.path.join(tmp_path, mp3))
            try:

                artist_path = os.path.join(output_path, song.tags['ARTIST'][0])
                album_path = os.path.join(artist_path, song.tags['ALBUM'][0])
                song_path = os.path.join(album_path, song.tags['TITLE'][0])

                if not os.path.isdir(artist_path):
                    os.mkdir(artist_path)

                if not os.path.isdir(album_path):
                    os.mkdir(album_path)

                copy2(os.path.join(tmp_path, mp3), song_path + '.mp3')
                print('copying: ' + song.tags['TITLE'][0])

            except:
                print("", end='')


if __name__ == "__main__":
    main()
