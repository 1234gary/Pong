###PONG AI
###BY: MIKE YIN


count = 0
def counter():
    """Function to be called in the game function
    call pong_ai.counter() to initialize these global variables"""
    global count
    global ballx2
    global bally2
    if count ==0:
        ballx2 = 30
        bally2 = 30
        count += 1
        return 
    count =1
    return 
        

def pong_ai(paddle_frect, other_paddle_frect, ball_frect, table_size):
    '''return "up" or "down", depending on which way the paddle should go to
    align its centre with the centre of the ball, assuming the ball will
    not be moving

    Arguments:
    paddle_frect: a rectangle representing the coordinates of the paddle
                  paddle_frect.pos[0], paddle_frect.pos[1] is the top-left
                  corner of the rectangle.
                  paddle_frect.size[0], paddle_frect.size[1] are the dimensions
                  of the paddle along the x and y axis, respectively

    other_paddle_frect:
                  a rectangle representing the opponent paddle. It is formatted
                  in the same way as paddle_frect
    ball_frect:   a rectangle representing the ball. It is formatted in the
                  same way as paddle_frect
    table_size:   table_size[0], table_size[1] are the dimensions of the table,
                  along the x and the y axis respectively

    The coordinates look as follows:

     0             x
     |------------->
     |
     |
     |
 y   v
    '''

    global ballx0
    global bally0
    global ballx1
    global bally1
    global ballx0
    global ballx2
    global bally2
    global bally0
    global counter
    counter()
    ballx0 = ball_frect.pos[0] - (paddle_frect.size[0]/2) 
    bally0 = ball_frect.pos[1]
    ballx1 = ball_frect.pos[0] - (paddle_frect.size[0]/2) 
    bally1 = ball_frect.pos[1]
    ai_paddle_x = paddle_frect.pos[0] + (paddle_frect.size[0]/2)
    ai_paddle_y = paddle_frect.pos[1] + (paddle_frect.size[1]/2)
    dx = (ballx1-ballx2)
    if ai_paddle_x < table_size[0]/2:
        if ballx1 <=ballx2:
            while (paddle_frect.pos[1]+paddle_frect.size[1]) <= (table_size[1]) and paddle_frect.pos[1]>=0:
                if bally1<=bally2:
                    if dx !=0:
                        slope = (bally1-bally2)/dx
                    else:
                        return
                    distyinit = bally2
                    if slope!=0:
                        distxinit = distyinit/slope
                        periodx = 2*table_size[1]/slope
                        remainx = (ballx2 - distxinit)%periodx
                        if ballx2 - distxinit <0:
                            crit_pt = distyinit*(distxinit-ballx2)/distxinit
                        elif remainx<(periodx/2):
                            crit_pt = remainx*(slope)
                        elif remainx>=(periodx/2):
                            newremainx = remainx - periodx/2
                            crit_pt = table_size[1]-(newremainx)*(slope)
                        if (ai_paddle_y)<crit_pt:
                            ballx2 = ballx1
                            bally2 = bally1
                            if ball_frect.pos[0] + (ball_frect.size[0]/2) - (paddle_frect.pos[0] + (paddle_frect.size[0]/2)) <=30 and paddle_frect.pos[1]<table_size[1] - paddle_frect.size[1] and paddle_frect.pos[1]>0 and slope<0.1:
                                return "up"
                            if ball_frect.pos[0] + (ball_frect.size[0]/2) - (paddle_frect.pos[0] + (paddle_frect.size[0]/2)) <=20 and paddle_frect.pos[1]<table_size[1] - paddle_frect.size[1] and paddle_frect.pos[1]>0 and slope<0.8:
                            
                                return "up"
                            return "down"
                        elif (ai_paddle_y)>crit_pt:
                            ballx2 = ballx1
                            bally2 = bally1
                            if ball_frect.pos[0] + (ball_frect.size[0]/2) - (paddle_frect.pos[0] + (paddle_frect.size[0]/2)) <=30 and paddle_frect.pos[1]<table_size[1] - paddle_frect.size[1] and paddle_frect.pos[1]>0 and slope<0.1:
                              
                                return "up"
                            if ball_frect.pos[0] + (ball_frect.size[0]/2) - (paddle_frect.pos[0] + (paddle_frect.size[0]/2)) <=20 and paddle_frect.pos[1]<table_size[1] - paddle_frect.size[1] and paddle_frect.pos[1]>0 and slope<0.8:
                           
                                return "up"
                            return "up"
                        else:
                            ballx2 = ballx1
                            bally2 = bally1
                            if ball_frect.pos[0] + (ball_frect.size[0]/2) - (paddle_frect.pos[0] + (paddle_frect.size[0]/2)) <=30 and paddle_frect.pos[1]<table_size[1] - paddle_frect.size[1] and paddle_frect.pos[1]>0 and slope<0.1:
                            
                                return "up"
                            if ball_frect.pos[0] + (ball_frect.size[0]/2) - (paddle_frect.pos[0] + (paddle_frect.size[0]/2)) <=20 and paddle_frect.pos[1]<table_size[1] - paddle_frect.size[1] and paddle_frect.pos[1]>0 and slope<0.8:
                             
                                return "up"
                          
                            return "down"
                    elif slope == 0:
                        return 

                elif bally1>=bally2:
                    #going down
                    if dx !=0:
                        slope =(bally2-bally1)/dx
                    else:
                        return
                  
                    distyinit2 = table_size[1] - bally2
                 
                    if slope!=0:
                        distxinit = distyinit2/slope
                        periodx = 2*table_size[1]/slope
                        
                        remainx = (ballx2 - distxinit)%periodx
                        if ballx2 - distxinit <0:
                            crit_pt = table_size[1] - distyinit2*(distxinit-ballx2)/distxinit
                        elif remainx<(periodx/2):
                            crit_pt = table_size[1] - remainx*(slope)
                        elif remainx>=(periodx/2):
                            newremainx = remainx - periodx/2
                            crit_pt = newremainx*(slope)
                        if (ai_paddle_y)<crit_pt:
##                            if ball_frect.pos[0] + (ball_frect.size[0]/2) - (paddle_frect.pos[0] + (paddle_frect.size[0]/2)) <=30 and paddle_frect.pos[1]<table_size[1] - paddle_frect.size[1] and paddle_frect.pos[1]>0 and slope<0.1:
##                            
##                                return "up"
##                            if ball_frect.pos[0] + (ball_frect.size[0]/2) - (paddle_frect.pos[0] + (paddle_frect.size[0]/2)) <=20 and paddle_frect.pos[1]<table_size[1] - paddle_frect.size[1] and paddle_frect.pos[1]>0 and slope<0.8:
##                       
##                                return "up"
                            ballx2 = ballx1
                            bally2 = bally1

                            return "down"
                            
                        
                        elif (ai_paddle_y)>crit_pt:
##                            if ball_frect.pos[0] + (ball_frect.size[0]/2) - (paddle_frect.pos[0] + (paddle_frect.size[0]/2)) <=30 and paddle_frect.pos[1]<table_size[1] - paddle_frect.size[1] and paddle_frect.pos[1]>0 and slope<0.1:
##                              
##                                return "up"
##                            if ball_frect.pos[0] + (ball_frect.size[0]/2) - (paddle_frect.pos[0] + (paddle_frect.size[0]/2)) <=20 and paddle_frect.pos[1]<table_size[1] - paddle_frect.size[1] and paddle_frect.pos[1]>0 and slope<0.8:
##                               
##                                return "up"
                            ballx2 = ballx1
                            bally2 = bally1
                           
                            return "up"
                        else:
##                            if ball_frect.pos[0] + (ball_frect.size[0]/2) - (paddle_frect.pos[0] + (paddle_frect.size[0]/2)) <=30 and paddle_frect.pos[1]<table_size[1] - paddle_frect.size[1] and paddle_frect.pos[1]>0 and slope<0.1:
##                              
##                                return "up"
##                            if ball_frect.pos[0] + (ball_frect.size[0]/2) - (paddle_frect.pos[0] + (paddle_frect.size[0]/2)) <=20 and paddle_frect.pos[1]<table_size[1] - paddle_frect.size[1] and paddle_frect.pos[1]>0 and slope<0.8:
##                              
##                                return "up"
                            ballx2 = ballx1
                            bally2 = bally1
                           
                            return "down"
                    elif slope == 0:
                        return
        elif ballx1 > ballx2:
            ballx1 = ball_frect.pos[0]
            ball_mid_x = ball_frect.pos[0] + (ball_frect.size[0]/2)
            ball_mid_y = ball_frect.pos[1] + (ball_frect.size[1]/2)
            ai_paddle_x = paddle_frect.pos[0] + (paddle_frect.size[0]/2)
            ai_paddle_y = paddle_frect.pos[1] + (paddle_frect.size[1]/2)

            if ai_paddle_y>(table_size[1]/2):
                ballx2 = ballx1
                bally2 = bally1
                return "up"
            elif ai_paddle_y<=(table_size[1]/2):
                ballx2 = ballx1
                bally2 = bally1
                return "down"
    #Right Side
    counter()
    ballx0 = ball_frect.pos[0]
    bally0 = ball_frect.pos[1]
    ballx1 = ball_frect.pos[0] 
    bally1 = ball_frect.pos[1]
    ai_paddle_x = paddle_frect.pos[0] + (paddle_frect.size[0]/2)
    ai_paddle_y = paddle_frect.pos[1] + (paddle_frect.size[1]/2)
    dx = (ballx1-ballx2)
    if ai_paddle_x > table_size[0]/2:
        if ballx1 >=ballx2:
            while (paddle_frect.pos[1]+paddle_frect.size[1]) <= (table_size[1]) and paddle_frect.pos[1]>=0:
                if bally1<=bally2:
                    #going up
                    if dx !=0:
                        slope = (bally2-bally1)/dx
                    else:
                        return
                    #slope pos
                    distyinit = bally2
                    #print slope
                    if slope!=0:
                        distxinit = distyinit/slope
                        periodx = 2*table_size[1]/slope
                        remainx = (table_size[0] - (table_size[0] - ai_paddle_x) - ballx2 - distxinit)%periodx
                        if (ai_paddle_x-ballx2) - distxinit <0:
                            crit_pt = distyinit*(ballx2+distxinit-ai_paddle_x)/distxinit
                        elif remainx<(periodx/2):
                            crit_pt = remainx*(slope)
                        elif remainx>=(periodx/2):
                            newremainx = remainx - periodx/2
                            crit_pt = table_size[1]-(newremainx)*(slope)
                        if (ai_paddle_y)<crit_pt:
                            ballx2 = ballx1
                            bally2 = bally1
##                            if ball_frect.pos[0] + (ball_frect.size[0]/2) - (paddle_frect.pos[0] + (paddle_frect.size[0]/2)) <=30 and paddle_frect.pos[1]<table_size[1] - paddle_frect.size[1] and paddle_frect.pos[1]>0 and slope<0.1:
##                                return "up"
##                            if ball_frect.pos[0] + (ball_frect.size[0]/2) - (paddle_frect.pos[0] + (paddle_frect.size[0]/2)) <=20 and paddle_frect.pos[1]<table_size[1] - paddle_frect.size[1] and paddle_frect.pos[1]>0 and slope<0.8:
##                            
##                                return "up"
                            return "down"
                        elif (ai_paddle_y)>crit_pt:
                            ballx2 = ballx1
                            bally2 = bally1
##                            if ball_frect.pos[0] + (ball_frect.size[0]/2) - (paddle_frect.pos[0] + (paddle_frect.size[0]/2)) <=30 and paddle_frect.pos[1]<table_size[1] - paddle_frect.size[1] and paddle_frect.pos[1]>0 and slope<0.1:
##                              
##                                return "up"
##                            if ball_frect.pos[0] + (ball_frect.size[0]/2) - (paddle_frect.pos[0] + (paddle_frect.size[0]/2)) <=20 and paddle_frect.pos[1]<table_size[1] - paddle_frect.size[1] and paddle_frect.pos[1]>0 and slope<0.8:
##                           
##                                return "up"
                            return "up"
                        else:
                            ballx2 = ballx1
                            bally2 = bally1
##                            if ball_frect.pos[0] + (ball_frect.size[0]/2) - (paddle_frect.pos[0] + (paddle_frect.size[0]/2)) <=30 and paddle_frect.pos[1]<table_size[1] - paddle_frect.size[1] and paddle_frect.pos[1]>0 and slope<0.1:
##                            
##                                return "up"
##                            if ball_frect.pos[0] + (ball_frect.size[0]/2) - (paddle_frect.pos[0] + (paddle_frect.size[0]/2)) <=20 and paddle_frect.pos[1]<table_size[1] - paddle_frect.size[1] and paddle_frect.pos[1]>0 and slope<0.8:
##                             
##                                return "up"
                          
                            return "down"
                    elif slope == 0:
                        return
                    ####
                #elif bally1>=bally2:
                elif bally1>=bally2:
                    #going down
                    if dx !=0:
                        slope =(bally1-bally2)/dx
                    else:
                        return
                    #slope pos
                    distyinit2 = table_size[1] - bally2
                    #print slope
                    if slope!=0:
                        distxinit = distyinit2/slope
                        periodx = 2*table_size[1]/slope
                        
                        remainx = (ai_paddle_x - ballx2 - distxinit)%periodx
                        if distxinit > (ai_paddle_x-ballx2):
                            crit_pt = table_size[1] - (distyinit2*(distxinit+ballx2-ai_paddle_x))/distxinit
                        elif remainx<(periodx/2):
                            crit_pt = table_size[1] - remainx*(slope)
                        elif remainx>=(periodx/2):
                            newremainx = remainx - periodx/2
                            crit_pt = newremainx*(slope)
                        if (ai_paddle_y)<crit_pt:
##                            if ball_frect.pos[0] + (ball_frect.size[0]/2) - (paddle_frect.pos[0] + (paddle_frect.size[0]/2)) <=30 and paddle_frect.pos[1]<table_size[1] - paddle_frect.size[1] and paddle_frect.pos[1]>0 and slope<0.1:
##                            
##                                return "up"
##                            if ball_frect.pos[0] + (ball_frect.size[0]/2) - (paddle_frect.pos[0] + (paddle_frect.size[0]/2)) <=20 and paddle_frect.pos[1]<table_size[1] - paddle_frect.size[1] and paddle_frect.pos[1]>0 and slope<0.8:
##                       
##                                return "up"
                            ballx2 = ballx1
                            bally2 = bally1
                        
                            return "down"
                        elif (ai_paddle_y)>crit_pt:
##                            if ball_frect.pos[0] + (ball_frect.size[0]/2) - (paddle_frect.pos[0] + (paddle_frect.size[0]/2)) <=30 and paddle_frect.pos[1]<table_size[1] - paddle_frect.size[1] and paddle_frect.pos[1]>0 and slope<0.1:
##                              
##                                return "up"
##                            if ball_frect.pos[0] + (ball_frect.size[0]/2) - (paddle_frect.pos[0] + (paddle_frect.size[0]/2)) <=20 and paddle_frect.pos[1]<table_size[1] - paddle_frect.size[1] and paddle_frect.pos[1]>0 and slope<0.8:
##                               
##                                return "up"
                            ballx2 = ballx1
                            bally2 = bally1
                           
                            return "up"
                        else:
##                            if ball_frect.pos[0] + (ball_frect.size[0]/2) - (paddle_frect.pos[0] + (paddle_frect.size[0]/2)) <=30 and paddle_frect.pos[1]<table_size[1] - paddle_frect.size[1] and paddle_frect.pos[1]>0 and slope<0.1:
##                              
##                                return "up"
##                            if ball_frect.pos[0] + (ball_frect.size[0]/2) - (paddle_frect.pos[0] + (paddle_frect.size[0]/2)) <=20 and paddle_frect.pos[1]<table_size[1] - paddle_frect.size[1] and paddle_frect.pos[1]>0 and slope<0.8:
##                              
##                                return "up"
                            ballx2 = ballx1
                            bally2 = bally1
                           
                            return "down"
                    elif slope == 0:
                        return
        elif ballx1 < ballx2:
            ballx1 = ball_frect.pos[0]
            ball_mid_x = ball_frect.pos[0] + (ball_frect.size[0]/2)
            ball_mid_y = ball_frect.pos[1] + (ball_frect.size[1]/2)
            ai_paddle_x = paddle_frect.pos[0] + (paddle_frect.size[0]/2)
            ai_paddle_y = paddle_frect.pos[1] + (paddle_frect.size[1]/2)

            if ai_paddle_y>(table_size[1]/2):
                ballx2 = ballx1
                bally2 = bally1
                return "up"
            elif ai_paddle_y<=(table_size[1]/2):
                ballx2 = ballx1
                bally2 = bally1
                return "down"
