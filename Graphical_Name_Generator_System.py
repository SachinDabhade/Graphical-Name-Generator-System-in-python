# ************************** Graphical Naming System ***************************

# All credits go to Ramaneffect
# He wrote this code in cpp, i convert it in python

# Importing Libraries
from datetime import datetime

# This will record all the activities in the game
def record(ime):
    with open("record.txt", "a") as f:
        f.write(f"The \'Magic words\' game is played by {ime.capitalize()} on {datetime.now()}\n")

# Will stop the infinite loop by user permission
def play_quit():
    global ime
    play_game = input("\n\nEnter any key to continue or \"Q\" to quit: ")
    while True:
        if play_game.capitalize() == "Q":
            print(
                "Thanks for your valuable time that you spend with us....! We expect, you will be back soon...! Take care and stay home...!")
            exit()
        break

if __name__ == '__main__':

    while True:
        ime = input("\n\nEnter your name: \n\n")

        # Symnols generation as per the letters    
        for c in ime:
            c = c.upper()

            if (c == "A"):
                print("..######..\n..#....#..\n..######..\n..#....#..\n..#....#..\n\n")
    
            elif (c == "B"):
                print("..######..\n..#....#..\n..#####...\n..#....#..\n..######..\n\n")
    
            elif (c == "C"):
                print("..######..\n..#.......\n..#.......\n..#.......\n..######..\n\n")
    
            elif (c == "D"):
                print("..#####...\n..#....#..\n..#....#..\n..#....#..\n..#####...\n\n")
    
            elif (c == "E"):
                print("..######..\n..#.......\n..#####...\n..#.......\n..######..\n\n")
    
            elif (c == "F"):
                print("..######..\n..#.......\n..#####...\n..#.......\n..#.......\n\n")
    
            elif (c == "G"):
                print("..######..\n..#.......\n..#####...\n..#....#..\n..#####...\n\n")
    
            elif (c == "H"):
                print("..#....#..\n..#....#..\n..######..\n..#....#..\n..#....#..\n\n")
    
            elif (c == "I"):
                print("..######..\n....##....\n....##....\n....##....\n..######..\n\n")
    
            elif (c == "J"):
                print("..######..\n....##....\n....##....\n..#.##....\n..####....\n\n")
    
            elif (c == "K"):
                print("..#...#...\n..#..#....\n..##......\n..#..#....\n..#...#...\n\n")
    
            elif (c == "L"):
                print("..#.......\n..#.......\n..#.......\n..#.......\n..######..\n\n")
    
            elif (c == "M"):
                print("..#....#..\n..##..##..\n..#.##.#..\n..#....#..\n..#....#..\n\n")
    
            elif (c == "N"):
                print("..#....#..\n..##...#..\n..#.#..#..\n..#..#.#..\n..#...##..\n\n")
            
            elif (c == "O"):
                print("..######..\n..#....#..\n..#....#..\n..#....#..\n..######..\n\n")
            
            elif (c == "P"):
                print("..######..\n..#....#..\n..######..\n..#.......\n..#.......\n\n")
            
            elif (c == "Q"):
                print("..######..\n..#....#..\n..#.#..#..\n..#..#.#..\n..######..\n\n")
            
            elif (c == "R"):
                print("..######..\n..#....#..\n..#.##...\n..#...#...\n..#....#..\n\n")
            
            elif (c == "S"):
                print("..######..\n..#.......\n..######..\n.......#..\n..######..\n\n")
            
            elif (c == "T"):
                print("..######..\n....##....\n....##....\n....##....\n....##....\n\n")
            
            elif (c == "U"):
                print("..#....#..\n..#....#..\n..#....#..\n..#....#..\n..######..\n\n")
            
            elif (c == "V"):
                print("..#....#..\n..#....#..\n..#....#..\n...#..#...\n....##....\n\n")
            
            elif (c == "W"):
                print("..#....#..\n..#....#..\n..#.##.#..\n..##..##..\n..#....#..\n\n")
            
            elif (c == "X"):
                print("..#....#..\n...#..#...\n....##....\n...#..#...\n..#....#..\n\n")
            
            elif (c == "Y"):
                print("..#....#..\n...#..#...\n....##....\n....##....\n....##....\n\n")
            
            elif (c == "Z"):
                print("..######..\n......#...\n.....#....\n....#.....\n..######..\n\n")
            
            elif (c == " "):
                print("..........\n..........\n..........\n..........\n\n")
            
            elif (c == "."):
                print("----..----\n\n")
        
        print("Thanks for playing with us...")
        record(ime)
        play_quit()
