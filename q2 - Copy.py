import pandas
#قراءة ملف excel
excel_df = pandas.read_excel('EMP.xlsx', sheet_name='hm')

#تحويله لملف txt
data = excel_df.to_csv(index=False)
with open(file='myEmp.txt',mode='w') as file:
    file.write(data)
    
#ايجاد الmin,max,avarage
min_Experience=excel_df.Experience.min()
min_Salary=excel_df.Salary.min()
min_Age=excel_df.Age.min()
    
max_Experience=excel_df.Experience.max()
max_Salary=excel_df.Salary.max()
max_Age=excel_df.Age.max()


mean_Experience=excel_df.Experience.mean()
mean_Salary=excel_df.Salary.mean()
mean_Age=excel_df.Age.mean()

#اضافه الmin,max,avarage الى اخر صف
min_rows={'EmployeeName':"min",'Experience':min_Experience,'Salary':min_Salary,'Age':min_Age}
excel_df=excel_df.append(min_rows,ignore_index=True)

max_rows={'EmployeeName':"max",'Experience':max_Experience,'Salary':max_Salary,'Age':max_Age}
excel_df=excel_df.append(max_rows,ignore_index=True)

mean_rows={'EmployeeName':"mean",'Experience':mean_Experience,'Salary':mean_Salary,'Age':mean_Age}
excel_df=excel_df.append(mean_rows,ignore_index=True)
excel_df.to_excel('EMP.xlsx', sheet_name='hm',index=False)

#الزياده على الsalary بمقدار 5 وانشاء عامود جديد  
excel_df["new salary"]=excel_df["Salary"]+5

#تحويله الى csv
excel_df.to_csv('EmployeeStatistics.csv', index=False)


    
