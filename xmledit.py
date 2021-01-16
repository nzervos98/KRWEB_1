import xml.etree.ElementTree as ET
import crossfiledialog
from array import *

def browsexmlfile():
    file = crossfiledialog.open_file()
    if file.endswith('.xml'):
        return file
    else:
        exit('NOT AN XML FILE!')

#file = 'schedule.xml'
def getxmldata(file):
    arr = []
    mytree = ET.parse(file)
    myroot = mytree.getroot()
    for lesson in myroot.findall('Lesson'):
        title = lesson.find('Title').text
#       print(title.text)
        professor = lesson.find('Professor')
        if professor is None:
            professor = " "
        else:
            professor = professor.text
#       print(professor.text)
        for lecture in lesson.findall('Lecture'):
            day = lecture.find('Day').text
#           print(day.text)
            time = lecture.find('Time').text
#           print(time.text)
#           print(title + "\n" + day + "\n" + time + "\n" + professor + "\n\n\n")
            arr.append([title, day, time, professor])
    return arr

# dhmiourgia lesson element me ola ta paidia
def addxmldata(file, title, day, time, professor):
    mytree = ET.parse(file)
    root = mytree.getroot()
    lesson_element = ET.SubElement(root, 'Lesson')
    title_element = ET.SubElement(lesson_element, 'Title')
    title_element.text = title
    lecture_element = ET.SubElement(lesson_element, 'Lecture')
    day_element = ET.SubElement(lecture_element, 'Day')
    day_element.text = day
    time_element = ET.SubElement(lecture_element, 'Time')
    time_element.text = time
    professor_element = ET.SubElement(lesson_element, 'Professor')
    professor_element.text = professor
    mytree.write(file)


#arxeio xml
file = browsexmlfile()
#pinakas gia display
xmlarray = getxmldata(file)
xmlarray.insert(0, ['Title', 'Day', 'Time', 'Professor'])
#oros gia to align tou pinaka (stoixish)
mx = len(max((sub[0] for sub in xmlarray),key=len))

#print(xmlarray) test

while True:
    case = input('What to do with given .xml file?\n1) View XML data.\n2) Add data to .xml file.\n3) Exit.\n')
    if case == '1':
        for row in xmlarray:
            #print pinaka stoixismenou
            print(" ".join(["{:<{mx}}".format(ele, mx=mx) for ele in row]))
        print("\n")
    elif case == '2':
        new_title = input("Provide lesson title:\n")
        new_professor = input("Provide the name of the professor:\t(Can be left blank)\n")
        lecture_num = int(input("How many lectures does the new lesson have?\n"))
        for x in range(lecture_num):
            num = str(x+1)
            new_day = str(input("Provide day of lecture number " + num + ":\n"))
            new_time = input("Provide time of lecture number " + num + ":\t(In format hh-hh)\n")

            #add data to xml array for display in-app
            xmlarray.append([new_title, new_day, new_time, new_professor])
            #add data to xml file
            addxmldata(file, new_title, new_day, new_time, new_professor)


    elif case == '3':
        break
    else:
        print("Woops, there is no such option!\n")
        continue