import os,glob,sys

print("Current directry "+os.getcwd(),"\n")

os.chdir(os.getcwd())


for file in glob.glob("*.csv"):
	print(file)
	os.system('python csvMake.py '+file)