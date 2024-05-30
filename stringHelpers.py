



def getStringHeight(st:str):
	return len(st.splitlines()) #takes into account all types of newlines. might be slower
	# return st.count("\n") + 1 #only takes into account the new line character \n

def getStringsMaxWidth(strs:list):
	w = 0
	for l in strs:
		w = max(w, len(l))
	return w

def getStringWidth(st:str):
	return getStringsMaxWidth(st.splitlines())
	# w = 0
	# for l in lines:
	# 	w = max(w, len(l))
	# return w


def joinStringsByLine(st1,  st2, separator = ""):
	if len(st1) == 0:
		return st2
	if len(st2) == 0:
		return st1


	lines1 = st1.splitlines()
	lines2 = st2.splitlines()

	h1 = len(lines1)
	h2 = len(lines2)
	maxLines = max(h1, h2)

	if maxLines == 1:
		return st1 + separator + st2


	w1 = getStringWidth(st1)
	pad = " "*w1

	j = ""


	for i in range(maxLines):
		if i > 0:
			j = j + "\n"

		if i < h1 and i < h2:
			j = j + lines1[i].rjust(w1) + separator + lines2[i]
		elif i >= h1:
			j = j + pad + " "*len(separator) +lines2[i] 
		elif i >= h2:
			j = j + lines1[i].rjust(w1) 


	return j


def makeSeparator(padLength:int, numLines:int, anchorIndex:int, separatorChars:list = [" ", "-", "|"]):
	separator = ""
	pad0 = " "*padLength
	# separator = pad0 + (" \n"*(s1[2]-1)) + 
	# for i in range(s1[1]):
	for i in range(numLines):
		if i < anchorIndex:
			separator =  separator + pad0 + separatorChars[0]
		elif i == anchorIndex:
			separator =  separator + pad0 + separatorChars[1]
		else:
			separator =  separator + pad0 + separatorChars[2]
		if i < (numLines - 1):
			separator =  separator + "\n"
	return separator

if __name__ == "__main__":

	# str1 = ""
	# for i in range(5):
	# 	str1 = str1 + "a"*(i+1) + "\n"
	
	# str2 = "b\n"*3

	# print(joinStringsByLine(str1, str2))

	print(makeSeparator(10, 10, 5, ["x", "-", "|"]))
	print("9")


