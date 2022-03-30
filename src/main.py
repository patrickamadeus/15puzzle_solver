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

root_cost = getCost(m)
if isSolvable(m):
    i = 1
    while not isSolution(m):
        print("TURN %d" % i)
        # time.sleep(1)
        while_counter += 1

        x,y = koordinat(m,0)
        for dirs in moveType(x,y):
            nm = dc(m)
            nm = move(nm, x, y, dirs)

            # -- enqueue valid problem for every direction, with its root cost -- #
            if isSolvable(nm):
                pq.enqueue(nm, getCost(nm) + root_cost)
                # print(getCost(nm) , root_cost)

        # -- dequeue the least cost matrix -- #
        # print(pq)
        root_cost,m = pq.dequeue()
        printMatrix(m)
        i+=1

    end = dt.now()
    print("Total Turn Needed to Solve : %d" % while_counter)
    print("RUNTIME: %.5f" % (float((end-start).total_seconds()) - 0) )
else:
    print("THIS PROBLEM IS NOT SOLVABLE")
