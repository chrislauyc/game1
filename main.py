import CAL
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

myCAL = CAL.CAL()
myCAL.Create_board()
myCAL.Run_board()
myCAL.End_Game()




