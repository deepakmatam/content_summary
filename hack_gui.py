import Tkinter
from tkFileDialog import askopenfilename
m = Tkinter.Tk()
m.title('News categorizer ')
m.minsize(width=566, height=450)

def choosefile():
	filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
	label = Tkinter.Label( m, text = filename )
	label.pack()
	
def categorize():
	input_list = []

	with open('c:/python27/words.txt','r') as f:
		for line in f:
			for word in line.split():
				chars_to_remove=['.',',','?','!','@','#','$','%','^','&','*',')','(','-','_','+','=','{','}','[','}','|','<','>',':',';','"']
				r=word.translate(None, ''.join(chars_to_remove))
				input_list.append(r) #print(word)
			 
		    
#print input_list

	stop_words_list = []

	with open('stop_words.txt','r') as f:
		for line in f:
			for word in line.split():
				stop_words_list.append(word)
			
	c_list = []
	c_list = list(set(input_list) - set(stop_words_list))		
	c_list = list(set(c_list))

	sports_list,entertainment_list,politics_list,business_list = [],[],[],[]

	with open('sports.txt','r') as f:
		for line in f:
			for word in line.split(','):
				sports_list.append(word)

	with open('politics.txt','r') as f:
		for line in f:
			for word in line.split(','):
				politics_list.append(word)
			
	with open('entertainment.txt','r') as f:
		for line in f:
			for word in line.split(','):
				entertainment_list.append(word)
			
	with open('business_2.txt','r') as f:
		for line in f:
			for word in line.split(','):
				business_list.append(word)

#print politics_list

	sports_count,ent_count,politics_count,business_count,other_count = 0,0,0,0,0

	for item in c_list:
		if item in sports_list:
			sports_count +=1
		if item in entertainment_list:
			ent_count +=1
		if item in politics_list:
			politics_count +=1
		if item in business_list:
			business_count +=1
	#else:
	#	other_count +=1

	dict = {'sports':sports_count,'Entertainment':ent_count,'politics':politics_count,'Business':business_count,'other':other_count}

	print dict

	result = max(dict,key = dict.get)
	fresult = 'This news is about ',result
	if result == 'other':
		print "This content does not belong to any news"
	else:  
		label = Tkinter.Label( m, text = fresult )
		label.pack()
	
	
	

B_choose = Tkinter.Button(m, text ="choose a file", command = choosefile)
B_choose.place(x=250,y=130)


categorize = Tkinter.Button(m, text ="categorize", command = categorize)
categorize.place(x=255,y=170)



m.mainloop() 