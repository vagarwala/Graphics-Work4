from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform, screen, color ):
    script = open(fname)
    instr = script.read().split('\n')
    i = 0
    while i < len(instr):
        print i
        print instr[i]
        if instr[i] == "line":
            i += 1
            values = instr[i].split(' ')
            add_edge( points, int(values[0]), int(values[1]), int(values[2]), int(values[3]), int(values[4]), int(values[5])) 
        elif instr[i] == "circle":
            i += 1
            values = instr[i].split(' ')
            add_circle( points, int(values[0]), int(values[1]), 0, int(values[2]), float(1/50)) 
        elif instr[i] == "ident":
            transform = new_matrix(4, 4)
            ident(transform)
            i += 1
        elif instr[i] == "scale":
            i += 1
            values = instr[i].split(' ')
            scale = make_scale( float(values[0]), float(values[1]), float(values[2]))
            matrix_mult(scale, transform)
        elif instr[i] == "move":
            i += 1
            values = instr[i].split(' ')
            translate = make_translate( int(values[0]), int(values[1]), int(values[2]))
            matrix_mult(translate, transform)
        elif instr[i] == "rotate":
            i += 1
            values = instr[i].split(' ')
            if values[0] == 'x':
                rot = make_rotX(int(values[1]))
            if values[0] == 'y':
                rot = make_rotY(int(values[1]))
            if values[0] == 'z':
                rot = make_rotZ(int(values[1]))
            matrix_mult(rot, transform)
        elif instr[i] == "apply":
            matrix_mult(transform, points)
        elif instr[i] == "display":
            clear_screen(screen)
            draw_lines(points, screen, [255, 255, 255])
            i += 1
        elif instr[i] == "save":
            draw_lines(points, screen, [255, 255, 255])
            i += 1
            save_ppm(screen, instr[i])
        i += 1



