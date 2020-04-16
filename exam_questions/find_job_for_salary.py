la = 100000
lb = 1000000000

lines = []

global line_count
line_count = 0
global sl
sl = set()
while True and len(lines) <= la+2:# 
    line = input()#"Pls input:\n"
    
    # print(line)
    # print(line_count)
    if line:# line is a string with space
        line_count += 1
        int_line = line.split(' ')
        lines.append(int_line)
        num_job = int(lines[0][0])
        num_people = int(lines[0][1])
        # print(num_job, num_people)
        # print(line)
        if line_count!= 1 and line_count != num_job + 2:
            sl.add(int_line[1])

        if line_count == num_job +2 and len(int_line) == num_people:
            break


    else:
        continue
        
if len(sl) != int(lines[0][0]):
    # print(sl, len(sl))
    # print("same salary error")
    exit(0)

num_job = int(lines[0][0])
num_people = int(lines[0][1])

if num_job > la or num_people > la:
    exit(0)

workDB = lines[1:-1]
high_salary = []
n_job = len(lines) - 2
n_people = len(lines[-1])
abilities = lines[-1]

# print(lines)
# print("____________")


for i in range(n_people):
    job_tmp = []
    Ai = int(abilities[i])
    if Ai > lb:
        break
    for j in range(n_job):
        Di = int(workDB[j][0])
        Pi = int(workDB[j][1])
        if Di > lb or Pi > lb:
            break
        if Ai >= Di:
            job_tmp.append(j)
    max_salary = 0
    for k in job_tmp:
        # print(k)
        salary_tmp = int(workDB[k][1])
        if salary_tmp > max_salary:
            max_salary = salary_tmp
    if max_salary != 0:
        high_salary.append(max_salary)
    # print(max_salary)
if len(high_salary) == n_people:
    for h in high_salary:
        print(h)
