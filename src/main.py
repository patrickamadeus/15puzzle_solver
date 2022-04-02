from src import *

# ========= FILENAME VALIDATION SECTION ========= #
filename = input("Enter your filename (with extension): ")

path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'test'))
# validate filename
while filename not in os.listdir(path):
    print("File not found!")
    filename = input("Enter your filename (with extension): ")


m = readFile(path+'\\'+filename)



# ========== MAIN PROGRAM SECTION ========== #


if isSolvable2(m):
    nodes = 0
    routes = {str(m) : ('root',None)}
    root_cost = getCost(m)

    # Init heap
    l = [(root_cost,m)]
    hq.heapify(l)


    # ============= SOLUTION FINDING SECTION ============= #
    # begin timer
    start = dt.now()
    while not isSolution(m):
        x,y = koordinat(m,0)
        for dirs in moveType(x,y):
            nm = dc(m)
            nm = move(nm, x, y, dirs)

            # enqueue new problem for direction dirs, with its cost consist of sum of current cost and root
            if str(nm) not in routes:
                hq.heappush(l, (getCost(nm) + root_cost, nm))
                nodes += 1
                routes[str(nm)] = (m,dirs)

        # get the least cost puzzle 
        root_cost,m = hq.heappop(l)
    
    end = dt.now()
    # end timer


    # Gather and print the solved path
    result = gatherSolvedPath(m,routes)
    printSolvedPath(result)


    # Information about the solution
    print("Total Node(s) Needed to Solve : %d" % nodes)
    print("ALGORITHM RUNTIME: %.5f s" % (float((end-start).total_seconds())) )
else:
    print("THIS PROBLEM IS NOT SOLVABLE")
