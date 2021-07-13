1. Develop a flutter based app with two screens. 
 Screen1: A form to add a student with details name, 
 qualification, 
 percentage. A table below the form to display all the existing student data. 

screen 2: A dashboard page which displays below details.
Total student count. 
Counts of student by qualifications. 
Count of students by percentage brackets 70+ 80+ etc. 

Note: Dashboard should be implemented using websockets with autorefresh of updates. 

2. Backend should be developed with Django rest framework and postgresql

3. Should be deployed using EC2 instance.


Model Student.

name,
qualification,
percentage



api /students
{
    name:
    qualification:
    percentage:
}


websockets
autorefresh