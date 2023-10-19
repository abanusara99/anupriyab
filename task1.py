def find_seat_type(seat_num):
    # Define seat types
    seat_types = ["WS", "MS", "AS", "AS", "MS", "WS"]
    
    # Calculate the facing seat
    row = (seat_num - 1) // 12  # Find the row number
    opposite_seat = 12 * row + (13 - (seat_num % 12))

    # Calculate the seat type
    seat_type = seat_types[seat_num % 6]

    return opposite_seat, seat_type

# Main function
if __name__ == "__main__":
    T = int(input(" "))

    for _ in range(T):
        N = int(input(" "))
        opposite_seat, seat_type = find_seat_type(N)
        print(f"{opposite_seat} {seat_type}")
