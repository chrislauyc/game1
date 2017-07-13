import Node, GUI, CAL
'''def main():
	# my code here
	#menu
	print "menu (please select an option)"
	print "1-test gui"
	print "2-quit"
	num = raw_input('enter a number: ')
	if num == '1':
		gui = GUI.GUI()
		gui.run_GUI()
		print "im in 1"
	elif num == '2':
		print "im in 2"
		quit()

if __name__ == "__main__":
	main()

'''

#testing GUI.py and CAL.py
myCAL = CAL.CAL()
myGUI = GUI.GUI()
myCAL.Create_board()
myCAL.Set_GUI(myGUI)#so that myCAL can use the same GUI object
myGUI.Power_GUI()
done = False
while (done == False):
	done = myGUI.Run_GUI(done)
	myCAL.Run_board()
	



