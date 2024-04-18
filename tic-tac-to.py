from tkinter import*
import random


window = Tk()
window.geometry('500x500')
window.title("Tic-Tac-To Game")
window.config(background="gray")
window.resizable(width=False, height=False)

strt_cont = 0

players = ["X", "O"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]


def empty_spaces():
    spaces = 9
    
    for row in range(3):
       for column in range(3):
         if buttons[row][column]['text'] != '':
           spaces -= 1
          
    if spaces == 0:
      return False
    else:
      return True


def next_turn(row , column, frame, player_one, player_two):
     global player
     
     if buttons[row][column]['text'] == "" and check_winner() is False:
       
          if player == players[0]:
             buttons[row][column]['text'] = player
             player_two.config(highlightthickness='0', highlightbackground='gray')
           
             if check_winner() is False:
                player  = players[1]
                player_one.config(highlightthickness='2', highlightbackground='white')
                
                
             elif check_winner is True:
                 player_two.config(bg='green')
                 
             elif check_winner == 'Tie':
               player_one.config(text=('Tie'))
               player_two.config(text=('Tie'))
               
          else:
            
              buttons[row][column]['text'] = player
              player_one.config(highlightthickness='0', highlightbackground='gray')
           
              if check_winner() is False:
                   player  = players[0]
                   player_two.config(highlightthickness='2', highlightbackground='white')
                   
              elif check_winner() is True:
                 player_one.config(bg='green')
                 
              elif check_winner == 'Tie':
               player_two.config(text=('Tie'))
               
               
def check_winner():
        for row in range(3):
          if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            
             buttons[row][0].config(bg='green')
             buttons[row][1].config(bg='green')
             buttons[row][2].config(bg='green')
             return True
           
        for column in range(3):
          if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            
             buttons[0][column].config(bg='green')
             buttons[1][column].config(bg='green')
             buttons[2][column].config(bg='green')
             return True
           
        if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] !="":
          
             buttons[0][0].config(bg='green')
             buttons[1][1].config(bg='green')
             buttons[2][2].config(bg='green')
             return True
        
        elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] !="":
          
             buttons[0][2].config(bg='green')
             buttons[1][1].config(bg='green')
             buttons[2][0].config(bg='green')
             return True
        
        elif empty_spaces() is False:
          for row in range(3):
            for column in range(3):
              buttons[row][column].config(bg='yellow')
          return  'Tie'
          
        else:
          return False
        
  
def start(num, first, second):

  def new_game():
    global player
    global strt_cont

  
    for row in range(3):
      for column in range(3):
        buttons[row][column].config(text='')
        
    game_frame.destroy()
    tic_tac_frame.destroy()
    strt_cont = 1
        
    first_page()
  
  global strt_cont
  strt_cont += num
  
  first_player = first.get()
  second_player = second.get()

  
  if first_player and second_player != "":
    
    vs_label = Label(window, text='VS', font=("Arial", 22), bg='gray', fg='yellow')
    vs_label.place(relx='0.435', rely='0.44')     
  
    if strt_cont >= 2:
    
      game_frame = Frame(window, bg='gray')
      game_frame.place(x=1, y=1, width=500, height=500)
    
      player1_name = Label(game_frame,text=first_player, font=('Arial', 20), fg='#66fc03', bg="gray",highlightthickness='2',highlightbackground='white')
      player1_name.place(x=170, y=10)

      player2_name = Label(game_frame,text=second_player, font=('Arial', 20), fg="#66fc03", bg="gray")
      player2_name.place(x=170, y=450)
    
      tic_tac_frame = Frame(game_frame)
      tic_tac_frame.pack(expand=True, fill='both', padx=80, pady=80)
    
      new_game1 = Button(game_frame, text='New Game', bg='green', fg='yellow', activebackground='green', activeforeground='yellow', command = new_game)
      new_game1.place(x=4, y=10)
    
      tic_tac_frame.columnconfigure((0, 1, 2), weight=1)
      tic_tac_frame.rowconfigure((0, 1, 2), weight=1)
    
      for row in range(3):
        for column in range(3):
          buttons[row][column] = Button(tic_tac_frame,text='', font=("Arial", 60), width=5, height=2, command =lambda row=row, column=column : next_turn(row, column, game_frame, player1_name, player2_name))
          buttons[row][column].grid(column=column, row=row, sticky='nswe')

  else:
    error_label = Label(window, text='Enter the names', font=("Arial", 12), bg='gray', fg='red')
    error_label.place(relx='0.435', rely='0.44')

def first_page():
  
  game_title = Label(window, text='Tic-Tac-To Game', font=('Arial', 22), bg="gray", fg="#66fc03")
  game_title.place(relx='0.29', rely='0.03')

  instruction_label = Label(window, text="Instructions: Player should look for the symbol in the book before entering.", font=('Arial', 10), bg="gray", fg="white")
  instruction_label.place(relx='0.05', rely='0.15')

  player1 = Entry(window, font=('Arial', 20), fg='#66fc03', bg="gray")
  player1.place(relx='0.2', rely='0.27')
  
  player2 = Entry(window, font=('Arial', 20), fg="#66fc03", bg="gray")
  player2.place(relx='0.2', rely='0.63')
  
  red_label = Label(window,bg='red', fg='white',relief='solid',highlightthickness='2',highlightbackground='white',text=player, width=5, height=2)
  red_label.place(relx='0.87', rely='0.27')
  
  for find_op in players:
    if find_op != player:
    
     blue_label = Label(window,bg='blue',fg='white', text=find_op, width=5, height=2) 
     blue_label.place(relx='0.87', rely='0.63')

  game_start_button = Button(window,text='Start', font=('Arial', 22), width=10, bg='white', fg="black", command=lambda: start(1, first=player1, second=player2))
  game_start_button.place(relx='0.34', rely='0.8')
  
first_page()

window.mainloop()
    
