print(
" MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n",
"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n",
"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n",
"MMMMMMMMshMMMMMMMMmoNMMMMMMMMMy:/MMMMMMMMMMN::dMMMMMMN+mMMMMMMMo:oMMMMMMMMh+-.-:sNMMMMMMs:::::::::yMMMMMMNodMMMMMMMMMMh+:-.-:+hMMMMMMMo::::::/hMMMMMMMMh/-.-/sNMMMMMMMMMMM\n",
"MMMMMMMM/ /MMMMMMMd  /mMMMMMMMo `MMMMMMMMMMN  yMMMMMMN  hMMMMMM/ :MMMMMMM/ `shy/.yMMMMMMhsss  :ssmMMMMMMN` hMMMMMMMMo` -oyhyssNMMMMMMM- -ssssNMMMMMMMM+ -shy/ `hMMMMMMMMMM\n",
"MMMMMMMM/ -MMMMMMMd    :dMMMMMo `MMMMMMMMMMN  yMMMMMMN  yMMMMMM/ :MMMMMMM` /MMMMMMMMMMMMMMMM` sMMMMMMMMMm  hMMMMMMN- -mMMMMMMMMMMMMMMM- /MMMMMMMMMMMMMMdMMMMM: :MMMMMMMMMM\n",
"MMMMMMMM/ -MMMMMMMd  s/  -yMMMo `MMMMMMMMMMN  yMMMMMMN  yMMMMMM/ :MMMMMMMd- `:ohNMMMMMMMMMMM` sMMMMMMMMMm  hMMMMMMo `NMMMMMMMMMMMMMMMh` .///yMMMMMMMMMMMMMMMy  yMMMMMMMMMM\n",
"MMMMMMMM/ -MMMMMMMd  dMm+` .sNo `MMMMMMMMMMN  yMMMMMMN  yMMMMMM/ :MMMMMMMMMNy+- `+MMMMMMMMMM` sMMMMMMMMMm  hMMMMMM+ .MMMMMMMMMMMMMMMyo. .ooohMMMMMMMMMMMMMN/ .hMMMMMMMMMMM\n",
"MMMMMMMM/ -MMMMMMMd  dMMMNo` `- `MMMMMMMMMMm  hMMMMMMN  yMMMMMM: :MMMMMMMMNMMMMd` sMMMMMMMMM` sMMMMMMMMMm  hMMMMMMh  hMMMMMMMMMMMMMMMM- /MMMMMMMMMMMMMMMMs` +NMMMMMMMMMMMM\n",
"MMMMMMMM/ -MMMMMMMd  dMMMMMNs.  `MMMMMMMMMMh  dMMMMMMM: -mMMMMy  yMMMMMMd.-mMMMd  yMMMMMMMMM` sMMMMMMMMMm  hMMMMMMMs  +mMMMMMMMMMMMMMM- /MMMMMMMMMMMMMMd- :mMMMMMMMMMMMMMM\n",
"MMMMMMMM/ -MMMMMMMd  dMMMMMMMMy-`MMMMMN/`::  oMMMMMMMMNo` -::. -yMMMMMMMMo` -:- `sMMMMMMMMMM`:dMMMMMMMMMm  hMMMMMMMMm+. `-::..yMMMMMMM- `....:hMMMMMMN/   ....-yMMMMMMMMMM\n",
"MMMMMMMMdhdMMMMMMMNhhNMMMMMMMMMMdMMMMMMmysshNMMMMMMMMMMMMdysshmMMMMMMMMMMMNhysydMMMMMMMMMMMMdMMMMMMMMMMMMhhNMMMMMMMMMMMmhyssydMMMMMMMMdhhhhhdMMMMMMMMdhhhhhhhhNMMMMMMMMMMM\n",
"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n",
"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n",
"MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n"
)


def isanumber(p):
	try:
		int(p)
		return True
	except ValueError:
		try:
			float(p)
			return True
		except ValueError:
			return False

def format_color(p):
	p = int(p)	# Gets rid of optional "+" sign, keeps "-"

	Color_Off = "\033[0m"
	Red = "\033[0;31m"          # Red
	Green = "\033[0;32m"        # Green

	if p > 0:	# Positive is green text prefaced by a "+" symbol
		p = "\033[0;32m+" + str(p) + "\033[0m"
	elif p < 0: 
		p = "\033[0;31m" + str(p) + "\033[0m"

	return p

if __name__ == "__main__":		# Main begin
	
	while (1):
		print("Welcome to the Injustice 2 Gear Comparitor\n\n")

		prompt1 = ""
		prompt2 = ""
		prompt3 = ""
		prompt4 = ""

		p1 = False
		p2 = False
		p3 = False
		p4 = False

		types = ["Attack ", "Ability", "Defense", "HP     "]

		while not p1:
			prompt1 = input ("1. (ATTACK) stat: ")
			if prompt1 == 'error':
				continue
			p1 = isanumber(prompt1)
			if p1 == False:
				print("\033[0;31m"+"Invalid Input. Try Again with an Integer."+ "\033[0m")


		while not p2:
			prompt2 = input ("2. (ABILITY) stat: ")
			if prompt2 == 'error':
				continue
			p2 = isanumber(prompt2)
			if p2 == False:
				print("\033[0;31m"+"Invalid Input. Try Again with an Integer."+ "\033[0m")

		while not p3:
			prompt3 = input ("3. (DEFENSE) stat: ")
			if prompt3 == 'error':
				continue
			p3 = isanumber(prompt3)
			if p3 == False:
				print("\033[0;31m"+"Invalid Input. Try Again with an Integer."+ "\033[0m")

		while not p4:
			prompt4 = input ("4. (HP) stat: ")
			if prompt4 == 'error':
				continue
			p4 = isanumber(prompt4)
			if p4 == False:
				print("\033[0;31m"+"Invalid Input. Try Again with an Integer."+ "\033[0m")

		prompts = [prompt1, prompt2, prompt3, prompt4]
		num_prompts = [int(prompt1), int(prompt2), int(prompt3), int(prompt4)]

		print("==============================")
		for i in range(len(prompts)):
			prompts[i] = format_color(prompts[i])
			print(types[i],": \t" , prompts[i])

		total_sum = sum(num_prompts)
		print("\nITEM SCORE IS \033[1;32m", format_color(total_sum), "\033[0m")
		print("==============================")

		valid = False
		while not valid:
			user_inp = input ("Continue?: (Y/N) ")
			if user_inp == "":
				print("**** Empty Entry. Try Again. ****")
				continue
			if user_inp[0].lower() == 'y' or user_inp == '1':
				valid = True
				print("\n\n\n")
				break
			elif user_inp[0].lower() == 'n' or user_inp == '0':
				valid = True
				print("Thank you for using the Injustice Comparitor")
				print("Exiting back to Terminal ...\n\n\n")
				exit()
			else: 
				print("**** Invalid Entry. Try Again. ****")
				continue


