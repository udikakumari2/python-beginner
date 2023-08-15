import examMarks as em

name,sid,e,s,m=em.getInfo()
average=em.calAvg(e,s,m)
status=em.status(average)

print('Name:',name)
print('Average:',average)
print('Status:',status)
