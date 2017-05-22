##Reading csv Data

import csv

with open("sample.csv","r") as scoreFile:
	scoreFileReader=csv.reader(scoreFile)
	scoreList=[]
	for row in scoreFileReader:
	 if len(row) != 0:
	 	scoreList=scoreList+[row]

print(scoreList)


##Writing - Overwrite

firstname=raw_input('Enter your first name')
lastname=raw_input('Enter your last name')
score1=raw_input('Enter your score1')
score2=raw_input('Enter your score2')
score3=raw_input('Enter your score3')


with open("sample.csv","w") as scoreFile:
	scoreFileWriter=csv.writer(scoreFile)
	scoreFileWriter.writerow([firstname,lastname,score1,score2,score3])
scoreFile.close()

##Append - 

with open("sample.csv","w") as scoreFile:
  
  ## if gender is'male or female'
  
  
  with open("sample.csv","r") as scoreFile:
	gender =raw_input('Enter gender: ')
	scoreFileReader=csv.reader(scoreFile)
	for row in scoreFileReader:
		if field == gender:
			  print row

scoreFile.close()


##