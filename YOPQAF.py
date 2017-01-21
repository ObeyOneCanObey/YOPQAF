import pickle
import os
import random
field=open('fields.dat','rb')
#functions&classes#############################
fields=[]
def prompt():
    print "+++++++COMMANDS+++++++"
    print "Choose your action:"
    print "1.Ask a question"
    print "2.Give Answers"
    print "3.Add subjects"
    print "4.Remove subjects"
    print "5.Display subjects"
    print "6.Display Questions and Answers"
    print "7.Generate Questions"
    print "8.Exit"
    global c
    c=input("Enter your choice:")
    print "======================="
class QA():
    def __init__(self,q,a):
        self.q=q
        self.a='Not Answered'
    def Q(self):
        self.q=raw_input("Enter your question:")
    def A(self):
        self.a=raw_input("Enter your answer:")
    def OQ(self):
        print self.q
    def display(self):
        print "Question:",self.q
        print "Answer:"
        print self.a
#Main#########################################
print 'Welcome to your own personal question answer forum.'
print 'Having trouble keeping a track of you questions and answers?'
print 'Now you can store everythong easily and systematically!!'

field=open('fields.dat','rb')
fields=pickle.load(field)
field.close()

while 1==1:
    prompt()
    if c==1:
        print "+++++++++++ASK QUESTIONS+++++++++++++"
        print "Subjects:"
        for i in range(len(fields)):
            print i+1,".",fields[i]
        x1=input("Choose your subject number:")
        sub=open(fields[x1-1]+'.txt','ab+')
        q=QA('a','b')
        q.Q()
        pickle.dump(q,sub)
        sub.close()
        print "====================================="
    elif c==2:
        print "+++++++++++ANSWER QUESTIONS+++++++++++++"
        for i in range(len(fields)):
            print i+1,".",fields[i]
        x1=input("Choose your subject number:")
        sub=open(fields[x1-1]+'.txt','rb+')
        n=1
        try:
            while True:
                x2=pickle.load(sub)
                print n,'.'
                x2.display()
                n+=1
        except EOFError:
            ''
        sub.close()
        x5=input('Enter question number:')
        sub=open(fields[x1-1]+'.txt','rb+')
        subn=open(fields[x1-1]+'a'+'.txt','wb+')
        n=1
        try:
            while True:
                x2=pickle.load(sub)
                if n==x5:
                    x2.A()
                    x2.display()
                    n+=1
                    pickle.dump(x2,subn)
                else:
                    n+=1
                    pickle.dump(x2,subn)
        except EOFError:
            ''
        sub.close()
        subn.close()
        os.remove(fields[x1-1]+'.txt')
        os.rename(fields[x1-1]+'a'+'.txt',fields[x1-1]+'.txt')
        print "====================================="
    elif c==3:
        print "+++++++++++ADD SUBJECTS+++++++++++++"
        xname=raw_input("Enter subject name:")
        fields.append(xname)
        fieldw=open('fields.dat','wb')
        pickle.dump(fields,fieldw)
        fieldw.close()
        print "====================================="
    elif c==4:
        print "+++++++++++REMOVE SUBJECTS+++++++++++++"
        print "Subjects:"
        for i in range(len(fields)):
            print i+1,".",fields[i]
        xn=input("Enter subject number:")
        print fields.pop(xn-1),'has been removed.' 
        fieldw=open('fields.dat','wb')
        pickle.dump(fields,fieldw)
        fieldw.close()
    elif c==5:
        print "+++++++++++DISPLAY SUBJECTS+++++++++++++" 
        for i in range(len(fields)):
            print i+1,".",fields[i]
    elif c==6:
        print "+++++++++++DISPLAY Q&A's OF SUBJECTS+++++++++++++"
        print "Subjects:"
        for i in range(len(fields)):
            print i+1,".",fields[i]
        x1=input("Choose your subject number:")
        sub=open(fields[x1-1]+'.txt','rb+')
        try:
            while True:
                x2=pickle.load(sub)
                x2.display()
        except EOFError:
            pass
        print "====================================="
    elif c==7:
        print "Subjects:"
        for i in range(len(fields)):
            print i+1,".",fields[i]
        xn=input("Enter subject number:")
        sub=open(fields[xn-1]+'.txt','rb+')
        ques=[]
        try:
            while True:
                x2=pickle.load(sub)
                ques.append(x2)
        except EOFError:
            pass
        sub.close()
        print "+++++++++++++++++++++++QUESTIONS++++++++++++++++++++++"
        random.shuffle(ques)
        for i in range(len(ques)):
            print 'Question',i+1,':'
            print ques[i].q
        chans=raw_input('Would you like to display answers?')
        if chans=='y':
            for i in range(len(ques)):
                print 'Question',i+1,':'
                print ques[i].q
                print 'Answer:'
                print ques[i].a       
    elif c==8:
        xfin=raw_input("Are you sure you want to quit?(y/n)")
        if xfin=='y':
            exit()
            
    

