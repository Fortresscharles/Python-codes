class wahala:
    course_name = []
    cour_unit = []
    CA_score = []
    Exam_score = []
    total_score = []
    Product_unit_and_Points = []
    gpa_array = []
    points = []

    def __init__(self):
        matric = input("enter matric No:")
        print(str(matric))
        name = input("enter Student Name:")
        wahala.first_semester(self)
        wahala.second_semester(self)
        wahala.GPA_total(self)

    def first_semester(self):
        wahala.record(self)
        wahala.Total(self)
        print("First semester result recorded")

    def second_semester(self):
        wahala.record(self)
        wahala.Total(self)
        print("second semester result recorded")


    def Total(self):
        total_cour_unit = sum(wahala.cour_unit)
        total_points = sum(wahala.Product_unit_and_Points)
        gpa = total_points/total_cour_unit
        wahala.gpa_array.append(gpa)

    def GPA_total(self):
        ok = sum(wahala.gpa_array)
        cgpa = ok/2
        print(f'Your CGPA is = {cgpa}')



    def record(self):
        cour = float(input("enter Number of Courses:"))
        i = 0
        while(i<cour):
            cn = input("enter Course Name:")
            unit = float(input(f'enter credit unit for {cn}:'))
            test = int(input("enter CA Score:"))
            exam = int(input("enter Exam score:"))
            add = test+exam
            i+=1
            wahala.course_name.append(cn)
            wahala.cour_unit.append(unit)
            wahala.CA_score.append(test)
            wahala.Exam_score.append(exam)
            wahala.total_score.append(add)

            if(add>=75 and add<=100):
                print("Grade = A and Point = 5")
                wahala.points.append(5)
                wahala.Product_unit_and_Points.append(unit*5)
            elif(add>=65 and add<=74):
                print("Grade = B and Point = 4")
                wahala.points.append(4)
                wahala.Product_unit_and_Points.append(unit*4)
            elif(add>=54 and add<=64):
                print("Grade = C and Point = 3")
                wahala.points.append(3)
                wahala.Product_unit_and_Points.append(unit*3)
            elif(add>=45 and add<=53):
                print("Grade = D and Point = 2")
                wahala.points.append(2)
                wahala.Product_unit_and_Points.append(unit*2)
            elif(add>=35 and add<=44):
                print("Grade = E and Point = 1")
                wahala.points.append(1)
                wahala.Product_unit_and_Points.append(unit*1)
            elif(add>=0 and add<=34):
                print("Grade = F and Point = 0")
                wahala.points.append(0)
            else:
                print("invalid Score")



wahala()


