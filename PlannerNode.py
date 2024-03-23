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
        open.put((self.h(start,end), self.h(start,end), start))

        currCell=start

        self.obj=Map(width,height,start,end)
              
        while not open.empty():
            
            if currCell==end:
                break
            
            
            if self.obj.check_top_wall(currCell)==False:
                childCell = (currCell[0]-1,currCell[1])
                temp_g_score = g_score[currCell]+1
                temp_f_score = temp_g_score + self.h(childCell,end)

                if temp_f_score<f_score[childCell]:
                    g_score[childCell]=temp_g_score
                    f_score[childCell]=temp_f_score   
                    open.put((temp_f_score, self.h(childCell,end), childCell))
                    
            if self.obj.check_bottom_wall(currCell)==False:
                childCell = (currCell[0]+1,currCell[1])
                temp_g_score = g_score[currCell]+1
                temp_f_score = temp_g_score + self.h(childCell,end)

                if temp_f_score<f_score[childCell]:
                    g_score[childCell]=temp_g_score
                    f_score[childCell]=temp_f_score   
                    open.put((temp_f_score, self.h(childCell,end), childCell))
                    
            if self.obj.check_left_wall(currCell)==False:
                childCell = (currCell[0],currCell[1]-1)
                temp_g_score = g_score[currCell]+1
                temp_f_score = temp_g_score + self.h(childCell,end)

                if temp_f_score<f_score[childCell]:
                    g_score[childCell]=temp_g_score
                    f_score[childCell]=temp_f_score   
                    open.put((temp_f_score, self.h(childCell,end), childCell))      

            if self.obj.check_right_wall(currCell)==False:
                childCell = (currCell[0],currCell[1]+1)
                temp_g_score = g_score[currCell]+1
                temp_f_score = temp_g_score + self.h(childCell,end)

                if temp_f_score<f_score[childCell]:
                    g_score[childCell]=temp_g_score
                    f_score[childCell]=temp_f_score   
                    open.put((temp_f_score, self.h(childCell,end), childCell))
                    

            prevCell=currCell
            currCell=open.get()[2]
                        
            if currCell[0]<prevCell[0]:
                self.current_obj.direction_callback("up")
            elif currCell[0]>prevCell[0]:
                self.current_obj.direction_callback("down")
            elif currCell[1]>prevCell[1]:
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
 