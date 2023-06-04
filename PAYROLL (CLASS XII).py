import mysql.connector as mycon
cn = mycon.connect(host="localhost",user="root",password="",database="company")
cur = cn.cursor()

def showAll():
    
    global cn
    global cur
    
    try:
        query="select * from emp"
        cur.execute(query)
        results = cur.fetchall()
        print("*************************************************************************************************")
        print('%5s'%"EMPNO",'%-15s'%'EMP NAME','%-12s'%'DEPARTMENT','%10s'%'SALARY(MONTHLY)','%15s'%'DOJ','%-25s'%'ADDRESS')
        print("*************************************************************************************************")
        count=0
        for row in results:
            print('%5s' % row[0],'%-15s'%row[1],'%-12s'%row[2],'%10s'%row[3],'%15s'%row[4],'%-25s'%row[5])
            count+=1
        print("**************************************** TOTAL RECORD : ",count,"*************************************")
    except:
        print("error")

def addEmp():
    global cn,cur
    print("*****************************************ADD NEW EMPLOYEE*************************************************")
    eno = int(input("Enter employee number :"))
    en = input("Enter employee name :")
    dp = input("Enter department ")
    sl = int(input("Enter Salary :"))
    doj= input("Enter Date of joining :")
    ad=  input("Enter Address of employee :")
    query="insert into emp values("+str(eno)+",'"+en+"','"+dp+"',"+str(sl)+",'"+doj+"','"+ad+"')"
    cur.execute(query)
    cn.commit()
    #print(query)
    print("!RECORD ADDED SUCCESSFULLY!")

def searchEmp():
    global cn,cur
    print("*****************************************SEARCH EMPLOYEE FORM ********************************************")
    x=int(input("Enter 1 to search by empname and 2 to search by empno."))
    if x==1:
        em=input("Enter the first character of the name to be searched:")
        query="select * from emp where empname like '"+em+"%'"
        cur.execute(query)
        results = cur.fetchall()
        if cur.rowcount<=0:
            print(" SORRY! NO MATCHING DETAILS AVAILABLE ")
        else:
       
            print("*******************************************************************************************************")
            print('%5s'%"EMPNO",'%15s'%'EMP NAME','%12s'%'DEPARTMENT','%10s'%'SALARY','%15s'%'DOJ','%-25s'%'ADDRESS')
            print("*******************************************************************************************************")
            for row in results:
                print('%5s' % row[0],'%15s'%row[1],'%12s'%row[2],'%10s'%row[3],'%15s'%row[4],'%-25s'%row[5])
    print("-"*105)

    if x==2:
        en = int(input("Enter Employee number to search :"))
        query="select * from emp where empno="+str(en)
        cur.execute(query)
        results = cur.fetchall()
        if cur.rowcount<=0:
            print(" SORRY! NO MATCHING DETAILS AVAILABLE ")
        else:
       
            print("*******************************************************************************************************")
            print('%5s'%"EMPNO",'%15s'%'EMP NAME','%12s'%'DEPARTMENT','%10s'%'SALARY','%15s'%'DOJ','%-25s'%'ADDRESS')
            print("*******************************************************************************************************")
            for row in results:
                print('%5s' % row[0],'%15s'%row[1],'%12s'%row[2],'%10s'%row[3],'%15s'%row[4],'%-25s'%row[5])
    print("-"*105)
    
def editEmp():
    global cn,cur
    print("********************************************EDIT EMPLOYEE FORM *******************************************")
    en = int(input("Enter Employee number to edit :"))
    ans=1
    while ans!=0:
        query="select * from emp where empno="+str(en)
        cur.execute(query)
        results = cur.fetchall()
        if cur.rowcount<=0:
            print(" SORRY! NO MATCHING DETAILS AVAILABLE ")
        else:       
            print("******************************************************************************************************")
            print('%5s'%"EMPNO",'%15s'%'EMP NAME','%12s'%'DEPARTMENT','%10s'%'SALARY','%15s'%'DOJ','%-25s'%'ADDRESS')
            print('%5s'%" ",'%15s'%'2','%12s'%'3','%10s'%'4','%15s'%'5','%-25s'%'6')
            print("******************************************************************************************************")
        for row in results:
            print('%5s' % row[0],'%15s'%row[1],'%12s'%row[2],'%10s'%row[3],'%15s'%row[4],'%-25s'%row[5])
            
        print("-"*105)
        ans = int(input("Enter the Serial No of the field which you want to update (0 to Exit): "))
        if ans==2:
            ename=input("Enter New Name :")
            query="update emp set empname='"+ename+"' where empno="+str(en)
            cur.execute(query)
            cn.commit()
        if ans==3:
            edepart=input("Enter New Department:")
            query="update emp set department='"+edepart+"' where empno="+str(en)
            cur.execute(query)
            cn.commit()
            
        if ans==4:
            esal=input("Enter New Salary:")
            query="update emp set salary='"+esal+"' where empno="+str(en)
            cur.execute(query)
            cn.commit()
        if ans==5:
            edoj=input("Enter New Date of joining:")
            query="update emp set doj='"+edoj+"' where empno="+str(en)
            cur.execute(query)
            cn.commit()
        if ans==6:
            eadd=input("Enter New Address:")
            query="update emp set ='"+eadd+"' where empno="+str(en)
            cur.execute(query)
            cn.commit()
            
        print(" RECORD UPDATED  ")
                
def delEmp():
    global cn,cur
    print("******************************************DELETE EMPLOYEE FORM *******************************************")
    en = int(input("Enter Employee number to delete :"))
    query="select * from emp where empno="+str(en)
    cur.execute(query)
    results = cur.fetchall()
    if cur.rowcount<=0:
        print(" SORRY! NO MATCHING DETAILS AVAILABLE ")
    else:
       
        print("******************************************************************************************************")
        print('%5s'%"EMPNO",'%15s'%'EMP NAME','%12s'%'DEPARTMENT','%10s'%'SALARY','%15s'%'DOJ','%-25s'%'ADDRESS')
        print("******************************************************************************************************")
        for row in results:
            print('%5s' % row[0],'%15s'%row[1],'%12s'%row[2],'%10s'%row[3],'%15s'%row[4],'%-25s'%row[5])
    print("-"*50)
    ans = input("Are you sure to delete ? (y/n)")
    if ans=="y" or ans=="Y":
        query="delete from emp where empno="+str(en)
        cur.execute(query)
        cn.commit()
        print(" RECORD DELETED  ")
def clear():
      for i in range(1,20):
          print()
          
def generateSlip():

    global cn,cur
    print("*********************************SALARY SLIP **************************")
    en = int(input("Enter Employee number to print salary slip :"))
    query="select * from emp where empno="+str(en)
    cur.execute(query)
    results = cur.fetchone()
    if cur.rowcount<=0:
        print(" SORRY! NO MATCHING DETAILS AVAILABLE ")
    else:
        clear()
        print("EMPNO :",results[0]," "*20,"NAME :",results[1])
        print("DEPARTMENT :",results[2])
        print("*"*70)
        s = int(results[3])
        hra = s * 12/100
        da = s * 15/100
        it = 1000
        nps = (s+hra)*10/100
        gross = s +hra+da+nps
        ded = it + nps
        net = gross - ded
        tded=it + nps
        print("%19s"%"EARNING","%27s"%"DEDUCTION")
        print("----------------------------------------------------------------------")
        print("%20s"%"Basic  :"+str(s),"%22s"%"INC. TAX :"+str(it))
        print("%20s"%"HRA    :"+str(hra),"%20s"%"NPS    :"+str(nps))
        print("%20s"%"DA     :"+str(da))
        print("%20s"%"NPS    :"+str(nps))
        print("-"*70)
        print("     GROSS :",gross," NET SALARY :",net,"  TOTAL DED :",tded)
    print("-"*70)
    print("=== PRESS ANY ENTER KEY ===")
    input()
      
while True:
    
    print()
    print()
    print('%79s'%"*** PAYROLL MANAGEMENT PYTHON PROGRAMMING SOFTWARE ***")
    print('%79s'%"--------------------------------------------------------")
    print()
    print()
    print()
    print()
    print()
    print("1. SHOW EMPLOYEE LIST ")
    print("2. ADD NEW EMPLOYEE")
    print("3. SEARCH EMPLOYEE ")
    print("4. EDIT EMPLOYEE ")
    print("5. DELETE EMPLOYEE ")
    print("6. GENERATE PAY SLIP ")
    print("0. EXIT")
    ans = int(input("Enter your choice :"))
    if ans==1:
        showAll()
    elif ans==2:
        addEmp()
    elif ans==3:
        searchEmp()
    elif ans==4:
        editEmp()
    elif ans==5:
        delEmp()
    elif ans==6:
        generateSlip()
    elif ans==0:
        print(" Thank you,Have a good Day")
        cn.close()
        break
