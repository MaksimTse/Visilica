from tkinter import *
import random
import turtle
t = turtle.Turtle()
mang = Tk()
mang.title('Arva ära Sõna!')

a = ['tiiger', 'lõvi', 'kaelkirjak', 'elevant', 'ahv', 'zeebra']
b = ['kohv', 'tee', 'mahl', 'soda', 'vesi', 'limonaad']
c = ['pitsa', 'hamburger', 'sushi', 'pasta', 'salat', 'võileib']

word = ''
guesses = ''
mis = 0
max_mis = 5

def new():
    global word
    global guesses
    global mis
    global word_list
    
    #Tühjendage mängu muutujad
    word = ''
    guesses = ''
    mis = 0
    
    word_list = [a, b, c]
    word = random.choice(random.choice(word_list))
    
    #Tühjendage guess kirje ja result silt
    guess_entry.delete(0, END)
    result_lbl.config(text='')
    
    #Värskendage sõnasilti iga tähe alljoontega
    disp_word = ''
    for letter in word:
        disp_word += '_ '
    word_lbl.config(text=disp_word)

def check_guess():
    global word
    global guesses
    global mis
    
    #Hankige guess sisestuskastist
    guess = guess_entry.get().lower()
    
    #Tühjendage guess kirje
    guess_entry.delete(0, END)
    
    if len(guess) != 1:
        result_lbl.config(text='Palun sisestage üks täht.')
    if guess in guesses:
        result_lbl.config(text='Sa juba arvasid seda kirja.') 
    #Lisage oletus oletuste loendisse
    guesses += guess
    
    # Kontrollige, kas guess on sõna järjendis
    if guess in word:
        #Värskendage sõna silt õige oletusega
        display_word = ''
        for letter in word:
            if letter in guesses:
                display_word += letter + ' '
            else:
                display_word += '_ '
        word_lbl.config(text=display_word)
        
        #Kontrollige, kas mängija on võitnud
        if '_' not in display_word:
            result_lbl.config(text='Palju õnne! Sa arvasid sõna.',font='Arial 12')
            mis = 0
            mis_lbl.config(text=f'Vead: {mis}/{max_mis}',fg='green')
            
    else:
        #Suurendage vigade arvu ja värskendage vigade silti
        mis += 1
        mis_lbl.config(text=f'Vead: {mis}/{max_mis}',fg='red')
        
        if mis == 1:
            tahvel1=Canvas(mang,width=320,height=320,bg='#8c8c8c')
            img=PhotoImage(file='shield-png-1.png')
            tahvel1.create_image(2,2,image=img,anchor=NW)
            tahvel1.grid(row=0,column=1)
        elif mis == 2:
            tahvel2=Canvas(mang,width=320,height=320,bg='#8c8c8c')
            img=PhotoImage(file='shield-png-1.png')
            tahvel2.create_image(2,2,image=img,anchor=NW)
            tahvel2.grid(row=0,column=1)
        elif mis == 3:
            tahvel3=Canvas(mang,width=320,height=320,bg='#8c8c8c')
            img=PhotoImage(file='shield-png-1.png')
            tahvel3.create_image(2,2,image=img,anchor=NW)
            tahvel3.grid(row=0,column=1)
        elif mis == 4:
            tahvel4=Canvas(mang,width=320,height=320,bg='#8c8c8c')
            img=PhotoImage(file='shield-png-1.png')
            tahvel4.create_image(2,2,image=img,anchor=NW)
            tahvel4.grid(row=0,column=1)
        elif mis == 5:
            tahvel5=Canvas(mang,width=320,height=320,bg='#8c8c8c')
            img=PhotoImage(file='shield-png-1.png')
            tahvel5.create_image(2,2,image=img,anchor=NW)
            tahvel5.grid(row=0,column=1)
        
        #Kontrollige, kas mängija on kaotanud
        if mis >= max_mis:
            result_lbl.config(text=f'Mäng läbi. Sõna oli {word}!.',font='Arial 15')

f=Frame(mang,bg='#8c8c8c')

instructions_lbl = Label(f, text='Arva ära sõna!',font='Arial 15',bg='#8c8c8c', fg='#404040')
instructions_lbl.pack(pady=10)

word_lbl = Label(f, text='',bg='#8c8c8c',font='Arial 18')
word_lbl.pack(pady=10)

guess_entry = Entry(f, width=1,font='Arial 12')
guess_entry.pack(pady=10)

check_btn = Button(f, text='Kontrollima', bg='#d7f7ed',width='14',font='Arial 12',command=check_guess)
check_btn.pack(pady=10)

result_lbl = Label(f, text='',bg='#8c8c8c')
result_lbl.pack(pady=8)

mis_lbl = Label(f, text=f'Vaed: {mis}/{max_mis}',fg='#00bf13',bg='#d4d6d5',font='Arial 12',width='14')
mis_lbl.pack(pady=8)

new_btn = Button(f, text='Uus mäng', bg='#ecffcf',fg='#03bf00',width='18',font='Arial 12',command=new)
new_btn.pack(pady=100)

new_btn = Label(f, bg='#8c8c8c',width='70')
new_btn.pack(pady=5)

f.grid(row=0,column=4)

new()

mang.geometry('900x500')
mang.configure(background='#8c8c8c')
mang.mainloop()
