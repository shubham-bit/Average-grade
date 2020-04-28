data_valid = False

while data_valid == False:
    grade1 = float (input("Type the grade of the first test:"))
    if grade1 < 0 or grade1 > 10:
        print("Grade should be between 0 and 10")
        continue
    else:
        data_valid = True

data_valid == False:
    grade2 = float(input("Type the grade of the second test:"))
    if grade2<0 or grade2> 10:
        print("Grade should be between 0 and 10:)
              continue
            else:
                data_valid = True
                
while data_valid == False:
    absences = int(input("True the number of absences:"))
                if absences <0 or absences > total_classes:
                    print ("The number of absences can't be less than zero or greater than the number of total classes.")
                    continue
                else:
                    data_valid = True

avg_grade = (grade1+grade2)/2
attendance = (total_classes-absences)/ tota_classes
print("average grade:", round(avg_grade,2))
print("attendance rate:", str(round((attendance*100),2))+'%')
                    
        
    
