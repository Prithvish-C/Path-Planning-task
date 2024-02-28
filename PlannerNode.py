import sys
from queue import PriorityQueue
from MapNode import MapNode
from MapClass import Map

class PlannerNode:
    def __init__(self):
        self.current_obj=MapNode()
        
        # Since we know that the first step the bot will take will be down, we can simply do it here
        self.current_obj.direction_callback("down")  # example 1
        self.wall_callback()
        

    def wall_callback(self):
        # current_obj has all the attributes to help you in in your path planning !
                
        # Your code goes here. You need to figure out an algorithm to decide on the best direction of movement of the bot based on the data you have.
        # after deciding on the direction, you need to call the direction_callback() function as done in example 1.

        width=self.current_obj.walls.width
        height=self.current_obj.walls.height
        start=(1,0)
        end=self.current_obj.walls.end
        
        grid=[]
        for i in range(width):
            for j in range(height):
                grid.append((i,j))
        
        g_score={cell:float('inf') for cell in grid}
        g_score[start]=0
        f_score={cell:float('inf') for cell in grid}        
        f_score[start]= self.h(start,end)
        
        open=PriorityQueue()
        open.put(self.h(start,end), self.h(start,end), start)
        
        while not open.empty:
            currCell=start
            if currCell==end:
                break

            list=[] #stores tuple data containing movement and corresponding child cell

            if self.check_top_wall(currCell)==True:
                childCell = (currCell[0]-1,currCell[1])
                temp_g_score = g_score[currCell]+1
                temp_f_score = temp_g_score + self.h(childCell,end)
                open.put(temp_f_score, self.h(childCell,end), childCell)
                list.append(("up", childCell))

            if self.check_bottom_wall(currCell)==True:
                childCell = (currCell[0]+1,currCell[1])
                temp_g_score = g_score[currCell]+1
                temp_f_score = temp_g_score + self.h(childCell,end)
                open.put(temp_f_score, self.h(childCell,end), childCell)
                list.append(("down", childCell))

            if self.check_left_wall(currCell)==True:
                childCell = (currCell[0],currCell[1]-1)
                temp_g_score = g_score[currCell]+1
                temp_f_score = temp_g_score + self.h(childCell,end)
                open.put(temp_f_score, self.h(childCell,end), childCell)
                list.append(("left", childCell))

            if self.check_right_wall(currCell)==True:
                childCell = (currCell[0],currCell[1]+1)
                temp_g_score = g_score[currCell]+1
                temp_f_score = temp_g_score + self.h(childCell,end)
                open.put(temp_f_score, self.h(childCell,end), childCell)
                list.append(("right", childCell))


            self.current_obj.direction_callback("up")

            currCell=open.get()[2]

            for tup in list:
                if tup[1]==currCell:
                    move=tup[0]

            if move=="up":
                self.current_obj.direction_callback("up")
            elif move=="down":
                self.current_obj.direction_callback("down")
            elif move=="right":
                self.current_obj.direction_callback("right")
            else:
                self.current_obj.direction_callback("left")


        
        
    def h(self, cell1, cell2):

        x1,y1=cell1
        x2,y2=cell2

        return abs(x1-x2) + abs(y1-y2)


if __name__ == '__main__':
    start_obj=PlannerNode()
    start_obj.current_obj.print_root.mainloop()
 