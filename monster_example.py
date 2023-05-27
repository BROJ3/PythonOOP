import random

class Monster():
    def __init__ (self,n_rows,n_cols,max_speed):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.max_speed = max_speed

        self.my_row = random.randrange(self.n_rows)
        self.my_col = random.randrange(self.n_cols)
        self.my_speed_x = random.randrange(-max_speed,max_speed+1)

        #chooses an X speed
        self.my_speed_y = random.randrange(-max_speed,max_speed+1)

        def move(self):
            self.my_row = (self.my_row + self.my_speed_y) % self.n_rows
            self.my_col = (self.my_col + self.my_speed_x) % self.n_cols

        
N_MONSTERS = 20
N_ROWS = 100    #Could be any size
N_COLS = 200    #Could be any size
MAX_SPEED = 4
monster_list=[]
for i in range(N_MONSTERS):
    o_monster=Monster(N_ROWS,N_COLS,MAX_SPEED)
    monster_list.append(o_monster)


