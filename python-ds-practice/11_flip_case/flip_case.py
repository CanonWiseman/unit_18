def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    flip_lst = list(phrase)
    flipped_str = ""

    for char in flip_lst:
        if char == to_swap or char == to_swap.swapcase():
            flipped_str += char.swapcase()
        
        else:
            flipped_str += char
    
    return str(flipped_str)

    