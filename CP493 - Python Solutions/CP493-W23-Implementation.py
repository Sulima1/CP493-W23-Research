import subprocess
lam=139




def get_coloumn(coloumn):

    column_num = str(coloumn)
    commandA = "awk '{print $" + column_num +"}' A.txt"
    outputA = subprocess.check_output(commandA, shell=True)
    outputA = outputA.decode('utf-8').splitlines()

    commandB = "awk '{print $" + column_num +"}' B.txt"
    outputB= subprocess.check_output(commandB, shell=True)
    outputB = outputB.decode('utf-8').splitlines()

    commandC = "awk '{print $" + column_num +"}' C.txt"
    outputC = subprocess.check_output(commandC, shell=True)
    outputC = outputC.decode('utf-8').splitlines()

    outputA=[int(i) for i in outputA]
    outputB=[int(i) for i in outputB]
    outputC=[int(i) for i in outputC]

    outputA=[i for i in outputA]
    outputB=[i for i in outputB]
    outputC=[i for i in outputC]



    return outputA, outputB, outputC

def hash_first_set(coloumn):
    A_col,B_col,C_col=get_coloumn(coloumn) 
    a_hash=['' for i in range(1000)]
    b_hash=['' for i in range(1000)]
    c_hash=['' for i in range(1000)]
    counterA=0
    counterB=0
    counterC=0

    for i in range(len(A_col)):
        value=A_col[i]

        if a_hash[value]== "":
            a_hash[value]=a_hash[value]+str(counterA)
            counterA+=1
        else:
            a_hash[value]=a_hash[value]+","+str(counterA)
            counterA+=1

    for i in range(len(B_col)):
        value=B_col[i]
        if b_hash[value]== "":
            b_hash[value]=b_hash[value]+str(counterB)
            counterB+=1
        else:
            b_hash[value]=b_hash[value]+","+str(counterB)
            counterB+=1


    for i in range(len(C_col)):
        value=C_col[i]
        if c_hash[value]== "":
            c_hash[value]=c_hash[value]+str(counterC)
            counterC+=1
        else:
            c_hash[value]=c_hash[value]+","+str(counterC)
            counterC+=1
        
        
    x=0
    for i in range(len(b_hash)):
        temp=b_hash[int(i)].split(",")
        x+=len(temp)

    return a_hash,b_hash,c_hash

def hash_with_constraints(coloumn,a_constraint,b_constraint,c_constraint):
    A_col,B_col,C_col=get_coloumn(coloumn) 
    a_hash=['' for i in range(1000)]
    b_hash=['' for i in range(1000)]
    c_hash=['' for i in range(1000)]
    counterA=0
    counterB=0
    counterC=0
    tester=0

    for i in A_col:
        if counterA in a_constraint:
            value=A_col[counterA]
        
            if a_hash[value]== "":
                a_hash[value]=a_hash[value]+str(counterA)
                counterA+=1
            else:
                a_hash[value]=a_hash[value]+","+str(counterA)
                counterA+=1
        else:
            counterA+=1

    for i in B_col:
        if counterB in b_constraint:
            value=B_col[counterB]
            if b_hash[value]== "":
                b_hash[value]=b_hash[value]+str(counterB)
                counterB+=1
            else:
                b_hash[value]=b_hash[value]+","+str(counterB)
                counterB+=1
        else:
            counterB+=1

    for i in C_col:
        if counterC in c_constraint:
            tester+=1
            value=C_col[counterC]
            if c_hash[value]== "":
                c_hash[value]=c_hash[value]+str(counterC)
                counterC+=1
            else:
                c_hash[value]=c_hash[value]+","+str(counterC)
                counterC+=1
        else:
            counterC+=1

        


    return a_hash,b_hash,c_hash


def check_potential_paths(a_hash,b_hash,c_hash):
    potential_array=[]
    faila=[]
    failc=set()

    for i in range(len(a_hash)):
        if a_hash[i]=='':
            faila.append(i)
            continue

        for j in range(len(c_hash)):
            if c_hash[j]=='':
                failc.add(j)
                continue

            b_val=lam-j-i
            if b_hash[b_val]!='':
                potential_array.append((i,b_val,j))
            else:
                continue


    return potential_array

def create_potential_arrays(potentials,a_hash,b_hash,c_hash,given_file):
    
    given_routes=set()
    potentials_list=[]
    potentials_set=set()


    if given_file=="A":
        for i in potentials:
            if i[0] not in given_routes:
                given_routes.add(i[0])
            else:
                continue

        for i in given_routes:
            potentials_list+=a_hash[i].split(",")

        potentials_listarr=[]

        for x in potentials_list:
            if x.isdigit():
                potentials_listarr.append(int(x))
        potentials_listarr.sort()

        for i in potentials_listarr:
            potentials_set.add(i)
        
        return potentials_set
        

    if given_file=="B":
        for i in potentials:
            if i[1] not in given_routes:
                given_routes.add(i[1])
            else:
                continue

        for i in given_routes:
            potentials_list+=b_hash[i].split(",")

        potentials_listarr=[]

        for x in potentials_list:
            if x.isdigit():
                potentials_listarr.append(int(x))
        potentials_listarr.sort()

        for i in potentials_listarr:
            potentials_set.add(i)
        
        return potentials_set
        
    if given_file=="C":
        for i in potentials:
            if i[2] not in given_routes:
                given_routes.add(i[2])
            else:
                continue

        for i in given_routes:
            potentials_list+=c_hash[i].split(",")

        potentials_listarr=[]

        for x in potentials_list:
            if x.isdigit():
                potentials_listarr.append(int(x))
        potentials_listarr.sort()

        for i in potentials_listarr:
            potentials_set.add(i)
        
        return potentials_set
        

    
    return

def first_two_col_checker(col1,col2):
    a_hash,b_hash,c_hash=hash_first_set(col1)
    a2_hash,b2_hash,c2_hash=hash_first_set(col2)
    
    potential_paths=check_potential_paths(a_hash,b_hash,c_hash)
    potential_paths2=check_potential_paths(a2_hash,b2_hash,c2_hash)

    A1=create_potential_arrays(potential_paths,a_hash,b_hash,c_hash,"A")
    A2=create_potential_arrays(potential_paths2,a2_hash,b2_hash,c2_hash,"A")

    B1=create_potential_arrays(potential_paths,a_hash,b_hash,c_hash,"B")
    B2=create_potential_arrays(potential_paths2,a2_hash,b2_hash,c2_hash,"B")

    C1=create_potential_arrays(potential_paths,a_hash,b_hash,c_hash,"C")
    C2=create_potential_arrays(potential_paths2,a2_hash,b2_hash,c2_hash,"C")

    first_col_potential_setA=set()
    first_col_potential_setB=set()
    first_col_potential_setC=set()

    for i in A1:
        if i in A2:
            first_col_potential_setA.add(i)

    for i in B1:
        if i in B2:
            first_col_potential_setB.add(i)

    for i in C1:
        if i in C2:
            first_col_potential_setC.add(i)
            
    return first_col_potential_setA, first_col_potential_setB, first_col_potential_setC

def keep_valid_lines(row_array,filename):
    
    # Open the input file for reading
    with open(filename+".txt", 'r') as input_file:
        # Read all the lines from the input file into a list
        all_lines = input_file.readlines()

    # Define an array of row indices to keep

    # Filter the lines to keep only those with indices in the rows_to_keep array
    filtered_lines = [all_lines[row_index] for row_index in row_array]

    # Open the output file for writing
    with open(filename+"_round1.txt", 'w') as output_file:
        # Write the filtered lines to the output file
        output_file.writelines(filtered_lines)

    return

def main():

    
    col1=1
    col2=2
    # i=0
    # lock=[]
    # while i !=10:
    #     i+=1
    #     a,b,c=first_two_col_checker(col1,col2)
    #     col1+=2
    #     col2+=2
    #     lock.append((len(a),len(b),len(c)))

    a,b,c=first_two_col_checker(col1,col2)




    for i in range(3,38):
        checka,checkb,checkc=hash_with_constraints(i,a,b,c)
        potential_paths=check_potential_paths(checka,checkb,checkc)
        A1=create_potential_arrays(potential_paths,checka,checkb,checkc,"A")
        B1=create_potential_arrays(potential_paths,checka,checkb,checkc,"B")
        C1=create_potential_arrays(potential_paths,checka,checkb,checkc,"C")
        a=A1
        b=B1
        c=C1

        print("===============")
        print(len(A1))
        print(len(B1))
        print(len(C1))
        print("===============")

    # for i in range(3,38):
    #     checka,checkb,checkc=hash_with_constraints(i,a,b,c)
    #     potential_paths=check_potential_paths(checka,checkb,checkc)
    #     A1=create_potential_arrays(potential_paths,checka,checkb,checkc,"A")
    #     B1=create_potential_arrays(potential_paths,checka,checkb,checkc,"B")
    #     C1=create_potential_arrays(potential_paths,checka,checkb,checkc,"C")
    #     a=A1
    #     b=B1
    #     c=C1

    #     print("===============")
    #     print(len(A1))
    #     print(len(B1))
    #     print(len(C1))
    #     print("===============")

    keep_valid_lines(list(A1),"A")
    keep_valid_lines(list(B1),"B")
    keep_valid_lines(list(C1),"C")



    return
main()



