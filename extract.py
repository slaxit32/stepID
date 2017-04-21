import csv
import numpy



exampleFile = open('output.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)

def all_indices(value, qlist):
    indices = []
    idx = -1
    while True:
        try:
            idx = qlist.index(value, idx+1)
            indices.append(idx)
        except ValueError:
            break
    #print(indices)
    return indices

def std():
	x=[]
	y=[]
	z=[]
	sec=[]
	for i in range (len(exampleData)):
		x.append(exampleData[i][1])
		y.append(exampleData[i][2])
		z.append(exampleData[i][3])
		sec.append(int(exampleData[i][5]))

	# for i in range (len(sec)):
	# 	print(sec[i])

	temp1=list(set(sec))
	temp1.sort()

	rem=[]
	
	for j in range(len(temp1)):
		
		temp2=all_indices(j, sec)

		x2=[]
		y2=[]
		z2=[]

		for i in range(len(temp2)):
			x2.append(float(x[i]))
			y2.append(float(y[i]))
			z2.append(float(z[i]))
		
		re=[]
		re.append(numpy.std(x2))
		re.append(numpy.std(y2))
		re.append(numpy.std(z2))
		#print(re)

		rem.append(re)
	return rem


def aad():
	x=[]
	y=[]
	z=[]
	sec=[]
	for i in range (len(exampleData)):
		x.append(exampleData[i][1])
		y.append(exampleData[i][2])
		z.append(exampleData[i][3])
		sec.append(int(exampleData[i][5]))

	# for i in range (len(sec)):
	# 	print(sec[i])

	temp1=list(set(sec))
	temp1.sort()

	rem=[]
	
	for j in range(len(temp1)):
		
		temp2=all_indices(j, sec)

		x2=[]
		y2=[]
		z2=[]

		for i in range(len(temp2)):
			x2.append(float(x[i]))
			y2.append(float(y[i]))
			z2.append(float(z[i]))
		
		re=[]
		#print(x2,"\n\n")
		re.append(numpy.average(numpy.absolute(numpy.diff(x2))))
		re.append(numpy.average(numpy.absolute(numpy.diff(y2))))
		re.append(numpy.average(numpy.absolute(numpy.diff(z2))))
		#print(re)

		rem.append(re)
	return rem

def ave():
	x=[]
	y=[]
	z=[]
	sec=[]
	for i in range (len(exampleData)):
		x.append(exampleData[i][1])
		y.append(exampleData[i][2])
		z.append(exampleData[i][3])
		sec.append(int(exampleData[i][5]))

	# for i in range (len(sec)):
	# 	print(sec[i])

	temp1=list(set(sec))
	temp1.sort()

	rem=[]
	
	for j in range(len(temp1)):
		
		temp2=all_indices(j, sec)

		x2=[]
		y2=[]
		z2=[]

		for i in range(len(temp2)):
			x2.append(float(x[i]))
			y2.append(float(y[i]))
			z2.append(float(z[i]))
		
		re=[]
		#print(x2,"\n\n")
		re.append(numpy.average(x2))
		re.append(numpy.average(y2))
		re.append(numpy.average(z2))
		#print(re)

		rem.append(re)
	return rem

def arv():
	x=[]
	y=[]
	z=[]
	sec=[]
	for i in range (len(exampleData)):
		x.append(exampleData[i][1])
		y.append(exampleData[i][2])
		z.append(exampleData[i][3])
		sec.append(int(exampleData[i][5]))

	# for i in range (len(sec)):
	# 	print(sec[i])

	temp1=list(set(sec))
	temp1.sort()

	rem=[]
	
	for j in range(len(temp1)):
		
		temp2=all_indices(j, sec)

		x2=[]
		y2=[]
		z2=[]

		for i in range(len(temp2)):
			x2.append(float(x[i]))
			y2.append(float(y[i]))
			z2.append(float(z[i]))
		
		re=[]
		for k in range(len(x2)):
			re.append(numpy.sqrt(x2[k]*x2[k]+y2[k]*y2[k]+z2[k]*z2[k]))


		rem.append(numpy.average(re))
	return rem

print(arv())