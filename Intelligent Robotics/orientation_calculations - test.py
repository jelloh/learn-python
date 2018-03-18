import math

c = [[1,1],[2,2],[2,3],[3,2]]

old_degree = 0

coordinate_old = c[0]
counter = 0

for coordinate in c:

    if counter + 1 is len(c):
        break

    #print(coordinate, " to ", c[counter+1]) # for testing
    print(coordinate_old, " to ", coordinate)

    # get x and y distances
    '''
    x = math.fabs(c[counter][0] - c[counter + 1][0]) # absolute value
    y = math.fabs(c[counter][1] - c[counter + 1][1]) # absolute value
    '''

    x = math.fabs(coordinate[0] - coordinate_old[0])
    y = math.fabs(coordinate[1] - coordinate_old[1])

    # get the overall distance (the hypotenuse)
    distance = math.sqrt(math.pow(x,2) + math.pow(y,2))

    if not x == 0:
        degree = math.atan(x/y)
    else:
        degree = 90

    change_in_degree = degree - old_degree

    print("Distance: ", distance)
    print ("Degree: ", math.degrees(degree))
    print("Change in degree: ", math.degrees(change_in_degree))

    old_degree = degree
    coordinate_old = c[counter]
    counter = counter + 1
    print("\n")
