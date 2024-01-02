from tkinter import *
import random
from Result import *
def main():
    root = Tk()
    root.title("Welcome")
    root.geometry("1366x768")
    root.configure(bg="sky blue")
    user_score=0 
    computer_score=0
    label1 = Label(root, text="Welcome", fg="yellow",bg="dark blue", width=57, font="times 30 bold", height=2)
    label1.place(x=683, y=50, anchor="center")

    label2 = Label(root, text="Let's play Rock, Paper, Scissor--click your choice!", fg="blue",bg="sky blue",width=40, height=3, font="times 20 bold")
    label2.place(x=683, y=300, anchor="center")

    btn1 = Button(root, text="ROCK", font="times 20 bold", command=lambda:result("rock"), fg="#4267B2", bg="white", padx=20, pady=15)
    btn1.place(x=100, y=400)

    btn2 = Button(root, text="PAPER", font="times 20 bold", command=lambda:result("paper"), fg="#4267B2", bg="white", padx=20, pady=15)
    btn2.place(x=600, y=400)

    btn3 = Button(root, text="SCISSOR", font="times 20 bold", command=lambda:result("scissor"), fg="#4267B2", bg="white", padx=20, pady=15)
    btn3.place(x=1000, y=400)
    #functions
    def declare_result(result,u_input,c_input,user_score,computer_score):#show a quick result for each match
        top=Toplevel(root)
        top.configure(bg="sky blue")
        top.geometry("450x250")
        top.title("result")
        u_score=0
        c_score=0
        u_score+=user_score
        c_score+=computer_score
        
        lb1=Label(top,text="Your input:"+u_input,fg="green",bg="sky blue",font="times 20 bold",width=50)
        lb1.pack()
        
        lb1=Label(top,text="Computer input:"+c_input,fg="green",bg="sky blue",font="times 20 bold",width=50)
        lb1.pack()
        
        lb1=Label(top,text=result,fg="blue",bg="sky blue",font="times 35 bold",width=100)
        lb1.pack()
        
        btn1 = Button(top, text="Try again", font="times 20 bold", command=lambda:top.destroy(), fg="green", bg="white", padx=20, pady=15)
        btn1.pack(side=LEFT)
        
        btn4 = Button(top, text="Scores", font="times 20 bold", command=lambda:final_scores(u_score,c_score), fg="red", bg="white", padx=20, pady=15)
        btn4.pack(side=RIGHT) 

    def result(u_input):#calculte a result based on inputs
        options=["rock","paper","scissor"]
        c_input=random.choice(options)
        if u_input==c_input:
            declare_result("It is a Tie!",u_input,c_input,user_score,computer_score)
            
        elif u_input=="rock":
            if c_input=="paper":
                computer_score+=1
                declare_result("Computer Win",u_input,c_input,user_score,computer_score)
            elif c_input=="scissor":
                user_score+=1
                declare_result("You Win",u_input,c_input,user_score,computer_score)
                
        elif u_input=="paper":
            if c_input=="rock":
                user_score+=1
                declare_result("You Win",u_input,c_input,user_score,computer_score)
            elif c_input=="scissor":
                computer_score+=1
                declare_result("Computer Win",u_input,c_input,user_score,computer_score)
                
        elif u_input=="scissor":
            if c_input=="paper":
                user_score+=1
                declare_result("You win",u_input,c_input,user_score,computer_score)
            elif c_input=="rock":
                computer_score+=1
                declare_result("Computer Win",u_input,c_input,user_score,computer_score)   
# running the main loop
    root.mainloop()    
if __name__ == '__main__':
    main()
