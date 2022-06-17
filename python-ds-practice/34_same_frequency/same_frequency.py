def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    is_same = False

    for num in set(str(num1)):
        if str(num1).count(str(num)) == str(num2).count(str(num)):
            is_same = True
        else: 
            is_same = False
    
    return is_same
            