from tkinter import *
from PIL import ImageTk, Image
import glob
import os

images=glob.glob("*.jpg")+glob.glob("*.png")
print (images)
print(type(images))

clicks = 0

canv_num = 1
list_images_n = 0
len_images_n = len(images)

button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9, button_10, button_11, button_12, button_13, button_14, button_15, button_16, button_17, button_18, button_19, button_20, button_21, button_22, button_23, button_24, button_25, button_26, button_27, button_28, button_29, button_30, button_31, button_32, button_33, button_34, button_35, button_36, button_37, button_38, button_39, button_40, button_41, button_42, button_43, button_44, button_45, button_46, button_47, button_48, button_49, button_50, button_51, button_52, button_53, button_54, button_55, button_56, button_57, button_61 = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
 
def click_button():
    global clicks
    clicks += 1
    root.title("Clicks {}".format(clicks))
    
def click_button_1():
    global clicks, button_1
    clicks += 1
    if button_1 == 0:
       btn1.config(background="#777", foreground="#bbb")
       button_1 = 1
    else:
       btn1.config(background="#555", foreground="#ccc")
       button_1 = 0       
  
def click_button_2():
    global clicks, button_2
    clicks += 1
    if button_2 == 0:
       btn2.config(background="#777", foreground="#bbb")
       button_2 = 1       
    else:
       btn2.config(background="#555", foreground="#ccc") 
       button_2 = 0
        
def click_button_3():
    global clicks, button_3
    clicks += 1
    if button_3 == 0:
       btn3.config(background="#777", foreground="#bbb") 
       button_3 = 1 
    else:
       btn3.config(background="#555", foreground="#ccc")
       button_3 = 0        

def click_button_4():
    global clicks, button_4
    clicks += 1
    if button_4 == 0:
       btn4.config(background="#777", foreground="#bbb") 
       button_4 = 1 
    else:
       btn4.config(background="#555", foreground="#ccc")
       button_4 = 0       

def click_button_5():
    global clicks, button_5
    clicks += 1
    if button_5 == 0:
       btn5.config(background="#777", foreground="#bbb")
       button_5 = 1 
    else:
       btn5.config(background="#555", foreground="#ccc")
       button_5 = 0        

def click_button_6():
    global clicks, button_6
    clicks += 1
    if button_6 == 0:
       btn6.config(background="#777", foreground="#bbb") 
       button_6 = 1 
    else:
       btn6.config(background="#555", foreground="#ccc") 
       button_6 = 0 
  
def click_button_7():
    global clicks, button_7
    clicks += 1
    if button_7 == 0:
       btn7.config(background="#777", foreground="#bbb")
       button_7 = 1        
    else:
       btn7.config(background="#555", foreground="#ccc")
       button_7 = 0        

def click_button_8():
    global clicks, button_8
    clicks += 1
    if button_8 == 0:
       btn8.config(background="#777", foreground="#bbb") 
       button_8 = 1 
    else:
       btn8.config(background="#555", foreground="#ccc") 
       button_8 = 0 

def click_button_9():
    global clicks, button_9
    clicks += 1
    if button_9 == 0:
       btn9.config(background="#777", foreground="#bbb")
       button_9 = 1        
    else:
       btn9.config(background="#555", foreground="#ccc") 
       button_9 = 0 

def click_button_10():
    global clicks, button_10
    clicks += 1
    if button_10 == 0:
       btn10.config(background="#777", foreground="#bbb") 
       button_10 = 1 
    else:
       btn10.config(background="#555", foreground="#ccc") 
       button_10 = 0        

def click_button_11():
    global clicks, button_11
    clicks += 1
    if button_11 == 0:
       btn11.config(background="#777", foreground="#bbb")
       button_11 = 1        
    else:
       btn11.config(background="#555", foreground="#ccc")
       button_11 = 0        
  
def click_button_12():
    global clicks, button_12
    clicks += 1
    if button_12 == 0:
       btn12.config(background="#777", foreground="#bbb")
       button_12 = 1        
    else:
       btn12.config(background="#555", foreground="#ccc")
       button_12 = 0        

def click_button_13():
    global clicks, button_13
    clicks += 1
    if button_13 == 0:
       btn13.config(background="#777", foreground="#bbb")
       button_13 = 1        
    else:
       btn13.config(background="#555", foreground="#ccc")
       button_13 = 0        

def click_button_14():
    global clicks, button_14
    clicks += 1
    if button_14 == 0:
       btn14.config(background="#777", foreground="#bbb")
       button_14 = 1        
    else:
       btn14.config(background="#555", foreground="#ccc")
       button_14 = 0        

def click_button_15():
    global clicks, button_15
    clicks += 1
    if button_15 == 0:
       btn15.config(background="#777", foreground="#bbb")
       button_15 = 1        
    else:
       btn15.config(background="#555", foreground="#ccc")
       button_15 = 1        

def click_button_16():
    global clicks, button_16
    clicks += 1
    if button_16 == 0:
       btn16.config(background="#777", foreground="#bbb")
       button_16 = 1        
    else:
       btn16.config(background="#555", foreground="#ccc")
       button_16 = 0        
  
def click_button_17():
    global clicks, button_17
    clicks += 1
    if button_17 == 0:
       btn17.config(background="#777", foreground="#bbb")
       button_17 = 1        
    else:
       btn17.config(background="#555", foreground="#ccc")
       button_17 = 0        

def click_button_18():
    global clicks, button_18
    clicks += 1
    if button_18 == 0:
       btn18.config(background="#777", foreground="#bbb")
       button_18 = 1       
    else:
       btn18.config(background="#555", foreground="#ccc")
       button_18 = 0       

def click_button_19():
    global clicks, button_19
    clicks += 1
    if button_19 == 0:
       btn19.config(background="#777", foreground="#bbb")
       button_19 = 1       
    else:
       btn19.config(background="#555", foreground="#ccc")
       button_19 = 0       
       
def click_button_20():
    global clicks, button_20
    clicks += 1
    if button_20 == 0:
       btn20.config(background="#777", foreground="#bbb")
       button_20 = 1       
    else:
       btn20.config(background="#555", foreground="#ccc")
       button_20 = 0       

def click_button_21():
    global clicks, button_21
    clicks += 1
    if button_21 == 0:
       btn21.config(background="#777", foreground="#bbb")
       button_21 = 1       
    else:
       btn21.config(background="#555", foreground="#ccc")
       button_21 = 0       
  
def click_button_22():
    global clicks, button_22
    clicks += 1
    if button_22 == 0:
       btn22.config(background="#777", foreground="#bbb")
       button_22 = 1       
    else:
       btn22.config(background="#555", foreground="#ccc")
       button_22 = 0       

def click_button_23():
    global clicks, button_23
    clicks += 1
    if button_23 == 0:
       btn23.config(background="#777", foreground="#bbb")
       button_23 = 1       
    else:
       btn23.config(background="#555", foreground="#ccc")
       button_23 = 0       

def click_button_24():
    global clicks, button_24
    clicks += 1
    if button_24 == 0:
       btn24.config(background="#777", foreground="#bbb")
       button_24 = 1       
    else:
       btn24.config(background="#555", foreground="#ccc")
       button_24 = 0       

def click_button_25():
    global clicks, button_25
    clicks += 1
    if button_25 == 0:
       btn25.config(background="#777", foreground="#bbb")
       button_25 = 1       
    else:
       btn25.config(background="#555", foreground="#ccc")
       button_25 = 0       

def click_button_26():
    global clicks, button_26
    clicks += 1
    if button_26 == 0:
       btn26.config(background="#777", foreground="#bbb")
       button_26 = 1       
    else:
       btn26.config(background="#555", foreground="#ccc")
       button_26 = 0       
  
def click_button_27():
    global clicks, button_27
    clicks += 1
    if button_27 == 0:
       btn27.config(background="#777", foreground="#bbb")
       button_27 = 1       
    else:
       btn27.config(background="#555", foreground="#ccc")
       button_27 = 0       
       
def click_button_28():
    global clicks, button_28
    clicks += 1
    if button_28 == 0:
       btn28.config(background="#777", foreground="#bbb")
       button_28 = 1       
    else:
       btn28.config(background="#555", foreground="#ccc")
       button_28 = 0       

def click_button_29():
    global clicks, button_29
    clicks += 1
    if button_29 == 0:
       btn29.config(background="#777", foreground="#bbb")
       button_29 = 1       
    else:
       btn29.config(background="#555", foreground="#ccc")
       button_29 = 0       

def click_button_30():
    global clicks, button_30
    clicks += 1
    if button_30 == 0:
       btn30.config(background="#777", foreground="#bbb")
       button_30 = 1       
    else:
       btn30.config(background="#555", foreground="#ccc")
       button_30 = 0       

def click_button_31():
    global clicks, button_31
    clicks += 1
    if button_31 == 0:
       btn31.config(background="#777", foreground="#bbb")
       button_31 = 1       
    else:
       btn31.config(background="#555", foreground="#ccc")
       button_31 = 0       
  
def click_button_32():
    global clicks, button_32
    clicks += 1
    if button_32 == 0:
       btn32.config(background="#777", foreground="#bbb")
       button_32 = 1       
    else:
       btn32.config(background="#555", foreground="#ccc")
       button_32 = 0       

def click_button_33():
    global clicks, button_33
    clicks += 1
    if button_33 == 0:
       btn33.config(background="#777", foreground="#bbb")
       button_33 = 1       
    else:
       btn33.config(background="#555", foreground="#ccc")
       button_33 = 0       

def click_button_34():
    global clicks, button_34
    clicks += 1
    if button_34 == 0:
       btn34.config(background="#777", foreground="#bbb")
       button_34 = 1       
    else:
       btn34.config(background="#555", foreground="#ccc")
       button_34 = 0       

def click_button_35():
    global clicks, button_35
    clicks += 1
    if button_35 == 0:
       btn35.config(background="#777", foreground="#bbb")
       button_35 = 1       
    else:
       btn35.config(background="#555", foreground="#ccc")
       button_35 = 0       

def click_button_36():
    global clicks, button_36
    clicks += 1
    if button_36 == 0:
       btn36.config(background="#777", foreground="#bbb")
       button_36 = 1       
    else:
       btn36.config(background="#555", foreground="#ccc")
       button_36 = 0       
  
def click_button_37():
    global clicks, button_37
    clicks += 1
    if button_37 == 0:
       btn37.config(background="#777", foreground="#bbb")
       button_37 = 1       
    else:
       btn37.config(background="#555", foreground="#ccc")
       button_37 = 0       

def click_button_38():
    global clicks, button_38
    clicks += 1
    if button_38 == 0:
       btn38.config(background="#777", foreground="#bbb")
       button_38 = 1       
    else:
       btn38.config(background="#555", foreground="#ccc")
       button_38 = 0       

def click_button_39():
    global clicks, button_39
    clicks += 1
    if button_39 == 0:
       btn39.config(background="#777", foreground="#bbb")
       button_39 = 1       
    else:
       btn39.config(background="#555", foreground="#ccc")
       button_39 = 0       

def click_button_40():
    global clicks, button_40
    clicks += 1
    if button_40 == 0:
       btn40.config(background="#777", foreground="#bbb")
       button_40 = 1       
    else:
       btn40.config(background="#555", foreground="#ccc")
       button_40 = 0       

def click_button_41():
    global clicks, button_41
    clicks += 1
    if button_41 == 0:
       btn41.config(background="#777", foreground="#bbb")
       button_41 = 1       
    else:
       btn41.config(background="#555", foreground="#ccc")
       button_41 = 0       
  
def click_button_42():
    global clicks, button_42
    clicks += 1
    if button_42 == 0:
       btn42.config(background="#777", foreground="#bbb")
       button_42 = 1       
    else:
       btn42.config(background="#555", foreground="#ccc")
       button_42 = 0       

def click_button_43():
    global clicks, button_43
    clicks += 1
    if button_43 == 0:
       btn43.config(background="#777", foreground="#bbb")
       button_43 = 1       
    else:
       btn43.config(background="#555", foreground="#ccc")
       button_43 = 0       

def click_button_44():
    global clicks, button_44
    clicks += 1
    if button_44 == 0:
       btn44.config(background="#777", foreground="#bbb")
       button_44 = 1       
    else:
       btn44.config(background="#555", foreground="#ccc")
       button_44 = 0       

def click_button_45():
    global clicks, button_45
    clicks += 1
    if button_45 == 0:
       btn45.config(background="#777", foreground="#bbb")
       button_45 = 1       
    else:
       btn45.config(background="#555", foreground="#ccc")
       button_45 = 0       

def click_button_46():
    global clicks, button_46
    clicks += 1
    if button_46 == 0:
       btn46.config(background="#777", foreground="#bbb")
       button_46 = 1       
    else:
       btn46.config(background="#555", foreground="#ccc")
       button_46 = 0       
  
def click_button_47():
    global clicks, button_47
    clicks += 1
    if button_47 == 0:
       btn47.config(background="#777", foreground="#bbb")
       button_47 = 1       
    else:
       btn47.config(background="#555", foreground="#ccc")
       button_47 = 0       

def click_button_48():
    global clicks, button_48
    clicks += 1
    if button_48 == 0:
       btn48.config(background="#777", foreground="#bbb")
       button_48 = 1       
    else:
       btn48.config(background="#555", foreground="#ccc")
       button_48 = 0       

def click_button_49():
    global clicks, button_49
    clicks += 1
    if button_49 == 0:
       btn49.config(background="#777", foreground="#bbb")
       button_49 = 1       
    else:
       btn49.config(background="#555", foreground="#ccc")
       button_49 = 0       

def click_button_50():
    global clicks, button_50
    clicks += 1
    if button_50 == 0:
       btn50.config(background="#777", foreground="#bbb")
       button_50 = 1       
    else:
       btn50.config(background="#555", foreground="#ccc")
       button_50 = 0       
       
def click_button_51():
    global clicks, button_51
    clicks += 1
    if button_51 == 0:
       btn51.config(background="#777", foreground="#bbb")
       button_51 = 1       
    else:
       btn51.config(background="#555", foreground="#ccc")
       button_51 = 0       
 
def click_button_52():
    global clicks, button_52
    clicks += 1
    if button_52 == 0:
       btn52.config(background="#777", foreground="#bbb")
       button_52 = 1       
    else:
       btn52.config(background="#555", foreground="#ccc")
       button_52 = 0       

def click_button_53():
    global clicks, button_53
    clicks += 1
    if button_53 == 0:
       btn53.config(background="#777", foreground="#bbb")
       button_53 = 1       
    else:
       btn53.config(background="#555", foreground="#ccc")
       button_53 = 0       

def click_button_54():
    global clicks, button_54
    clicks += 1
    if button_54 == 0:
       btn54.config(background="#777", foreground="#bbb")
       button_54 = 1       
    else:
       btn54.config(background="#555", foreground="#ccc")
       button_54 = 0       

def click_button_55():
    global clicks, button_55
    clicks += 1
    if button_55 == 0:
       btn55.config(background="#777", foreground="#bbb")
       button_55 = 1       
    else:
       btn55.config(background="#555", foreground="#ccc")
       button_55 = 0       

def click_button_56():
    global clicks, button_56
    clicks += 1
    if button_56 == 0:
       btn56.config(background="#777", foreground="#bbb")
       button_56 = 1       
    else:
       btn56.config(background="#555", foreground="#ccc")
       button_56 = 0       
  
def click_button_57():
    global clicks, button_57
    clicks += 1
    if button_57 == 0:
       btn57.config(background="#777", foreground="#bbb") 
       button_57 = 1       
    else:
       btn57.config(background="#555", foreground="#ccc")
       button_57 = 0       

def click_button_61():
    global clicks, button_61
    clicks += 1
    if button_61 == 0:
       btn61.config(background="#777", foreground="#bbb")
       button_61 = 1
    else:
       btn61.config(background="#555", foreground="#ccc")
       button_61 = 0       

def click_button_58(): #Nav button
    global clicks, image1, list_images_n, images, button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9, button_10, button_11, button_12, button_13, button_14, button_15, button_16, button_17, button_18, button_19, button_20, button_21, button_22, button_23, button_24, button_25, button_26, button_27, button_28, button_29, button_30, button_31, button_32, button_33, button_34, button_35, button_36, button_37, button_38, button_39, button_40, button_41, button_42, button_43, button_44, button_45, button_46, button_47, button_48, button_49, button_50, button_51, button_52, button_53, button_54, button_55, button_56, button_57, button_61
    clicks += 1
    if list_images_n > 0:
       list_images_n = list_images_n - 1
    
    canvas = Canvas(root,width=700,height=700)
    canvas.place(x=750, y=0)
    im_name = images[list_images_n]
    pilImage1 = Image.open(im_name)
    image1 = ImageTk.PhotoImage(pilImage1)
    img = canvas.create_image(400,400,image=image1)
    button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9, button_10, button_11, button_12, button_13, button_14, button_15, button_16, button_17, button_18, button_19, button_20, button_21, button_22, button_23, button_24, button_25, button_26, button_27, button_28, button_29, button_30, button_31, button_32, button_33, button_34, button_35, button_36, button_37, button_38, button_39, button_40, button_41, button_42, button_43, button_44, button_45, button_46, button_47, button_48, button_49, button_50, button_51, button_52, button_53, button_54, button_55, button_56, button_57, button_61 = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    btn1.config(background="#555", foreground="#ccc")
    btn2.config(background="#555", foreground="#ccc")
    btn3.config(background="#555", foreground="#ccc")
    btn4.config(background="#555", foreground="#ccc")
    btn5.config(background="#555", foreground="#ccc")
    btn6.config(background="#555", foreground="#ccc")
    btn7.config(background="#555", foreground="#ccc")
    btn8.config(background="#555", foreground="#ccc")
    btn9.config(background="#555", foreground="#ccc")
    btn10.config(background="#555", foreground="#ccc")
    btn11.config(background="#555", foreground="#ccc")
    btn12.config(background="#555", foreground="#ccc")
    btn13.config(background="#555", foreground="#ccc")
    btn14.config(background="#555", foreground="#ccc")
    btn15.config(background="#555", foreground="#ccc")
    btn16.config(background="#555", foreground="#ccc")
    btn17.config(background="#555", foreground="#ccc")
    btn18.config(background="#555", foreground="#ccc")
    btn19.config(background="#555", foreground="#ccc")
    btn20.config(background="#555", foreground="#ccc")
    btn21.config(background="#555", foreground="#ccc")
    btn22.config(background="#555", foreground="#ccc")
    btn23.config(background="#555", foreground="#ccc")
    btn24.config(background="#555", foreground="#ccc")
    btn25.config(background="#555", foreground="#ccc")
    btn26.config(background="#555", foreground="#ccc")
    btn27.config(background="#555", foreground="#ccc")
    btn28.config(background="#555", foreground="#ccc")
    btn29.config(background="#555", foreground="#ccc")
    btn30.config(background="#555", foreground="#ccc")
    btn31.config(background="#555", foreground="#ccc")
    btn32.config(background="#555", foreground="#ccc")
    btn33.config(background="#555", foreground="#ccc")
    btn34.config(background="#555", foreground="#ccc")
    btn35.config(background="#555", foreground="#ccc")
    btn36.config(background="#555", foreground="#ccc")
    btn37.config(background="#555", foreground="#ccc")
    btn38.config(background="#555", foreground="#ccc")
    btn39.config(background="#555", foreground="#ccc")
    btn40.config(background="#555", foreground="#ccc")
    btn41.config(background="#555", foreground="#ccc")
    btn42.config(background="#555", foreground="#ccc")
    btn43.config(background="#555", foreground="#ccc")
    btn44.config(background="#555", foreground="#ccc")
    btn45.config(background="#555", foreground="#ccc")
    btn46.config(background="#555", foreground="#ccc")
    btn47.config(background="#555", foreground="#ccc")
    btn48.config(background="#555", foreground="#ccc")
    btn49.config(background="#555", foreground="#ccc")
    btn50.config(background="#555", foreground="#ccc")
    btn51.config(background="#555", foreground="#ccc")
    btn52.config(background="#555", foreground="#ccc")
    btn53.config(background="#555", foreground="#ccc")
    btn54.config(background="#555", foreground="#ccc")
    btn55.config(background="#555", foreground="#ccc")
    btn56.config(background="#555", foreground="#ccc")
    btn57.config(background="#555", foreground="#ccc")
    btn61.config(background="#555", foreground="#ccc")
	

def click_button_59():
    global clicks, images, list_images_n, button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9, button_10, button_11, button_12, button_13, button_14, button_15, button_16, button_17, button_18, button_19, button_20, button_21, button_22, button_23, button_24, button_25, button_26, button_27, button_28, button_29, button_30, button_31, button_32, button_33, button_34, button_35, button_36, button_37, button_38, button_39, button_40, button_41, button_42, button_43, button_44, button_45, button_46, button_47, button_48, button_49, button_50, button_51, button_52, button_53, button_54, button_55, button_56, button_57
    filename = images[list_images_n]
    string = filename[0:-4] + "; "
    if button_1 == 1:
       string = string + "Арт-светильники | "
    if button_2 == 1:
       string = string + "Детские светильники | "
    if button_3 == 1:
       string = string + "Влагозащитные светильники | "
    if button_4 == 1:
       string = string + "Люстры в восточном стиле | "
    if button_5 == 1:
       string = string + "Светильники для квартиры | "
    if button_6 == 1:
       string = string + "Люстры для залов | "
    if button_7 == 1:
       string = string + "Канделябры | "
    if button_8 == 1:
       string = string + "Классические люстры | "
    if button_9 == 1:
       string = string + "Кованые люстры | "
    if button_10 == 1:
       string = string + "Люстры с абажуром | "
    if button_11 == 1:
       string = string + "Люстры с цветами | "
    if button_12 == 1:
       string = string + "Светодиодные люстры LED | "
    if button_13 == 1:
       string = string + "Люстры Hi-tech (Хай тек) | "
    if button_14 == 1:
       string = string + "Эко светильники | "
    if button_15 == 1:
       string = string + "Хрустальные люстры | "
    if button_16 == 1:
       string = string + "Каскадные люстры | "
    if button_17 == 1:
       string = string + "Люстры с пультом | "
    if button_18 == 1:
       string = string + "HoReCa | "
    if button_19 == 1:
       string = string + "Светильники Regenbogen | "
    if button_20 == 1:
       string = string + "Премиальные люстры | "
    if button_21 == 1:
       string = string + "Лимитированные коллекции | "
    if button_22 == 1:
       string = string + "Белые светильники | "
    if button_23 == 1:
       string = string + "Красные люстры | "
    if button_24 == 1:
       string = string + "Черные люстры | "
    if button_25 == 1:
       string = string + "Хромированные люстры | "
    if button_26 == 1:
       string = string + "Дизайнерские люстры | "
    if button_27 == 1:
       string = string + "Недорогие светильники | "
    if button_28 == 1:
       string = string + "Эксклюзивные люстры | "
    if button_29 == 1:
       string = string + "Деревянные люстры | "
    if button_30 == 1:
       string = string + "Люстры прованс | "
    if button_31 == 1:
       string = string + "Люстры свечи | "
    if button_32 == 1:
       string = string + "Люстры с рожками | "
    if button_33 == 1:
       string = string + "Квадратные люстры | "
    if button_34 == 1:
       string = string + "Люстры флористика | "
    if button_35 == 1:
       string = string + "Люстры под старину | "
    if button_36 == 1:
       string = string + "Бронзовые люстры | "
    if button_37 == 1:
       string = string + "Яркие люстры | "
    if button_38 == 1:
       string = string + "Люстры в стиле лофт | "
    if button_39 == 1:
       string = string + "Люстры простые | "
    if button_40 == 1:
       string = string + "Люстры Luxury | "
    if button_41 == 1:
       string = string + "Люстры на штанге | "
    if button_42 == 1:
       string = string + "Плоские люстры | "
    if button_43 == 1:
       string = string + "Белые люстры | "
    if button_44 == 1:
       string = string + "Необычные светильники | "
    if button_45 == 1:
       string = string + "Светодиодные светильники | "
    if button_46 == 1:
       string = string + "Антуражные люстры | "
    if button_47 == 1:
       string = string + "Подвесные люстры | "
    if button_48 == 1:
       string = string + "Потолочные люстры | "
    if button_49 == 1:
       string = string + "Новые коллекции 2018 | "
    if button_50 == 1:
       string = string + "Трек-системы | "
    if button_51 == 1:
       string = string + "Люстры-пауки | "
    if button_52 == 1:
       string = string + "Ротанг | "
    if button_53 == 1:
       string = string + "Светильники хайтек | "
    if button_54 == 1:
       string = string + "Для кафе и ресторанов | "
    if button_55 == 1:
       string = string + "Для отелей и гостиниц | "
    if button_56 == 1:
       string = string + "Для баров и клубов | "
    if button_57 == 1:
       string = string + "Дочки-сыночки | "
    if button_61 == 1:
       string = string + "Античные люстры | "
	   
    string = string + "\n"
    file = open("output.csv", "a")
    file.write(string);
    file.close()
      
def click_button_60():
    global clicks, canv_num, image1, list_images_n, len_images_n, images, button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9, button_10, button_11, button_12, button_13, button_14, button_15, button_16, button_17, button_18, button_19, button_20, button_21, button_22, button_23, button_24, button_25, button_26, button_27, button_28, button_29, button_30, button_31, button_32, button_33, button_34, button_35, button_36, button_37, button_38, button_39, button_40, button_41, button_42, button_43, button_44, button_45, button_46, button_47, button_48, button_49, button_50, button_51, button_52, button_53, button_54, button_55, button_56, button_57, button_61
    clicks += 1
    if list_images_n < (len_images_n - 1):
       list_images_n = list_images_n + 1
      
    canvas = Canvas(root,width=700,height=700)
    canvas.place(x=750, y=0)
    im_name = images[list_images_n]
    pilImage1 = Image.open(im_name)
    image1 = ImageTk.PhotoImage(pilImage1)
    img = canvas.create_image(400,400,image=image1)
    button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9, button_10, button_11, button_12, button_13, button_14, button_15, button_16, button_17, button_18, button_19, button_20, button_21, button_22, button_23, button_24, button_25, button_26, button_27, button_28, button_29, button_30, button_31, button_32, button_33, button_34, button_35, button_36, button_37, button_38, button_39, button_40, button_41, button_42, button_43, button_44, button_45, button_46, button_47, button_48, button_49, button_50, button_51, button_52, button_53, button_54, button_55, button_56, button_57, button_61 = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
    btn1.config(background="#555", foreground="#ccc")
    btn2.config(background="#555", foreground="#ccc")
    btn3.config(background="#555", foreground="#ccc")
    btn4.config(background="#555", foreground="#ccc")
    btn5.config(background="#555", foreground="#ccc")
    btn6.config(background="#555", foreground="#ccc")
    btn7.config(background="#555", foreground="#ccc")
    btn8.config(background="#555", foreground="#ccc")
    btn9.config(background="#555", foreground="#ccc")
    btn10.config(background="#555", foreground="#ccc")
    btn11.config(background="#555", foreground="#ccc")
    btn12.config(background="#555", foreground="#ccc")
    btn13.config(background="#555", foreground="#ccc")
    btn14.config(background="#555", foreground="#ccc")
    btn15.config(background="#555", foreground="#ccc")
    btn16.config(background="#555", foreground="#ccc")
    btn17.config(background="#555", foreground="#ccc")
    btn18.config(background="#555", foreground="#ccc")
    btn19.config(background="#555", foreground="#ccc")
    btn20.config(background="#555", foreground="#ccc")
    btn21.config(background="#555", foreground="#ccc")
    btn22.config(background="#555", foreground="#ccc")
    btn23.config(background="#555", foreground="#ccc")
    btn24.config(background="#555", foreground="#ccc")
    btn25.config(background="#555", foreground="#ccc")
    btn26.config(background="#555", foreground="#ccc")
    btn27.config(background="#555", foreground="#ccc")
    btn28.config(background="#555", foreground="#ccc")
    btn29.config(background="#555", foreground="#ccc")
    btn30.config(background="#555", foreground="#ccc")
    btn31.config(background="#555", foreground="#ccc")
    btn32.config(background="#555", foreground="#ccc")
    btn33.config(background="#555", foreground="#ccc")
    btn34.config(background="#555", foreground="#ccc")
    btn35.config(background="#555", foreground="#ccc")
    btn36.config(background="#555", foreground="#ccc")
    btn37.config(background="#555", foreground="#ccc")
    btn38.config(background="#555", foreground="#ccc")
    btn39.config(background="#555", foreground="#ccc")
    btn40.config(background="#555", foreground="#ccc")
    btn41.config(background="#555", foreground="#ccc")
    btn42.config(background="#555", foreground="#ccc")
    btn43.config(background="#555", foreground="#ccc")
    btn44.config(background="#555", foreground="#ccc")
    btn45.config(background="#555", foreground="#ccc")
    btn46.config(background="#555", foreground="#ccc")
    btn47.config(background="#555", foreground="#ccc")
    btn48.config(background="#555", foreground="#ccc")
    btn49.config(background="#555", foreground="#ccc")
    btn50.config(background="#555", foreground="#ccc")
    btn51.config(background="#555", foreground="#ccc")
    btn52.config(background="#555", foreground="#ccc")
    btn53.config(background="#555", foreground="#ccc")
    btn54.config(background="#555", foreground="#ccc")
    btn55.config(background="#555", foreground="#ccc")
    btn56.config(background="#555", foreground="#ccc")
    btn57.config(background="#555", foreground="#ccc")
    btn61.config(background="#555", foreground="#ccc")

root = Tk()
root.title("Волкалюстроразмечалка")
root.geometry("1450x735")
 
btn1 = Button(text="Арт-светильники", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_1)
btn2 = Button(text="Детские светильники", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_2)
btn3 = Button(text="Влагозащитные светильники", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_3)
btn4 = Button(text="Люстры в восточном стиле", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_4)
btn5 = Button(text="Светильники для квартиры", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_5)
btn6 = Button(text="Люстры для залов", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_6)
btn7 = Button(text="Канделябры", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_7)
btn8 = Button(text="Классические люстры", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_8)
btn9 = Button(text="Кованые люстры", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_9)
btn10 = Button(text="Люстры с абажуром", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_10)
btn11 = Button(text="Люстры с цветами", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_11)
btn12 = Button(text="Светодиодные люстры LED", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_12)
btn13 = Button(text="Люстры Hi-tech (Хай тек)", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_13)
btn14 = Button(text="Эко светильники", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_14)
btn15 = Button(text="Хрустальные люстры", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_15)
btn16 = Button(text="Каскадные люстры", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_16)
btn17 = Button(text="Люстры с пультом", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_17)
btn18 = Button(text="HoReCa", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_18)
btn19 = Button(text="Светильники Regenbogen", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_19)
btn20 = Button(text="Премиальные люстры", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_20)
btn21 = Button(text="Лимитированные коллекции", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_21)
btn22 = Button(text="Белые светильники", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_22)
btn23 = Button(text="Красные люстры", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_23)
btn24 = Button(text="Черные люстры", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_24)
btn25 = Button(text="Хромированные люстры", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_25)
btn26 = Button(text="Дизайнерские люстры", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_26)
btn27 = Button(text="Недорогие светильники", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_27)
btn28 = Button(text="Эксклюзивные люстры", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_28)
btn29 = Button(text="Деревянные люстры", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_29)
btn30 = Button(text="Люстры прованс", background="#555", foreground="#ccc",  padx="25", pady="6", font="16", command=click_button_30)
btn31 = Button(text="Люстры свечи", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_31)
btn32 = Button(text="Люстры с рожками", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_32)
btn33 = Button(text="Квадратные люстры", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_33)
btn34 = Button(text="Люстры флористика", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_34)
btn35 = Button(text="Люстры под старину", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_35)
btn36 = Button(text="Бронзовые люстры", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_36)
btn37 = Button(text="Яркие люстры", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_37)
btn38 = Button(text="Люстры в стиле лофт", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_38)
btn39 = Button(text="Люстры простые", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_39)
btn40 = Button(text="Люстры Luxury", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_40)
btn41 = Button(text="Люстры на штанге", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_41)
btn42 = Button(text="Плоские люстры", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_42)
btn43 = Button(text="Белые люстры", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_43)
btn44 = Button(text="Необычные светильники", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_44)
btn45 = Button(text="Светодиодные светильники", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_45)
btn46 = Button(text="Антуражные люстры", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_46)
btn47 = Button(text="Подвесные люстры", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_47)
btn48 = Button(text="Потолочные люстры", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_48)
btn49 = Button(text="Новые коллекции 2018", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_49)
btn50 = Button(text="Трек-системы", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_50)
btn51 = Button(text="Люстры-пауки", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_51)
btn52 = Button(text="Ротанг", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_52)
btn53 = Button(text="Светильники хайтек", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_53)
btn54 = Button(text="Для кафе и ресторанов", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_54)
btn55 = Button(text="Для отелей и гостиниц", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_55)
btn56 = Button(text="Для баров и клубов", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_56)
btn57 = Button(text="Дочки-сыночки", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_57)
btn61 = Button(text="Античные люстры", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_61)

btn58 = Button(text="Назад", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_58)
btn59 = Button(text="Записать", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_59)
btn60 = Button(text="Вперед", background="#555", foreground="#ccc", padx="25", pady="6", font="16", command=click_button_60)

btn1.place(x=0, y=0, height=35, width=250)
btn2.place(x=0, y=35, height=35, width=250)
btn3.place(x=0, y=70, height=35, width=250)
btn4.place(x=0, y=105, height=35, width=250)
btn5.place(x=0, y=140, height=35, width=250)
btn6.place(x=0, y=175, height=35, width=250)
btn7.place(x=0, y=210, height=35, width=250)
btn8.place(x=0, y=245, height=35, width=250)
btn9.place(x=0, y=280, height=35, width=250)
btn10.place(x=0, y=315, height=35, width=250)
btn11.place(x=0, y=350, height=35, width=250)
btn12.place(x=0, y=385, height=35, width=250)
btn13.place(x=0, y=420, height=35, width=250)
btn14.place(x=0, y=455, height=35, width=250)
btn15.place(x=0, y=490, height=35, width=250)
btn16.place(x=0, y=525, height=35, width=250)
btn17.place(x=0, y=560, height=35, width=250)
btn18.place(x=0, y=595, height=35, width=250)
btn19.place(x=0, y=630, height=35, width=250)
btn20.place(x=0, y=665, height=35, width=250)
btn21.place(x=0, y=700, height=35, width=250)

btn22.place(x=250, y=0, height=35, width=250)
btn23.place(x=250, y=35, height=35, width=250)
btn24.place(x=250, y=70, height=35, width=250)
btn25.place(x=250, y=105, height=35, width=250)
btn26.place(x=250, y=140, height=35, width=250)
btn27.place(x=250, y=175, height=35, width=250)
btn28.place(x=250, y=210, height=35, width=250)
btn29.place(x=250, y=245, height=35, width=250)
btn30.place(x=250, y=280, height=35, width=250)
btn31.place(x=250, y=315, height=35, width=250)
btn32.place(x=250, y=350, height=35, width=250)
btn33.place(x=250, y=385, height=35, width=250)
btn34.place(x=250, y=420, height=35, width=250)
btn35.place(x=250, y=455, height=35, width=250)
btn36.place(x=250, y=490, height=35, width=250)
btn37.place(x=250, y=525, height=35, width=250)
btn38.place(x=250, y=560, height=35, width=250)
btn39.place(x=250, y=595, height=35, width=250)
btn40.place(x=250, y=630, height=35, width=250)
btn41.place(x=250, y=665, height=35, width=250)
btn42.place(x=250, y=700, height=35, width=250)

btn43.place(x=500, y=0, height=35, width=250)
btn44.place(x=500, y=35, height=35, width=250)
btn45.place(x=500, y=70, height=35, width=250)
btn46.place(x=500, y=105, height=35, width=250)
btn47.place(x=500, y=140, height=35, width=250)
btn48.place(x=500, y=175, height=35, width=250)
btn49.place(x=500, y=210, height=35, width=250)
btn50.place(x=500, y=245, height=35, width=250)
btn51.place(x=500, y=280, height=35, width=250)
btn52.place(x=500, y=315, height=35, width=250)
btn53.place(x=500, y=350, height=35, width=250)
btn54.place(x=500, y=385, height=35, width=250)
btn55.place(x=500, y=420, height=35, width=250)
btn56.place(x=500, y=455, height=35, width=250)
btn57.place(x=500, y=490, height=35, width=250)
btn61.place(x=500, y=525, height=35, width=250)

btn58.place(x=750, y=700, height=35, width=233)
btn59.place(x=983, y=700, height=35, width=233)
btn60.place(x=1216, y=700, height=35, width=233)

canvas = Canvas(root,width=700,height=700)
canvas.place(x=750, y=0)
im_name = images[list_images_n]
pilImage1 = Image.open(im_name)
image1 = ImageTk.PhotoImage(pilImage1)
img = canvas.create_image(400,400,image=image1)
 
root.mainloop()