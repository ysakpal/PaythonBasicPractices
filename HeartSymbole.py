for row in range(6):
    for cols in range(7):
        if (row == 0 and cols % 3 != 0) or (row == 1 and cols % 3 == 0) or ( row - cols == 2) or (row + cols == 8):
            print("*" ,end=" ")
        else:
            print(end=" ")
    print()


"""
 * *  * *  
*   *   * 
*      * 
 *    *  
  *  *   
   *    
"""