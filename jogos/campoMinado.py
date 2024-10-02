import random
import re
class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        self.board = self.novo_tabuleiro()
        self.valores_para_tabuleiro()
        self.dug = set()


    def valores_para_tabuleiro(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == "*":
                    continue
                self.board[r][c] = self.localizar_bombas_ao_redor(r,c)


    def localizar_bombas_ao_redor(self, row, col):
        bombas_ao_redor = 0
        for r in range(max(0,row+1), min(self.dim_size-1,row+1)+1):
            for c in range(max(0,col-1), min(self.dim_size-1,col+1)+1):
                if r== row and c == col:
                    continue
                if self.board[r][c] == "*":
                    bombas_ao_redor +=1
        return bombas_ao_redor
    

    def novo_tabuleiro(self):
        board = [[None for _ in range(self.dim_size)]for _ in range(self.dim_size)]
        bombs_plant = 0
        while bombs_plant < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 -1)
            row = loc // self.dim_size
            col = loc% self.dim_size
            if board[row][col] == "*":
                continue
            board[row][col] =  "*"
            bombs_plant +=1
        return board
    


    def dig(self, row, col):
        self.dug.add((row,col))
        if self.board[row][col] =="*":
            return False
        elif self.board[row][col] >0:
            return True
        for r in range(max(0,row+1), min(self.dim_size-1,row+1)+1):
            for c in range(max(0,col-1), min(self.dim_size-1,col+1)+1):
                if(r,c) in self.dug:
                    continue
                self.dig(r,c)
        return True
    def __str__(self):
        #return sting that shows the board to the player
        visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = " "
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key=len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'

        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-' * str_len + '\n' + string_rep + '-' * str_len

        return string_rep


safe = True
def jogar(dim_size = 10, num_bombs=10):
    board = Board(dim_size, num_bombs)
    while len(board.dug)<board.dim_size **2 - num_bombs:
        print(board)
        user_input = input("Onde voce vai mergulhar, linha, coluna ")
        row, col = int(user_input[0]), int(user_input[-1])
        if row<0 or row>= board.dim_size or col<0 or col>=dim_size:
            print("localidade invalida")
            continue
        safe = board.dig(row,col)
        if not safe:
            break
    if safe:
        print("Parabens!!, voce ganhou")
    else:
        print("Voce perdeu")
        board.dug = [(r,c)for r in range(board.dim_size)for c in range(board.dim_size)]
        print(board)
