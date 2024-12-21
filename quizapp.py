from tkinter import *
from tkinter import messagebox as mb
import json

class quiz:
    def __init__(self):
        self.q_no = 0
        self.display_tittle()
        self.opt_selected = IntVer()
        self.opts = self.radio_buttons()
        self.display_options()
        self.data_size = len(question)
        self.correct = 0
    def display_result(self):
        wrong_count = self.data_size - self.correct
        correct = f"correct:{self.correct}"
        wrong = f"wrong:{wrong_count}"
        score = int(self.correct / self.data_size * 100)
        result = f"score:{score}%"
        mb.showinfo("result",f"{result}\n{correct}\n{wrong}")
    def check_ans(self,q_no):
        if self.pot_selection.get() == answer[q_no]:
            return True
    def next_btn(self):  
        if self.check_ans(self.q_no):
            self.correct += 1
        if self.q_no == self.data_size:
            self.display_result()
            root.destroy()
        else:
            self.display_question()
            self.display_options()
            
    def butter(self):   
        next_button = Button(root, text="next",command=self.next_btn,width=11,big="blue",fg="white",font=("ariel",16,"bold"))
        next_button.place(x=350,y=380)
        quit_button = Button(root,text="quit",command=root.destroy,width=5,bg="green",fg="white",font=("ariel",16,"bold"))
        quit_button.place(x=700,y=50)
    def display_oprations(self):
        val = 0
        self.opt_selected.set(0)
        for option in options[self.q_no]:
            self.opts[val]['text'] = option
            val +=1
    def display_question(self):  
        q_no = label(root,text=question[self.q_no], bg="black", fg="yellow",width=60,font=('ariel',16,'bold'),anchor='w')
        q_no = place(x=70,y=100)
    def display_tittle(self):
        tittle = lable(root,text="*TECH QUIZ*",width=50,bg="white",fg="black",font=("ariel",20,"bold"))
        tittle.place(x=0,y=2)
    def radio_buttons(self):
        q_list = []
        y_pos = 158
        while len(q_list)<4:
            radio_btn = rediobutton(root,text="",variable=self.opt_selection,value=len(list)+1,font=("ariel 14"))
            q_list.append(radio_btn)
            radio_btn.place(x=100,y=y_pos)
            y_pos += 40
        return q_list
root = Tk()
root.geometry(850*500)
root.tittle("TECH QUIZ")
root.configure(background="cyan")
with open('C:\\Users\\DHARMVEER\\dhar.json')as f:
    data = json.laod(f)
question = (data['questions'])
question = (data['options'])
answer = (data['answer'])
quiz = Quiz()
root.mainloop()




                
            
            
            
        
    