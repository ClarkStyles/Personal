import numpy as np

try:

    vector_1 = np.array([])
    print("For your vector 1: ")
    i_element_1 = float(input("Enter your ith element: ").strip())
    j_element_1 = float(input("Enter your jth element: ").strip())
    k_element_1 = float(input("Enter your kth element: ").strip())
    vector_1 = np.append(vector_1 , [i_element_1 , j_element_1 , k_element_1])

    vector_2 = np.array([])
    print("For your vector 2: ")
    i_element_2 = float(input("Enter your ith element: ").strip())
    j_element_2 = float(input("Enter your jth element: ").strip())
    k_element_2 = float(input("Enter your kth element: ").strip())
    vector_2 = np.append(vector_2 , [i_element_2 , j_element_2 , k_element_2])
    
    def vector_sum():
        vector_sum = vector_1 + vector_2
        f = f"{vector_sum[0]}i+{vector_sum[1]}j+{vector_sum[2]}k"
        return f 
    def vector_sub():
        vector_sub = vector_1 - vector_2
        f = f"{vector_sub[0]}i+{vector_sub[1]}j+{vector_sub[2]}k"
        return f
    
    def vector_dot_product():
        vector_dot_product = vector_1 * vector_2
        f = f"{vector_dot_product[0]}i+{vector_dot_product[1]}j+{vector_dot_product[2]}k"
        return f
    
    def vector_cross_product():
        vector_cross_product = np.cross(vector_1 , vector_2)
        f = f"{vector_cross_product[0]}i+{vector_cross_product[1]}j+{vector_cross_product[2]}k"
        return f
    
     
    operation = input(" Enter what you wonna do: sum, sub, dot product, cross product: ")

    match operation:
        case "sum":
            print("Vector 1 + Vector 2: ", vector_sum())
        case "sub":
            print("Vector 1 - Vector 2: ", vector_sub())
        case "dot product":
            print("Vector 1 . Vector 2: ", vector_dot_product())
        case "cross product":
            print("Vector 1 x vector 2: " , vector_cross_product())
        case _:
            print("Invalid operation. Please enter 'sum', 'sub', or 'dot_product'.")
    
    


except:
    print("Invalid operation! \n"
          "Please enter a number")