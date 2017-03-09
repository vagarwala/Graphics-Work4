from display import *
from matrix import *
from draw import *

def parse_file( fname, edge, transform, screen, color ):
    cmds = open(fname,'r').read().split("\n")
    i = 0 
    while i < len(cmds):
        if cmds[i] == "line":
            params = cmds[i+1].split(" ")
            add_edge(edge ,int(params[0]), int(params[1]), int(params[2]), int(params[3]), int(params[4]), int(params[5]))
            i += 1
        if cmds[i] == "ident":
            transform = ident(new_matrix())
        if cmds[i] == "scale":
            params = cmds[i+1].split(" ")
            m = make_scale( int(params[0]), int(params[1]), int(params[2]))
            matrix_mult(m,transform)
            i += 1
        if cmds[i] == "move":
            params = cmds[i+1].split(" ")
            matrix_mult(make_translate( int(params[0]), int(params[1]), int(params[2])),transform)
            i += 1
        if cmds[i] == "rotate":
            params = cmds[i+1].split(" ")
            if params[0] == "x":
                matrix_mult(make_rotX( int(params[1])),transform)
            if params[0] == "y":
                matrix_mult(make_rotY( int(params[1])),transform)
            if params[0] == "z":
                matrix_mult(make_rotZ( int(params[1])),transform)
            i += 1
        if cmds[i] == "apply":
            edge = matrix_mult(transform,edge)
        if cmds[i] == "display":
            for x in range(len(edge)):
                for j in range(len(edge[0])):
                    edge[x][j] = int(edge[x][j])
            clear_screen(screen)
            draw_lines(edge,screen,color)
            display(screen)
        if cmds[i] == "save":
            params = cmds[i+1]
            draw_lines(edge,screen,color)
            save_ppm(screen,params)
            i += 1
        i += 1
        
