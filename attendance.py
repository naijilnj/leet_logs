#n = int(input("No of Employees: "))
#
#emp_dict = {}
#
#for i in range(n):
# empname = input("Enter Employee Name: ")
# days = int(input("Enter No of Days: "))
# late = int(input("Enter No of late days: "))
# emp_dict[empname] = [days,late]
#
#print(emp_dict)


emp_dict = {
'Ravi':[22,3],
'Neha':[18,6],
'Simran':[25,0],
'Arjun':[20,8],
'Meera':[15,1]
}

for i in emp_dict:
 if emp_dict[i][0] < 20:
  if emp_dict[i][1] == 0:
    print(f"{i}: Poor Attendance, Perfect")
  elif emp_dict[i][1] >= 1 and emp_dict[i][1] <= 3:
    print(f"{i}: Poor Attendance, Satisfactory")
  else:
    print(f"{i}: Poor Attendance, Needs Improvement")
 elif emp_dict[i][0] >= 20 and emp_dict[i][1] <= 5:
   if emp_dict[i][1] == 0:
    print(f"{i}: Good Attendance, Perfect")
   elif emp_dict[i][1] >= 1 and emp_dict[i][1] <= 3:
    print(f"{i}: Good Attendance, Satisfactory")
   else:
    print(f"{i}: Good Attendance, Needs Improvement") 
 else:
  if emp_dict[i][1] == 0:
    print(f"{i}: Average Attendance, Perfect")
  elif emp_dict[i][1] >= 1 and emp_dict[i][1] <= 3:
    print(f"{i}: Average Attendance, Satisfactory")
  else:
    print(f"{i}: Average Attendance, Needs Improvement")

count=0
for i in emp_dict:
 if emp_dict[i][1] == 0:
  print("Summary of punctual employees:")
  pass
  print(i)
  count+=1
print(f"Total Punctual Employees",count)

