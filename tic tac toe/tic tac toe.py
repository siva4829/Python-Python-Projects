import random as rd
import time as tm

arr = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]
myTup = (0, 1, 2)


def game(a, b, arr, y):
    if not arr[a][b]:
        arr[a][b] = y
        display()
        return True
    else:
        tm.sleep(1)
        print("That cell is already taken")


def display():
    print("\n")
    for i in range(3):
        print("\t", " |".join(f"{cell or '':^3}" for cell in arr[i]))
        if i < 2:
            print("\t", "  ___________")
    print("\n")


def ai_assist():
    for i in range(3):
        if arr[i][0] == arr[i][1] == arr[i][2] != "":
            return f"{arr[i][0].upper()} is winner"
        if arr[0][i] == arr[1][i] == arr[2][i] != "":
            return f"{arr[0][i].upper()} is winner"
    if arr[0][0] == arr[1][1] == arr[2][2] != "":
        return f"{arr[1][1].upper()} is winner"
    if arr[0][2] == arr[1][1] == arr[2][0] != "":
        return f"{arr[1][1].upper()} is winner"
    if all(arr[i][j] != "" for i in range(3) for j in range(3)):
        return "Draw"

    return False


def decide_winner():
    for i in range(3):
        if arr[i][0] == arr[i][1] == arr[i][2] != "":
            print(f"{arr[i][0].upper()} is winner")
            usr_decide()
            return True
        if arr[0][i] == arr[1][i] == arr[2][i] != "":
            print(f"{arr[0][i].upper()} is winner")
            usr_decide()
            return True
    if arr[0][0] == arr[1][1] == arr[2][2] != "":
        print(f"{arr[1][1].upper()} is winner")
        usr_decide()
        return True
    if arr[0][2] == arr[1][1] == arr[2][0] != "":
        print(f"{arr[1][1].upper()} is winner")
        usr_decide()
        return True
    if all(arr[i][j] != "" for i in range(3) for j in range(3)):
        print("Draw")
        usr_decide()
        return True

    return False


def usr_decide():
    try:
        tm.sleep(1)
        x = input("Do you want to play again(Y/N):").strip()
        x = x.upper()
        if x == "Y" or x == "YES":
            arr[:] = [["", "", ""], ["", "", ""], ["", "", ""]]
        else:
            exit(1)
    except Exception as e:
        tm.sleep(1)
        print("Enter input only in string not other data type")


def rand_choose():
    return rd.choice(myTup)


def ai_predict(arr, a, b, y):

    for i in range(3):
        for j in range(3):
            if "" == arr[i][j]:
                arr[i][j] = 'o'
                if ai_assist() == "O is winner":
                    arr[i][j] = 'o'
                    display()
                    return
                arr[i][j] = ''

    for i in range(3):
        for j in range(3):
            if "" == arr[i][j]:
                arr[i][j] = 'x'
                if ai_assist() == "X is winner":
                    arr[i][j] = 'o'
                    display()
                    return
                arr[i][j] = ''

    if arr[a][b] == "":
        player(a, b, y)
        return


def player(a, b, y):
    if 0 <= a <= 2 and 0 <= b <= 2:
        y = y.lower()
        game(a, b, arr, y)
    else:
        tm.sleep(1)
        print("Enter the valid row or column")


try:
    print("Welcome to tic tac toe")
    while True:
        tm.sleep(1)
        print("1.opponent as computer")
        print("2.opponent as your friend")
        print("3.exit")
        tm.sleep(1)
        x = int(input("Enter your input:"))
        if x == 1:
            display()
            tm.sleep(1)
            print("Player 1 only allowed 'x' ")
            print("Computer only allowed 'o' ")
            try:
                while True:
                    print("\nPlayer 1")
                    a = int(input("Enter the row:"))
                    b = int(input("Enter the column:"))
                    y = 'x'
                    while True:
                        if not arr[a][b]:
                            player(a, b, y)
                            break
                        else:
                            a = int(input("Enter the row:"))
                            b = int(input("Enter the column:"))

                    if decide_winner():
                        break
                    print("\ncomputer")
                    a = rand_choose()
                    b = rand_choose()
                    y = 'o'
                    ai_predict(arr, a, b, y)

                    if decide_winner():
                        break
            except Exception as e:
                print(f" Error:{e}")
        elif x == 2:
            arr[:] = [["", "", ""], ["", "", ""], ["", "", ""]]
            tm.sleep(1)
            print("Player 1 only allowed 'x' ")
            print("Player 2 only allowed 'o' ")

            try:
                while True:
                    # === PLAYER 1 TURN ===
                    print("\nPlayer 1 (x)")
                    while True:
                        try:
                            a = int(input("Enter the row (0-2): "))
                            b = int(input("Enter the column (0-2): "))
                            if 0 <= a <= 2 and 0 <= b <= 2 and arr[a][b] == "":
                                player(a, b, 'x')
                                break
                            else:
                                print("Invalid or taken cell. Try again.")
                        except:
                            print("Please enter valid integers (0-2).")

                    if decide_winner():
                        break

                    # === PLAYER 2 TURN ===
                    print("\nPlayer 2 (o)")
                    while True:
                        try:
                            c = int(input("Enter the row (0-2): "))
                            d = int(input("Enter the column (0-2): "))
                            if 0 <= c <= 2 and 0 <= d <= 2 and arr[c][d] == "":
                                player(c, d, 'o')
                                break
                            else:
                                print("Invalid or taken cell. Try again.")
                        except:
                            print("Please enter valid integers (0-2).")

                    if decide_winner():
                        break

            except Exception as e:
                print(f"Error: {e}")

        elif x == 3:
            tm.sleep(1)
            print("Exiting program...")
            exit(0)
        else:
            print("Valid input")

except Exception as e:
    print(f"Error:{e}")

finally:
    print("The game was completed successfully")
