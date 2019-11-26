#What you need as a data_scientist

import numpy as np
import matplotlib.pyplot as plt

class data_scientist():
   def __init__(self):
     self.__languages=0
     self.__skills=0
     self.__experience=0
     self.__name=''
     self._skillset=list()
     self._names=list()
     self._knownlanguages=list()
     self._experiences=list()
     self.count=0
        
   def writetofile(self):
        with open('datascientist.txt','a') as fobj:
            fobj.write(self.__name +self. __languages + self.__skills + self.__experience)
    
   def assign(self):
      self.__name=input("What's your name ? ")+','
      self.__languages=input("\n\nHow many languages you're comfortable with, outof~\nPython | Scala | R | Ruby | Hadoop | JavaScript | C++ | SQL :")+','
      self.__skills=input('\n\nConcepts you can utilise, outof~\nData_Mining | Data_Logging | Data_Filtering | Data_Preprocessing | Data_Visualization | Big_DataHandling | Machine_Learning | NeuralNetworks :')+','
      self.__experience=input('\n\nExperience in years: ')+'\n'
      with open('datascientist.txt','r') as fobj:
         check=[line[0] for line in fobj]
      if self.__name not in check:
         self.writetofile()
      else:
         print('Username not available, Choose another :) ')

   def operations(self):
      print('~~~~~Welcome To DataScience Global Dataset~~~~~\n1/ Contribute To Dataset\t2/See Entries\t3/Data_Visualization !\n\n')
      return int(input('Your Choice: '))

   def displayentries(self):
      print(self._names)
      print(self._knownlanguages)
      print(self._skillset)
      print(self._experiences)
        
   def accumulator(self,flag=0):
      with open('datascientist.txt','r') as fobj:
         for lines in fobj:
            if len(lines)-1:
               data=lines.split(',')
               self._names.append(data[0])
               self._knownlanguages.append(data[1])                
               self._skillset.append(data[2])
               self._experiences.append(data[3])
               self.count+=1
      self._knownlanguages=list(map(int, self._knownlanguages))
      self._skillset=list(map(int, self._skillset))
      self._experiences=list(map(int, self._experiences))
      if flag:
         self.displayentries()
        
   def draw_insights(self):
        xlab=['Data_Mining','Data_Logging','Data_Filtering','Data_Preprocessing','Data_Visualization','Big_DataHandling','Machine_Learning','Neural Networks']
        ylab=['Python','Scala','R','Ruby','Hadoop','JavaScript','C++','SQL']
        col=['springgreen','indigo','blue','green','yellow','orange','red','purple','cyan']
        if(self.count>9):
            col*= int(self.count/9)+1
        size=np.array(self._experiences)
        size*=300
        plt.grid()
        plt.scatter(x=self._skillset ,y=self._knownlanguages ,s=size ,c=col[:self.count] ,alpha=1)
        plt.xticks([1,2,3,4,5,6,7,8],xlab)
        plt.yticks([1,2,3,4,5,6,7,8],ylab)
        plt.xlabel('Skillset -->')
        plt.ylabel('Languages -->')
        plt.title('~DataScientist Quotient~')
        for i in range(self.count):
            plt.text(self._skillset[i],self._knownlanguages[i],self._names[i])
        plt.show()
        
#driver_code

continue_=1
while(continue_):
    data_scientist_object = data_scientist()
    ch=data_scientist_object.operations()
    if ch==1:
        data_scientist_object.assign()
    elif ch==2:
        data_scientist_object.accumulator(1)
    elif ch==3:
        data_scientist_object.accumulator()
        data_scientist_object.draw_insights()
    else:
        print('Oh Please ! ')
        
    continue_=int(input('Continue? 0/1: '))
