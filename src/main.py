from src import *

### ========= MAIN PROGRAM ========= ###

filename = input("Enter your filename (with extension): ")

path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'test'))
# validate filename
while filename not in os.listdir(path):
    print("File not found!")
    filename = input("Enter your filename (with extension): ")


m = readFile(path+'\\'+filename)
printMatrix(m)

while_counter = 0


start = dt.now()

pq = PriorityQueue()


if isValidProblem(m):
    i = 1
    while not isSolution(m):
        print("TURN %d" % i)
        time.sleep(1)
        while_counter += 1

        min_matrix = None
        min_cost = 16

        x,y = koordinat(m,0)
        chosen_dir = ""
        for dirs in moveType(x,y):
            nm = dc(m)
            nm = move(nm, x, y, dirs)

            if isValidProblem(nm):
                cost = getCost(nm)
                if cost < min_cost:
                    min_matrix = nm
                    min_cost = cost
                    chosen_dir = dirs

        m = min_matrix
        print("MOVING %s" % chosen_dir)
        printMatrix(m)
        i+=1

    end = dt.now()
    print("Total Turn Needed to Solve : %d" % while_counter)
    print("RUNTIME: %.5f" % (float((end-start).total_seconds()) - while_counter) )
else:
    print("THIS PROBLEM IS NOT SOLVABLE")
