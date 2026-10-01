# Q2. Attendance tracker (~12 min)
# Write attendance_report(students) where students is a dict of
# {name: [list of present days, e.g. 1 for present, 0 for absent]}.
# Return a new dict with each student's attendance percentage.

# 1. Create an empty dict called report.
# 2. Repeat for each name, days in students.items():
#    a. Count how many 1s are in days (use a loop or sum()).
#    b. Calculate percentage = (count / len(days)) * 100.
#    c. Add name: percentage to report.
# 3. Return report.
# 4. Loop through report and print "Name: X%" for each student.


def report(student):
    
    report = {}
    
    for name, days in student.items():
         count = 0 
         for value in days:
             
            if value == 1:
                 count += 1
                 
            percent = (count/len(days)) * 100
            report[name] = percent
            
            
    return report


student = {
    "Vishwajeet singh": [1,1,0,1,1],
    "Rahul" : [0,0,1,1,0]
}

print(report(student))