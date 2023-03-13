import subprocess

lam = 139
x = []

def loopFtuple(a,c,b_hash1,b_hash2):
    for i in range(len(a)):
        print("{:.2%}".format(i/len(a)), end='\r')

        for j in range(len(c)):
            b_val1 = lam - a[i][0] - c[j][0]
            b_val2 = lam - a[i][1] - c[j][1]
            if b_hash1[b_val1]!="" and b_hash2[b_val2]!="":
                x.append((i,j,b_val1,b_val2))
    print("\n")
    return x
        

def get_column(column):
    column_num = str(column)
    commandB = "awk '{print $" + column_num +"}' B_round1.txt"
    outputB= subprocess.check_output(commandB, shell=True)
    outputB = outputB.decode('utf-8').splitlines()
    outputB=[int(i) for i in outputB]

    return outputB

    
def read_first_two_cols(filename):
    with open(filename, 'r') as file:
        cols = []
        for line in file:
            split_line = line.split()
            cols.append((int(split_line[0]), int(split_line[1])))
        return cols


def hash_col(column):
    B_col = get_column(column)
    max_value = max(B_col)
    b_hash = ['' for i in range(1000)]
    counterB = 0

    for i in range(1,len(B_col)):
        value = B_col[i]
        if b_hash[value] == "":
            b_hash[value] = b_hash[value] + str(counterB)
            counterB += 1
        else:
            b_hash[value] = b_hash[value] + "," + str(counterB)
            counterB += 1


    return b_hash


def compare_b_hashes(x,b_hash1,b_hash2):
    a_final_set=set()
    c_final_set=set()
    b_final_set=set()

    counter=0
    for x_value in x:
        print("{:.2%}".format(counter/len(x)), end='\r')
        counter+=1
        b_val1 = x_value[2]
        b_val2 = x_value[3]

        b_val1_set = set(b_hash1[b_val1].split(','))
        b_val2_set = set(b_hash2[b_val2].split(','))
        intersect = b_val1_set.intersection(b_val2_set)
        if len(intersect)>0:
            if x_value[0] in a_final_set:
                continue
            else:
                a_final_set.add(x_value[0])
            
            if x_value[1] in c_final_set:
                continue
            else:
                c_final_set.add(x_value[1])
            
            b_final_set.update(intersect)
    print("\n")

    return a_final_set,b_final_set,c_final_set
            

def main():
    a_cols = read_first_two_cols('A_round1.txt')
    c_cols = read_first_two_cols('C_round1.txt')
    b_hash1 = hash_col('1')
    b_hash2 = hash_col('2')
    x=loopFtuple(a_cols,c_cols,b_hash1,b_hash2)
    a_final,b_final,c_final=compare_b_hashes(x,b_hash1,b_hash2)
    print(len(a_final))
    print(b_final)
    print(len(c_final))


    return

main()
