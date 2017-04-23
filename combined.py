import os,glob,sys,csv
from pathlib import Path

print("\nCurrent directry "+os.getcwd(),"\n")
print("Combinding files : " ,len(glob.glob("*.csv"))," as ","all_"+str(len(glob.glob("*.csv")))+".txt","\n")

os.chdir(os.getcwd())


fow = open("all_"+str(len(glob.glob("*.csv")))+".txt", "a")
fow.write(str(glob.glob("*.csv")))
fow.close()


for file in glob.glob("*.csv"):
	print(file)
	# os.system('python extract.py '+file)ru	

	fo = open(file, "r")
	line = fo.read()
	fo.close()

	fow = open("all_"+str(len(glob.glob("*.csv")))+".txt", "a")
	fow.write(line);
	fow.close()

