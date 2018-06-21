from tkinter import *
from PIL import ImageTk,Image

####################### ROOT AND SIZE OF WINDOW ###############################
                 #### DECLARATION OF ROOT TKINTER ####
root = Tk()
screen_width,screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (screen_width, screen_height))
root.title("LET'S LEARN")

######################## STACK FUNCTION#######################################
def ex_stack():
	def push_pop():
		if(int(var.get()=='')):
			print("THIS IS HERE")
			return(None)
		abcd=int(str(var.get()))
		Label(stack,text=abcd).grid()
		Label(stack,text=abcd).grid()
		if((abcd)==1):
			Label(stack,text="HURRAY").grid()
		if(abcd==(1)):
			if(len(stack_list)==7):
				Message(stack,text="The Stack is FULL. POP an element first.",font=("arial",14)).grid()
			else:
				def push_the_number():
					stack_list.append(integer_num1.get())
					Message(stack,text="STACK CONTAINS:-",font=("arial",14)).grid()
					for tc in range(len(stack_list)):
						Message(stack,text=stack_list[tc],font=("arial",14)).grid(column=tc+1)

				integer_num1=IntVar()
				Label(stack,text="Enter an element.",font=("arial",14)).grid()
				Entry(stack,text=integer_num1,cursor="xterm",font=("arial",14)).grid(sticky=W)
				Button(stack,text="ENTER",cursor="hand2",command=lambda:push_the_number(),font=("arial",14)).grid()
	stack=Tk()
	stack.geometry("%dx%d+0+0"%(screen_width, screen_height))
	stack.title("STACK IMPLEMENTATION")
	stack_list=[]
	Label(stack,text="STACK IMPLEMENTATION",font=("times new roman",28,"bold","underline")).grid(sticky=W)
	Message(stack,width=screen_width,text="Here you can understand the concept of Stacks with continuous practice.",font=("arial",20)).grid(pady=10)
	Message(stack,text="Press 1 to PUSH an Element into a STACK.",font=("arial",14),width=screen_width,anchor=W).grid(sticky=W)
	Message(stack,width=screen_width,text="Press 2 to POP an Element out of the STACK.",font=("arial",14),anchor=W).grid(sticky=W)
	Message(stack,width=screen_width,text="Press 3 To DISPLAY the STACK.",font=("monotype corosiva",14),anchor=W).grid(sticky=W)
	var=StringVar()
	Entry(stack,textvariable=var).grid()
	Button(stack,text="Enter",command=lambda:push_pop()).grid()
	stack.update_idletasks()

####################### FRAME CHANGING FUNCTION ###############################
def raise_frame(frame):
    frame.tkraise()

####################### CHILD DELETING FUNCTION ##############################
def frame_del(a):
	for child in a.winfo_children():
		child.destroy()


############################# DS--FUNCTIONS ###############################

#function for "INTRODUCTION TO DS"#
def intro_to_ds_func(a):
	
	Label(a,text="INTRODUCTION TO DATA STRUCTURES",padx=10,pady=20,font=("times new roman",40,"bold","underline")).grid()
	intro_to_ds_func_file=open("intro_to_ds1.txt")
	Message(a,text=intro_to_ds_func_file.read(),padx=20,fg="red",font=("arial",20),width=screen_width-40).grid()
	intro_to_ds_func_file.close()
	Button(intro_to_ds_frame1,text="NEXT",cursor="hand2",command=lambda:[raise_frame(intro_to_ds_frame4)],font=(14),height=3,width=10).grid(row=21,sticky=E,padx=10,pady=2)
	Button(intro_to_ds_frame1,text="BACK",cursor="hand2",command=lambda:[raise_frame(index_DS),frame_del(intro_to_ds_frame1)],font=(14),height=3,width=10).grid(row=21,sticky=W,padx=10,pady=2)
	

	Label(intro_to_ds_frame2,text="TYPES OF DATA STRUCTURES",padx=4,pady=10,font=("times new roman",35,"bold","underline"),fg="blue").grid()
	Label(intro_to_ds_frame2,text="* Arrays",font=("arial",32,"underline"),fg="green").grid(sticky=W,padx=6)
	statement='''An array is a collection of similar data elements. The elements of the array are stored in consecutive memory locations. They always have fixed size.\nExample- int marks[10];\nThe above statement declares an array marks that contains 10 elements( having index 0 to 9).'''
	Message(intro_to_ds_frame2,text=statement,width=screen_width-40,font=("arial",16),fg="red").grid(sticky=W,padx=8)
	Label(intro_to_ds_frame2,text="* LINKED LISTS",font=("arial",32,"underline"),fg="green").grid(sticky=W,padx=6)
	statement='''Linked list is a very flexible, dynamic data styrcture in which the elements can be added to or deleted from anywhere at will. In contrast to using static arrays, aprogrammer need not worry about how many elements will be stored in the linked list. This feature enables the programmers to write robust programs which require less maintenance.\nIn a linked list each element (is called a node) is allocated space as it is added to the list. Every node in the list points to the next node in the list.  '''
	Message(intro_to_ds_frame2,text=statement,width=screen_width-40,font=("arial",16),fg="red").grid(sticky=W,padx=8)
	Label(intro_to_ds_frame2,text="* STACKS",font=("arial",32,"underline"),fg="green").grid(sticky=W,padx=6)
	statement='''In the computer's memory, stacks can be represented as a linear array. Every stack has a variable TOP associated with it. Top is used to store the address of the topmost element of the stack. It is this position from where the element will be added or deleted. There is another variable MAX, which will be used to store the maximum number of elements that this stack can store.\nIf TOP = NULL, then it indicates that the stack is empty and if TOP = MAX, then the stack is FULL.'''
	Message(intro_to_ds_frame2,text=statement,width=screen_width-40,font=("arial",16),fg="red").grid(sticky=W,padx=8)
	Button(intro_to_ds_frame2,text="NEXT",cursor="hand2",command=lambda:[raise_frame(intro_to_ds_frame3)],font=(14),height=3,width=10).grid(row=21,sticky=E,padx=10,pady=2)
	Button(intro_to_ds_frame2,text="BACK",cursor="hand2",command=lambda:[raise_frame(intro_to_ds_frame4)],font=(14),height=3,width=10).grid(row=21,sticky=W,padx=10,pady=2)

	
	Label(intro_to_ds_frame3,text="* Queues",font=("arial",35,"underline"),fg="green").grid(sticky=W,padx=6)
	statement='''A queue is a FIFO ( First-In First-Out) data structure in which the element that was inserted first is the first one to be taken out. The elements in a queue are added at one end called the rear end and removed from the other end called the front end.\n Before inserting an element in the queue, we must check for overflow conditions. An overflow occurs when we try to insert an element into a queue, that is already full that is when Rear = MAX -1.\n Similary, Before deleting an element from the queue, we must check for underflow conditions. An underflow condition occurs when we try to delete an element from a queue that is already empty that is when Front = -1 and Rear = -1.'''
	Message(intro_to_ds_frame3,text=statement,width=screen_width-40,font=("arial",16),fg="red").grid(sticky=W,padx=8)
	Label(intro_to_ds_frame3,text="* TREES",font=("arial",35,"underline"),fg="green").grid(sticky=W,padx=6)
	statement='''A binary tree is a data structure which is defined as a collection of elements called the nodes. Every node contains a left pointer, a right pointer, and a data element. Every binary tree has a root element pointed by a 'root' pointer. The root element is the topmost node in the tree. If root is NULL, then the tree is empty.\nIf the root node R is not NULL, then the two trees T1 and T2 are called the left and right subtrees of R. If T1 is non-empty, then T1 is said to be the left successor of R. Likewise, if T2 is non-empty, then it is called the right successor of R.'''
	Message(intro_to_ds_frame3,text=statement,width=screen_width-40,font=("arial",16),fg="red").grid(sticky=W,padx=8)
	Label(intro_to_ds_frame3,text="* GRAPHS",font=("arial",35,"underline"),fg="green").grid(sticky=W,padx=6)
	statement='''A graph is an abstract data structure that is used to implement that graph concept from mathematics. It is basically a collection of vertices (also called nodes) and edged that connect these vertices. A graph is often viewed as generalization of the tree structure,where instead os having a purely parent-to-child relationship between tree nodes, any kind of complex relationships between the nodes can be represented.\nIn a tree structure, the nodes can have many children but only one parent, a graph on the other hand relaxes all such kinds of restrictions.'''
	Message(intro_to_ds_frame3,text=statement,width=screen_width-40,font=("arial",16),fg="red").grid(sticky=W,padx=8)
	Button(intro_to_ds_frame3,text="BACK",cursor="hand2",command=lambda:[raise_frame(intro_to_ds_frame2)],font=(14),height=3,width=10).grid(row=21,sticky=W,padx=10,pady=2)

	intro_to_ds_background_image=ImageTk.PhotoImage(Image.open("intro_to_ds1.jpg"))
	intro_to_ds_background_image1= Label(intro_to_ds_frame4,image=intro_to_ds_background_image)
	intro_to_ds_background_image1.image=intro_to_ds_background_image
	intro_to_ds_background_image1.place(height=screen_height-50,width=screen_width-50)
	Button(intro_to_ds_frame4,text="BACK",cursor="hand2",command=lambda:[raise_frame(intro_to_ds_frame1)],font=(14),height=2,width=8).grid(row=0,sticky=E,padx=10,pady=2)
	Button(intro_to_ds_frame4,text="NEXT",cursor="hand2",command=lambda:[raise_frame(intro_to_ds_frame2)],font=("arial",14),height=1,width=8,anchor=E).grid(padx=1000,row=0,column=50,sticky=W)




#function for "STACKS"#
def stack_func(a):
	Label(stack_frame,text="STACK",font=("times new roman",40,"bold","underline")).grid(padx=500,pady=10)
	statement='''A stack is a linear data structure which can be implemented by either using an array or a linked list. The elements in a stack are added and removed only from one end, which is called the TOP. Hence, a stack is called a LIFO(Last-In-First-Out) data structure, as the element that was inserted last is the first one to be taken out.\n\nA stack has three basic operations: puch, pop and peep. The push operation adds an element to the top of the stack and the pop operation removes the element from the top of the stack. The peep operation returns the value of the topmost element of the stack.'''
	Message(stack_frame,text=statement,font=("arial",24),width=screen_width-50).grid()
	stack_image=ImageTk.PhotoImage(Image.open("stack.jpg"))
	stack_image1=Label(stack_frame,image=stack_image)
	stack_image1.image=stack_image
	stack_image1.grid(row=17)
	Button(a,text="NEXT",cursor="X_cursor",state=DISABLED,font=("arial",12),height=2,width=8).grid(row=20,sticky=E)
	Button(a,text="Interactive Example",cursor="X_cursor",height=2,width=15,command=lambda:ex_stack()).grid(row=20)
	Button(a,text="BACK",cursor="hand2",height=2,width=8,command=lambda:[raise_frame(index_DS),frame_del(a)]).grid(sticky=W,row=20)

#function for "QUEUES"#
def queue_func(a):
	Label(a,text="QUEUES",fg="blue" ,font=("times new roman",40,"bold","underline")).grid(padx=500,pady=10)
	statement='''A Queue is a linear list of elements in which deletions can take place only at one end, called the front, and insertions can take place only at the other end called the rear. The terms "front" and "rear" are used in describing a linear list only when it is implemented as a queue.\nQueues are also called first-out(FIFO) lists,since the first element in a queue will be the first element out of the queue. In other words, the order in which element enter a queue is the order in which they leave. This contrasts with stacks, which are last-in first-out.\nQueues abound in everyday life. The automobiles waiting to pass through an intersection form a queue, in which the first car in line is the first car through; the people waiting in line at a bank form a queue, where the first person in line is the first person to be waited on; and so on.'''
	Message(a,text=statement,font=("arial",24),width=screen_width-50).grid()
	queue_image=ImageTk.PhotoImage(Image.open("queue.png"))
	queue_image1=Label(a,image=queue_image)
	queue_image1.image=queue_image
	queue_image1.grid(row=17)
	Button(a,text="NEXT",cursor="X_cursor",state=DISABLED,font=("arial",12),height=2,width=8).grid(row=20,sticky=E)
	Button(a,text="Interactive Example",cursor="X_cursor",state=DISABLED,height=2,width=15).grid(row=20)
	Button(a,text="BACK",cursor="hand2",height=2,width=8,command=lambda:[raise_frame(index_DS),frame_del(a)]).grid(sticky=W,row=20)


############################ DLD--FUNCTIONS ###############################
def boolean_algebra_func(a):
	Label(a,text="DEFINITION OF BOOLEAN ALGEBRA",fg="blue" ,font=("times new roman",40,"bold","underline")).grid(padx=150,pady=10)
	statement='''Boolean algebra is an algebraic structure defined by a set of elements, B, together with two binary operators, (+) and (.) , provided that the following postulates are satisfied:-\n\n   1.(a) The structure is closed with respect to the operator +.\n      (b) The structure is closed with respect to the operator (.).\n\n   2.(a) The element 0 is an identity element with respect to + ; that is, x + 0= 0 + x= x.\n      (b)The element 1 is an identity element with respect to . , that is , x.y= y.x ;\n\n   3.(a)The structure is commutative with respect to + ; that is, x+y = y+ x;\n      (b) The structure is commutative with respect to . , x.y= y.x.\n   4. For every element x belonging to B, there exists an element x' belonging such that x + x' = 1 and x.x'=0.\n   5. There exist at least two elements x,y belonging to B such that x !=y. '''
	Message(a,text=statement,font=("arial",24),width=screen_width-50).grid(sticky=W)
	Button(a,text="NEXT",cursor="X_cursor",state=DISABLED,font=("arial",12),height=2,width=8).grid(row=20,sticky=E)
	Button(a,text="Interactive Example",cursor="X_cursor",state=DISABLED,height=2,width=15).grid(row=20)
	Button(a,text="BACK",cursor="hand2",height=2,width=8,command=lambda:[raise_frame(index_DLD),frame_del(a)]).grid(sticky=W,row=20)	




############################ DSTL--FUNCTIONS ###############################
def set_theory_func(a):
	Label(a,text="SET THEORY",fg="blue" ,font=("times new roman",40,"bold","underline")).grid(padx=150,pady=10)
	statement='''A set is any well-defined collection of objects, called the elements or members of the set. These elements may be anything: numbers, point in geometry, letters of alphabets, etc.Example- A battalion of soldiers; The rivers in India; The vowelsof alphabets.\n\n      FINITE AND INFINITE SET\n   A set with finite number of elements in it, is called a finite set. An infinite set is a set which contains infinite number of elements.\n\n      NULL SET\n   A set which contains no elements at all is called the Null set(also know as empty set or void set). \n\n      SINGLETON SET\n   A set which has only one element is called a Singleton set.'''
	Message(a,text=statement,font=("arial",24),width=screen_width-50).grid(sticky=W)
	Button(a,text="NEXT",cursor="X_cursor",state=DISABLED,font=("arial",12),height=2,width=8).grid(row=20,sticky=E)
	Button(a,text="Interactive Example",cursor="X_cursor",state=DISABLED,height=2,width=15).grid(row=20)
	Button(a,text="BACK",cursor="hand2",height=2,width=8,command=lambda:[raise_frame(index_DSTL),frame_del(a)]).grid(sticky=W,row=20)	




#######################declaration of all the frames#######################

subject_frame=Frame(root,height=screen_height,width=screen_width)
about_frame=Frame(root,height=screen_height,width=screen_width)

########################FRAMES OF DATA STRUCTURES##########################
index_DS = Frame(root,height=screen_height,width=screen_width)
intro_to_ds_frame1 = Frame(root,height=screen_height,width=screen_width)
stack_frame = Frame(root,height=screen_height,width=screen_width)
queue_frame = Frame(root,height=screen_height,width=screen_width)
intro_to_ds_frame2=Frame(root,height=screen_height,width=screen_width)
intro_to_ds_frame3=Frame(root,height=screen_height,width=screen_width)
intro_to_ds_frame4=Frame(root,height=screen_height,width=screen_width)
#############################FRAMES OF DLD##################################
index_DLD = Frame(root,height=screen_height,width=screen_width)
boolean_algebra = Frame(root,height=screen_height,width=screen_width)

#################################FRAMES OF DSTL#############################

index_DSTL = Frame(root,height=screen_height,width=screen_width)
set_theory= Frame(root,height=screen_height,width=screen_width)

###########################################################################
###########################################################################
for frame in (subject_frame,index_DS, intro_to_ds_frame1,  stack_frame,queue_frame,index_DLD,boolean_algebra,about_frame):
   frame.grid(row=0, column=0, sticky='news')

for frame in (intro_to_ds_frame2,intro_to_ds_frame3,intro_to_ds_frame4,index_DSTL,set_theory):
   frame.grid(row=0, column=0, sticky='news')
###########################################################################
##########################################################################


################# SUBJECT PAGE ##############################
subject_page_background_image=ImageTk.PhotoImage(Image.open("background_subject_page.jpg"))
subject_page_background_image1= Label(subject_frame,image=subject_page_background_image)
subject_page_background_image1.image=subject_page_background_image
subject_page_background_image1.place(x=2,y=2,relheight=1,relwidth=1)
Label(subject_frame,text="LET'S LEARN",font=("times new roman ",40,"bold","underline")).grid(sticky=W,pady=10,padx=450)
Label(subject_frame,text="SUBJECTS :-",font=("system",30,"bold")).grid(sticky=W,padx=8,pady=40,row=1,column=0)
Button(subject_frame,cursor="hand2",text="1. DATA STRUCTURES",command=lambda:raise_frame(index_DS),font=("Helvetica",24)).grid(sticky=W,padx=25,pady=30,row=2,column=0)
Button(subject_frame,text="2. DIGITAL LOGIC DESIGN",command=lambda:raise_frame(index_DLD),cursor="hand2",font=("Helvetica",24)).grid(sticky=W,padx=25,pady=30,row=3,column=0)
Button(subject_frame,text="3. DISCRETE MATHEMATICS",command=lambda:raise_frame(index_DSTL),cursor="hand2",font=("Helvetica",24)).grid(sticky=W,padx=25,pady=30,row=4,column=0)
Button(subject_frame,text="About",cursor="hand2",command=lambda:raise_frame(about_frame),font=("Helvetica",18)).grid(sticky=E,padx=900,pady=30,row=6)


################### DS-INDEX PAGE #################################
Label(index_DS,text="INDEX",font=("times new roman",40,"bold","underline")).grid(sticky=W,padx=25,pady=40,row=1,column=0)
Button(index_DS,text="1. Introduction To Data Structures",cursor="hand2",command=lambda:[raise_frame(intro_to_ds_frame1),intro_to_ds_func(intro_to_ds_frame1)],font=("arial",24)).grid(sticky=W,padx=25,pady=30,row=3,column=0)
Button(index_DS,text="2. STACKS",cursor="hand2",command=lambda:[stack_func(stack_frame),raise_frame(stack_frame)],font=("arial",24)).grid(sticky=W,padx=25,pady=30,row=4,column=0)
Button(index_DS,text="3. QUEUES",cursor="hand2",command=lambda:[raise_frame(queue_frame),queue_func(queue_frame)],font=("ariral",24)).grid(sticky=W,padx=25,pady=30,row=5,column=0)
Button(index_DS,text="BACK",cursor="hand2",command=lambda:raise_frame(subject_frame),font=("arial",12),height=2,width=7).grid(row=21,sticky=W,pady=50,padx=10)

############### DLD-INDEX PAGE ###################################
Label(index_DLD,text="INDEX",font=("times new roman",40,"bold","underline")).grid(sticky=W,padx=25,pady=40,row=1,column=0)
Button(index_DLD,text="Boolean Algebra and Logic Gates",cursor="hand2",command=lambda:[raise_frame(boolean_algebra),boolean_algebra_func(boolean_algebra)],font=("arial",24)).grid(sticky=W,padx=25,pady=30,row=3,column=0)
Button(index_DLD,text="BACK",cursor="hand2",command=lambda:raise_frame(subject_frame),font=("arial",12),height=2,width=7).grid(row=21,sticky=W,pady=50,padx=10)

############### DSTL-INDEX PAGE ###################################
Label(index_DSTL,text="INDEX",font=("times new roman",40,"bold","underline")).grid(sticky=W,padx=25,pady=40,row=1,column=0)
Button(index_DSTL,text="SET THEORY",cursor="hand2",command=lambda:[raise_frame(set_theory),set_theory_func(set_theory)],font=("arial",24)).grid(sticky=W,padx=25,pady=30,row=3,column=0)
Button(index_DSTL,text="BACK",cursor="hand2",command=lambda:raise_frame(subject_frame),font=("arial",12),height=2,width=7).grid(row=21,sticky=W,pady=50,padx=10)

############### ABOUT - FRAME #######################################
Message(about_frame,text="This a a software platform started as a college project for helping students in thier Academic studies. This package includes regular practice with interactive exercises and Theory to learn from.\n\n        DATE STARTED :- 6 SEPTEMBER,2017.\n\n\n\n\n\n\n\n\n    -KARTIK GIRI",font=("arial",18),width=screen_width-70).grid(padx=10,pady=10,sticky=W)
Button(about_frame,text="BACK",cursor="hand2",command=lambda:raise_frame(subject_frame),font=("arial",12),height=2,width=7).grid(row=21,sticky=W,pady=50,padx=10)

raise_frame(subject_frame)
root.mainloop()