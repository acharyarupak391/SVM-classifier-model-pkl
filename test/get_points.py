# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 19:01:05 2020

@author: Rupak
"""

import tkinter as tk
import numpy as np

class GUI:
    def __init__(self):
        self.curr_cls = 'A'
        self.color = '#ef8686'
        
        self.X = np.array([])
        self.Y = np.array([])
        
        self.x_pos = np.array([])
        self.y_pos = np.array([])
        self.pos_class = np.array([])
        self.point_count = 1
        self.arc = {
               "center": {"x": 10, "y": 10},
               "radius": 50
               }
        self.m = tk.Tk()
        self.m.title('Plot points for neural-network')
        window = {
                "width": 1000,
                "height": 600,
                "x(left)": 200,
                "y(top)": 100
                } 
        self.m.geometry(f"{window['width']}x{window['height']}+{window['x(left)']}+{window['y(top)']}")

        ''' 
            frame and button, label for class A & B
        '''
        self.frm = tk.Frame(self.m, highlightthickness=1, highlightbackground="black")
        self.frm.grid(row=0, column=0, padx=50)
        
        self.btn = tk.Button(self.frm,text="Change class", borderwidth=2, background=self.color, command=self.btn_click)
        self.btn.pack(pady=15)
        
        self.lbl = tk.Label(self.frm, text="Current class: {}".format(self.curr_cls))
        self.lbl.pack()
        
        ''' 
            frame and button for entering random points in canvas
        '''
        self.tst_frm = tk.Frame(self.m, highlightthickness=1, highlightbackground="black")
        self.tst_frm.grid(row=1, column=0, padx=50)
        
        self.enter_btn = tk.Button(self.tst_frm,text="Submit data", background="white", command=self.sub_btn_click)
        self.enter_btn.pack()
        
        ''' 
            frame and button for calculation
        '''
        self.cal_frm = tk.Frame(self.m, highlightthickness=0, highlightbackground="black")
        self.cal_frm.grid(row=2, column=0, padx=50)
        
        self.cal_lbl = tk.Label(self.cal_frm, text="how many consequtive points to plot")
        self.cal_lbl.pack(pady=5)
        
        self.cal_entry = tk.Entry(self.cal_frm, bd=2, highlightthickness=1, highlightbackground='green')
        self.cal_entry.insert(0, self.point_count)
        self.cal_entry.pack(pady=5)
        
        self.cal_btn = tk.Button(self.cal_frm,text="Enter", background="#5cf2f2", command=self.ent_btn_click)
        self.cal_btn.pack()
        
        ''' 
            canvas widget
        '''
        self.cnv = tk.Canvas(self.m, width=500, height=500, bg='black', highlightbackground="white")
        self.cnv.grid(row=0, column=1, rowspan=3, padx=10, pady=10)
        self.cnv.bind('<1>', self.canvas_click)
        
        ''' 
            clear canvas button
        '''
        self.clr_btn = tk.Button(self.m, text="Clear Canvas", background="white", command=self.clr_btn_click)
        self.clr_btn.grid(row=3, column=1)
        
        '''
            Executing main loop
        '''
        self.m.mainloop()
        
        
    def sub_btn_click(self):
        self.cnv.delete('all')
        self.X = np.append(self.X, [self.x_pos, self.y_pos]).reshape(2, -1)
        self.Y = np.reshape(self.pos_class, (1, -1))
        self.x_pos = np.array([])
        self.y_pos = np.array([])
        self.pos_class = np.array([])
        self.m.destroy()
    
    def change_class(self):
        if(self.curr_cls =='A'):
            self.curr_cls = 'B'
            self.color = "#8a83ea"
        else:
            self.curr_cls = 'A'
            self.color = "#ef8686"
        
    def btn_click(self):
        self.change_class()
        self.lbl['text'] = "Current class: {}".format(self.curr_cls)
        self.btn['background'] = self.color
        self.enter_btn['backgroun'] = "white"
        
    def canvas_click(self, e):
        if(__name__ == "__main__"):   
            print(f"e.x: {e.x}, e.y: {500-e.y}")        
        if((e.x in self.x_pos) and (e.y in self.y_pos)): return
        self.x_pos = np.append(self.x_pos, e.x)
        self.y_pos = np.append(self.y_pos, 500 - e.y)
        if(self.curr_cls=='A'): clss = 0
        else: clss = 1
        self.pos_class = np.append(self.pos_class, clss)
        self.draw_circle(e.x, e.y, 2, c=self.color)
    
    def ent_btn_click(self):
        self.point_count = int(self.cal_entry.get())
        
    def clr_btn_click(self):
        self.x_pos = np.array([])
        self.y_pos = np.array([])
        self.pos_class = np.array([])
        self.cnv.delete('all')
    
    
    def draw_arc(self, x, y, r, s=0, e=120, c='white'):
        self.cnv.create_arc(x-r, y-r, x+r, y+r, start=s, extent=e-s, fill=c, smooth=True)
    
    def draw_circle(self, x, y, r, c='white'):
        self.cnv.create_oval(x-r, y-r, x+r, y+r, fill=c)
        
    def draw_line(self, row, x, y, fill='white', lw=1):
        self.line = self.cnv.create_line(row[0], row[1], x, y, fill=fill, smooth=True, dash=(4, 4), width=lw)


if(__name__ == "__main__"):       
    gui = GUI()
    print(gui.X, gui.Y)
    
    
def tk_plot():
    gui_call = GUI()
    return gui_call.X, gui_call.Y

