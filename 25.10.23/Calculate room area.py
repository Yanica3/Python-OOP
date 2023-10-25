def calcilate_room_area(room_widhth, room_height):
    print(f"The result of the operation is:{room_widhth*room_height}")
    if room_widhth*room_height<140:
        return "The area of the room is below 140..."
    else:
        return "The area of the room is 140 or more"

result=calcilate_room_area(50,10)
print(f"The result of the function is: {result}")
