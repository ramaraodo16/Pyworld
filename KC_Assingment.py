import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.ticker as mticker
import matplotlib.pyplot as plt
from datetime import datetime
import colorama
from colorama import Fore
import time

plt.ion()
while True:
    try:
        print("Menu \n"+ Fore.GREEN+" 1 for Blinker\n 2 for Random\n 3 for Glider Gun\n 4 for Two Heavyweight Spaceships escorting unstable object"+Fore.RESET)
        option = int(input("Enter an option to select: "))

        if option == 1:
            print(" You selected Blinker")
            break
        elif option == 2:
            print("You selected Random")
            break
        elif option == 3:
            print("You selected 'Glider Gun'")
            break
        elif option==4:
            print("You selected '4'")
            break
        else:
            print(Fore.RED+ "Enter a valid option"+Fore.RESET)
    except ValueError:
        print(Fore.RED+ "Invalid input"+Fore.RESET)

while True:
    try:
        dim= int(input("Enter the size of the grid greater than 50 (NXN) :"))
        if dim >= 50:
            print(" Your grid size is", dim)
            break
        else:
            print(Fore.RED+ "Please enter a grid size greater than 50"+Fore.RESET)
            continue
    except ValueError:
        print(Fore.RED+ "Invalid input"+Fore.RESET)

while True:
    try:
        sml=int(input("Enter number of simulations: "))
        # if sml<0:
        #     print(Fore.RED+ "Enter a value of simulations greater than one"+Fore.RESET)
        #     continue
        # else:
        print(" Number of simulations are ", sml)
        break
    except ValueError:
        print(Fore.RED+"Invalid input"+Fore.RESET)

def step(board):
    N = (board[0:-2, 0:-2] + board[0:-2, 1:-1] + board[0:-2, 2:] +
         board[1:-1, 0:-2] + board[1:-1, 2:] +
         board[2:, 0:-2] + board[2:, 1:-1] + board[2:, 2:])
    birth = (N == 3) & (board[1:-1, 1:-1] == 0)
    survive = ((N == 2) | (N == 3)) & (board[1:-1, 1:-1] == 1)
    board[...] = 0
    board[1:-1, 1:-1][birth | survive] = 1
    return board

def grid(option, dim, sml):
    if option == 2:
        a = np.zeros((dim, dim), dtype=bool)
        r = np.random.random((10, 20))

        a[10:20, 10:30] = (r > 0.75)
        board = a.astype(int)
        scatter_plot(board, dim, sml)

    if option == 1:
        board = np.zeros((dim, dim), dtype=bool)
        board = board.astype(int)
        for j in range(3, dim-2, 5):
            for i in range(2, dim-1, 5):
                if i+4 <= dim:
                    board[j][i] = 1
                    board[j][i+1] = 1
                    board[j][i+2] = 1

        scatter_plot(board,dim, sml)

    if option == 3:
        board = np.zeros((dim, dim), dtype=bool)
        board = board.astype(int)
        coordinates = [(10, 5), (11, 5)(10,6),(11,6),(10,15),(11,15),(12,15),(9,16),(13,16),(8,17),(8,18),
              (14,17),(14,18),(11,19),(9,20),(13,20),(10,21),(11,21),(12,21),(11,22),(8,25),(9,25),(10,25),(8,26),
              (9,26),(10,26),(11,27),(7,27),(6,29),(7,29),(11,29),(12,29),(8,39),(9,39),(8,40),(9,40)]

        for g in coordinates:
            board[g[0]][g[1]] = 1

        scatter_plot(board, dim, sml)
    if option ==4:
            board = np.zeros((dim,dim),dtype=bool)
            board = board.astype(int)

            half = int(dim/2)
            coordinates = [(half-4, half-1), (half-4, half), (half-4, half+1), (half-4, half+2), (half-4, half+3), (half-4, half+4), (half-5, half-1), (half-5, half+5), (half-6, half-1),
                  (half-7, half), (half-7, half+5), (half-8, half+2), (half-8, half+3),
                  (half, half-3), (half, half-2),
                  (half+1, half-4), (half+1, half-3),(half+1, half-1), (half+1, half), (half+1, half+1), (half+1, half+2), (half+1, half+3), (half+1, half+4), (half+1, half+5),
                  (half+2, half-3), (half+2, half-2), (half+2, half-1), (half+2, half), (half+2, half+1), (half+2, half+2), (half+2, half+3), (half+2, half+4),
                  (half+3, half-2), (half+3, half-1), (half+3, half), (half+3, half+1), (half+3, half+2), (half+3, half+3),
                  (half+5, half+2), (half+5, half+3), (half+6,half), (half+6,half+5), (half+7, half-1), (half+8, half-1), (half+8, half+5),
                  (half+9, half-1), (half+9, half), (half+9, half+1), (half+9, half+2), (half+9, half+3), (half+9, half+4)]
            for g in coordinates:
                board[g[0]][g[1]] = 1

            scatter_plot(board, dim, sml)

def scatter_plot(board, dim, sml):
    a, b = np.meshgrid(np.arange(board.shape[1]) + .5, np.arange(board.shape[0]) + .5)

    fig, axes = plt.subplots(1, 1, figsize=(15, 9),
                             tight_layout=True)

    axes.grid(True, color="b")
    axes.xaxis.set_major_locator(mticker.MultipleLocator())
    axes.yaxis.set_major_locator(mticker.MultipleLocator())
    axes.tick_params(size=0, length=0, labelleft=False, labelbottom=False)
    axes.set(xlim=(0, board.shape[1]), ylim=(board.shape[0], 0),
              aspect="equal")

    plt_u = axes.scatter(a[board == 1],
                           b[board ==1], c='0.1',
                           marker='s')

    plt.show()
    start_datetime = datetime.now()
    print("the start time is ",start_datetime)

    # initial = board
    last = board
    count = 0
    living_cells = np.count_nonzero(board==1)
    for t in range(1, sml):
        new_board = step(board)
        if (last==new_board).all():
            count +=1
        if count > 2:
            new_board = board
        last = new_board
        living_cells += np.count_nonzero(new_board==1)
        a, b = np.meshgrid(np.arange(new_board.shape[1]) + .5, np.arange(new_board.shape[0]) + .5)
        update_plot(plt_u, a, b, new_board)
        fig.canvas.draw_idle()
        fig.canvas.draw()
        fig.canvas.flush_events()
        time.sleep(0.00001)

    end_datetime = datetime.now()
    print("The end time is ",end_datetime)
    time_diff = (end_datetime - start_datetime)
    execution_time = time_diff.total_seconds() * 1000
    print("Number of milliseconds:", execution_time)

    print("Total number of living cells during processing", living_cells)
    plt.waitforbuttonpress()

def update_plot(plt_u, a, b, grid):
    plt_u.set_offsets(np.c_[a[grid > 0], b[grid > 0]])
grid(option,dim,sml)