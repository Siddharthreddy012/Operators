#Logical operator on real time persons based on their gov jobs
Exam=False
Sports=False
print(Exam)
print(Sports)

dhoni={'Exam': True ,'Sports' : True}
Exam=dhoni['Exam']
Sports=dhoni['Sports']
print("Exam : ",Exam)
print("Sports : ",Sports)
res=Exam or Sports 
print(res)


siraj={'Exam' : False, 'Sports' : True}
Exam=siraj['Exam']
Sports=siraj['Sports']
print("Exam : ",Exam)
print("Sports : ",Sports)
res=Exam or Sports 
print(res)

siddharth={'Exam' : True, 'Sports' : False}
Exam=siddharth['Exam']
Sports=siddharth['Sports']
print("Exam : ",Exam)
print("Sports : ",Sports)
res=Exam or Sports 
print(res)

venky={'Exam' : False, 'Sports' : False}
Exam=venky['Exam']
Sports=venky['Sports']
print("Exam : ",Exam)
print("Sports : ",Sports)
res=Exam or Sports 
print(res)

