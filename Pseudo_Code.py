import numpy as np
from time import sleep

def setup():
	a=np.array([1,0,0,0,0,0])
	b=np.array([1,0,1,0,0,0])
	c=np.array([1,1,0,0,0,0])
	braille=np.zeros((3,2))
	d={"A":a,"B":b,"C":c}
	for i in d:
		d[i]=d[i].reshape(3,2)
	return d,braille

d,braille=setup()

def learning_mode():
	print_voice("You are now in learning mode")
	while True:
		for i in d:
			print(d[i])
			print_voice(i)
			sleep(5)
			print(braille)
			sleep(5)
		print_voice("Do you want to repeat ?")
		if voice():
			print_voice("You chose to return to learning mode")
			continue
		else:
			break

def voice():
	while True:
		obtain_voice()
		if voice_input=="Yes" or voice_input=="No":
			if voice_input=="Yes":
				return True
			else voice_input=="No":
				return False
			print_voice("Didn't quite get you please repeat")

def voice2()
	while True:
		obtain_voice()
		if voice_input in list(d.keys()):
				return voice_input
		print_voice("Didn't quite get you please repeat")

def searching_mode():
	print_voice("You are now in searching mode")
	while True:
		voice2()=k
		print(d[k])
		print_voice(k)
		sleep(5)
		print(braille)
		sleep(5)
		print_voice("Do you want to repeat ?")
		if voice():
			print_voice("You chose to return to searching mode")
			continue
		else:
			break

def obtain():
	obtain_voice()
	return(voice_input)

def testing_mode():
	print_voice("You are now in testing mode")
	while True:
		q=np.random.choice(list(d.keys()))
		print(d[q[0]])
		print_voice(q[0])
		sleep(5)
		print(braille)
		sleep(5)
		if obtain() == q[0]:
			print_voice("Kudos you got that right")
			print_voice("Do you want to continue")
			if voice():
				continue
			else:
				return
		else:
			print_voice("Oops im afraid thats wrong")
			print_voice("Do you want to try again")
			if voice():
				while True:
					print(d[q[0]])
					print_voice(q[0])
					sleep(5)
					print(braille)
					sleep(5)
					if obtain() == q[0]:
						print_voice("Kudos you got that right")
						print_voice("Do you want to continue")
						if voice():
							p=1
							break
						else:
							p=2
							break
					else:
						print_voice("Oops im afraid thats wrong")
						print_voice("Do you want to try again with the same chracter")
						if voice():
							continue
						else:
							print_voice("Do you want to know the answer")
							if voice():
								print_voice(q[0])
							else:
								pass
							print_voice("Do you want to exit testing mode")
							if voice():
								return
							else:
								break
				if p==1:
					continue
				elif p==0:
					return
			else:
				print_voice("Do you want to exit testing mode")
				if voice():
					return
				else:
					break
def choose_mode:
	print_voice("please choose one of the three options searching training testing")
	while True:
		obtain_voice()
		if voice_input=="searching":
			searching_mode()
		elif voice_input=="training":
			testing_mode()
		elif voice_input=="learning":
			learning_mode()
		else:
			print_voice("Didn't quite get you please repeat")


setup()
choose_mode()






						












