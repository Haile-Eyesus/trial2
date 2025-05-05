# This is a function without using numpy
def cross_product(array1, array2):
    # This is going to be the list of the sub-functions that i need in this function
    
    # Sub-function to access the column of a given array
    def col(array, n):
        column = []
        for elt in array:
            column.append(elt[n])
    
        return column
    
    # Sub-function to acces the row of a given array
    def row(array, n):
        return(array[n])
    
    # Sub-function for vector product
    def vectorP(vector1, vector2):
        product = 0
        for index in range(len(vector1)):
            product += vector1[index] * vector2[index]
        return product
    
    # This is going to be the main loop

    if len(array1[0]) != len(array2):
        return "These can not be multiplied"
    else:
        finalArray = []
        for r in range(len(array1)):
            inner = []
            for c in range(len(array2[0])):
                inner.append(vectorP(row(array1, r), col(array2, c)))
            finalArray.append(inner)
                
    return finalArray

# But just use numpy
