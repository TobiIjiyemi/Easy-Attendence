from os import sys
import os
import sys
from datetime import datetime

# current date and time

def Overwrite(userTxt):
  noOfStudents = int(input("Enter the number of Students in your class: "))
  studentsList = []
  try:
    fileCreater = open(userTxt, "w+")
    for x in range(noOfStudents):
      studentName = input("Enter your next student's name: ")
      studentsList.append(studentName)
    for name in studentsList:
      #its in a for loop "for [name] in studentsList"
      #smh overwrite whyy did you do this to us :((
      fileCreater.write(name + ",")
      fileCreater.read()
  except:
    print("Sorry, there was an error. Please try again.")


def add(userText):
  filename = userText + ".txt"
  f = open(filename, "x+")
  #yea it must be the overwrite.
  Overwrite(filename)
  f.close()

def Openfile(userTxt):
  f = open(userTxt)
  contents = f.read()
  f.close()
  print(contents)

def delete(filename):
  try:
    os.remove(filename)
  except:
    print("Couldn't delete file.")
  
def startAttendance(filename):
  print(filename)
  try:
    presentStudents = []
    absentStudents = []
    f = open(filename, "r")
    referenceList = list(f.read().split(","))
    # ['tobi', 'visu', 'thiru', 'nihal', ' ']
    referenceList.pop()
    for student in referenceList:
      currentIn = input(f"Is {student} present? [Type yes or no]: ")
      if currentIn.lower() == "yes":
        presentStudents.append(student)
      elif currentIn.lower() == "no":
        absentStudents.append(student)
      else:
        while (currentIn.lower() != "yes"  and currentIn.lower() != "no"):
          currentIn = input(f"Is {student} present? [TYPE IN YES OR NO]: ")
          if currentIn.lower() == "yes":
            presentStudents.append(student)
          elif currentIn.lower() == "no":
            absentStudents.append(student)
    print(f"\nPresent students: {presentStudents}")
    print(f"Absent Students: {absentStudents}")
  except:
    print(f"Error")

def uc():
  userChoice = input("Would you like to [overwrite], [add], [display existing], [start attendance] or \n[delete] students? Please type add, overwrite, display existing, or start attendance.")
  if userChoice == "overwrite":
    print("Let's Start.")
    userTxt = input("Which file do you want to overwrite? Name the file as \nnameoffile.txt: ")
    Overwrite(userTxt)
    uc()
  elif userChoice == "add":
    userTxt = input("What is the name of your class:\n ")
    #adds a file with the user input
    #here here here here
    add(userTxt)
    uc()
  elif userChoice == "display existing":
    userTxt = input("Which file do you want to see? Name the file as \nnameoffile.txt: ")
    print("Here are your students: ")
    #opens the specified file
    Openfile(userTxt)
    uc()
  elif userChoice == "delete":
    userTxt = input("Which file do you want to delete: ")
    delete(userTxt)
    uc()
  elif userChoice == "start attendance":
    filename = input("Which file do you want to use? ")
    startAttendance(filename)
    uc()
  else:
    print(f"Thank you for using (project name) :)")
    sys.exit()
uc()