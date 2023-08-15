def getInfo():
    name=input('Name:')
    sid=input('Student ID:')
    e=int(input('English Marks:'))
    s=int(input('Science Marks:'))
    m=int(input('Maths Marks:'))

    return name,sid,e,s,m

def calAvg(e,s,m):
    avg=(e+s+m)/3

    return avg

def status(avg):
    if avg>=50:
        status='PASS'
    else:
        status='FAIL'

    return status    
