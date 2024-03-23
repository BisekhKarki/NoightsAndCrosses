import random
import os.path
import json
random.seed()

def draw_board(board):
    #Displaying the board of noughtsandcrosses
    print(" -------------------")
    print(f"|  {board[0][0]}   |  {board[0][1]}   |  {board[0][2]}  |")
    print(" -------------------")
    print(f"|  {board[1][0]}   |  {board[1][1]}   |  {board[1][2]}  |")
    print(" -------------------")
    print(f"|  {board[2][0]}   |  {board[2][1]}   |  {board[2][2]}  |")
    print(" -------------------")
    pass 
    return board

def welcome(board):
    #Displaying the welcome message to the user 
    print("Welcome to the ""Unbeatable Noughts and Crosses""game")
    print("The board layout is shown below: ")
    #calling the function dra_board(board) to draw the board
    draw_board(board)
    pass
    return board

def initialise_board(board):
    #Setting spaces to " "
    for row in range(3):
        for col in range(3):
            board[row][col] = " "
    return board
    
def get_player_move(board):
    # develop code to ask the user for the cell to put the X in,
    while True:
        cell = int(input("Enter the cell between 1  to 9: "))
        if cell<1 and cell >= 9:
            print("Invalid cell number")
        else:
            row = ((cell-1) // 3) 
            col = ((cell-1)%3)
            if board[row][col]==" ":
                board[row][col] = "X"
                break
            else:
                print("Cell is already occupied..")
    return row, col   
    
def choose_computer_move(board):
    #Letting the computer to make a move
    while True:
        comp_cell = random.randint(1,9)
        row = ((comp_cell-1)//3)
        col = ((comp_cell-1)%3)
        if board[row][col] == " ":
            board[row][col]="O"
            break
    return row, col
              
def check_for_win(board, mark):
    #Checking the winner of the game
    if board[0][0] == board[0][1] == board[0][2] == mark:
        return True
    if board[1][0] == board[1][1] == board[1][2] == mark:
        return True
    if board[2][0] == board[2][1] == board[2][2] == mark:
        return True
    if board[0][0] == board[1][1] == board[2][2] == mark:
        return True
    if board[0][2] == board[1][1] == board[2][0] == mark:
        return True
    if board[0][0] == board[1][0] == board[2][0] == mark:
        return True
    if board[0][1] == board[1][1] == board[2][1] == mark:
        return True
    if board[0][2] == board[1][2] == board[2][2] == mark:
        return True  
    else:
        return False
    

def check_for_draw(board):
    #Checking if all cells are occupied
    for row in range(0,3):
        for col in range(0,3):
            if board[row][col]!= " ":
                return False    
    return True
        
def play_game(board):
    #Calling the function initialise_board(board) to set the space to " "
    initialise_board(board)
    #Drawing the board by calling the function draw_board(board)
    draw_board(board)
    while True: 
        #Letting the user to enter a cell   
        while True:
            cell = int(input("Enter the cell between 1  to 9: "))
            if cell<1 and cell >= 9:
                print("Invalid cell number")
            else:
                row = ((cell-1) // 3) 
                col = ((cell-1)%3)
                if board[row][col]==" ":
                    board[row][col] = "X"
                    break
                else:
                    print("Cell is already occupied..")
                    continue
        #Letting the computer to choose a cell
        while True:
            comp_cell = random.randint(1,9)
            row = ((comp_cell-1)//3)
            col = ((comp_cell-1)%3)
            if board[row][col]==" ":
                board[row][col]="O"
                break
            else:
                continue
        #Drawing the updated board
        draw_board(board)
        #To check if the player or the computer wins or both draws
        if check_for_win(board, "X"):
            return 1#returning 1 if player wins
        elif check_for_win(board, "O"):
            return -1#returning -1 if computer wins
        elif check_for_draw(board):
            return 0#returning 0 for draw
        
def menu():
    # 1 - Play the game
    print("\n")
    print("Enter 1 to Play the game")
    # 2 - Save score in file 'leaderboard.txt'
    print("Enter 2 to save the score in leaderboard.txt")
    # 3 - Load and display the scores from the 'leaderboard.txt'
    print("Enter 3 to load and display the scores from the 'leaderboard.txt'")
    #q - End the program
    print("Enter q to end the program")
    # get user input of either '1', '2', '3' or 'q'
    choice = input("Choose between '1', '2', '3' and 'q' : ")
    print("\n")
    return choice
    
def load_scores():
    #To load the score using the json module
        if os.path.isfile("leaderboard_2358423.txt"):
            with open("leaderboard_2358423.txt", 'r') as f:
                leaders = json.load(f) 
                return leaders
        else:
            raise FileNotFoundError("invalid file name")
        
def save_score(score):
   #Saving the score of the games played by tge players
    name = input("Enter your name: ")
    leaders={}
    try:
        if os.path.isfile("leaderboard_2358423.txt"):
            with open("leaderboard_2358423.txt",'r') as g:
                leaders=json.load(g)
        else:
            raise FileNotFoundError("Invalid file name")
        if name in leaders:
            leaders[name]= score + leaders[name]
        else:
            leaders[name] = score 
    except json.JSONDecodeError:
        print("Invalid..")
    with open("leaderboard_2358423.txt",'w') as f:
        json.dump(leaders,f)
        
def display_leaderboard(leaders):
    #Displaying the leaderboard scores
    print("Leaderboard is: ")
    new = sorted(leaders.items(), key=lambda x: x[1], reverse=True)
    for name, score in new:
        print(f"{name} :{score}")
    pass