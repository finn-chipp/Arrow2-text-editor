def quicksave(feed,filename):
	try:
		f = open(filename, "w")
		f.write(feed)
		f.close()
	except:
		print ("An unexpected error has occured. Please double check your directory and filename, and if there is any illegal characters eg ~ please remove them")
def loadfile(filename):
	try:
		f = open(filename, "r")
		return (f.read())
	except:
		return ("File is presumed not to exist. If you have entered the name correctly then try using a file suffix (such as .py or .txt)")
