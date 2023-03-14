from tkinter import *
import random

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
        
        #Kontrollige, kas mängija on kaotanud
        if mis >= max_mis:
            result_lbl.config(text=f'Mäng läbi. Sõna oli {word}!.',font='Arial 15')

instructions_lbl = Label(mang, text='Arva ära sõna!',font='Arial 15',bg='#8c8c8c', fg='#404040')      
word_lbl = Label(mang, text='',bg='#8c8c8c',font='Arial 18')
guess_entry = Entry(mang, width=1,font='Arial 12')
check_btn = Button(mang, text='Kontrollima', bg='#d7f7ed',width='14',font='Arial 12',command=check_guess)
result_lbl = Label(mang, text='',bg='#8c8c8c')
mis_lbl = Label(mang, text=f'Vaed: {mis}/{max_mis}',fg='#00bf13',bg='#d4d6d5',font='Arial 12',width='14')
new_btn = Button(mang, text='Uus mäng', bg='#ecffcf',fg='#03bf00',width='18',font='Arial 12',command=new)

new()

instructions_lbl.pack(pady=10)
word_lbl.pack(pady=10)
guess_entry.pack(pady=10)
check_btn.pack(pady=10)
result_lbl.pack(pady=8)
mis_lbl.pack(pady=8)
new_btn.pack(pady=10)

mang.geometry('500x500')
mang.configure(background='#8c8c8c')
mang.mainloop()
