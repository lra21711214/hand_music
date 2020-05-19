def finger(landmark):
    x = 0
    y = 1
    thumbFinger = False
    firstFinger = False
    secondFinger = False
    thirdFinger = False
    fourthFinger = False

    if landmark[9][y] < landmark[0][y]:
        Hand_direction_y = 'up'
    else:
        Hand_direction_y = 'down'

    landmark_point = landmark[2][x]
    if landmark[5][x] < landmark[17][x]:
        if landmark[3][x] < landmark_point and landmark[4][x] < landmark_point:
            thumbFinger = True
        Hand_direction_x = 'right'
    else:
        if landmark[3][x] > landmark_point and landmark[4][x] > landmark_point:
            thumbFinger = True
        Hand_direction_x = 'left'

    landmark_point = landmark[6][y]
    if landmark[7][y] < landmark_point and landmark[8][y] < landmark_point:
        firstFinger = True

    landmark_point = landmark[10][y]
    if landmark[11][y] < landmark_point and landmark[12][y] < landmark_point:
        secondFinger = True

    landmark_point = landmark[14][y]
    if landmark[15][y] < landmark_point and landmark[16][y] < landmark_point:
        thirdFinger = True

    landmark_point = landmark[18][y]
    if landmark[19][y] < landmark_point and landmark[20][y] < landmark_point:
        fourthFinger = True

    if thumbFinger and firstFinger and secondFinger and thirdFinger and fourthFinger:
        hand = 'five'
    elif not thumbFinger and firstFinger and secondFinger and thirdFinger and fourthFinger:
        hand = 'four'
    elif not thumbFinger and firstFinger and secondFinger and thirdFinger and not fourthFinger:
        hand = 'tree'
    elif not thumbFinger and firstFinger and secondFinger and not thirdFinger and not fourthFinger:
        hand = 'two'
    elif not thumbFinger and firstFinger and not secondFinger and not thirdFinger and not fourthFinger:
        hand = 'one'
    elif not thumbFinger and not firstFinger and not secondFinger and not thirdFinger and not fourthFinger:
        hand = 'zero'
    elif thumbFinger and not firstFinger and not secondFinger and not thirdFinger and fourthFinger:
        hand = 'aloha'
    elif not thumbFinger and firstFinger and not secondFinger and not thirdFinger and fourthFinger:
        hand = 'fox'
    elif thumbFinger and firstFinger and not secondFinger and not thirdFinger and not fourthFinger:
        hand = 'up'
    elif thumbFinger and firstFinger and not secondFinger and not thirdFinger and fourthFinger:
        hand = 'RankaLee'
    else:
        hand = None

    return hand, Hand_direction_x, Hand_direction_y