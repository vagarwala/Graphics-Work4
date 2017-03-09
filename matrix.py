import math

def make_translate( x, y, z ):
    mat = new_matrix()
    mat = ident(mat)
    mat[3][0] = x
    mat[3][1] = y
    mat[3][2] = z
    return mat

def make_scale( x, y, z ):
    mat = new_matrix()
    mat = ident(mat)
    mat[0][0] = x
    mat[1][1] = y
    mat[2][2] = z
    return mat

def make_rotX( theta ):    
    theta = math.radians(theta)
    mat = new_matrix()
    mat = ident(mat)
    mat[1][1] = math.cos(theta)
    mat[2][1] = -1*math.sin(theta)
    mat[1][2] = math.sin(theta)
    mat[2][2] = math.cos(theta)
    return mat

def make_rotY( theta ):
    theta = math.radians(theta)
    mat = new_matrix()
    mat = ident(mat)
    mat[0][0] = math.cos(theta)
    mat[2][0] = math.sin(theta)
    mat[2][2] = math.cos(theta)
    mat[0][2] = -1*math.sin(theta)
    return mat

def make_rotZ( theta ):
    theta = math.radians(theta)
    mat = new_matrix()
    mat = ident(mat)
    mat[0][0] = math.cos(theta)
    mat[1][0] = -1*math.sin(theta)
    mat[0][1] = math.sin(theta)
    mat[1][1] = math.cos(theta)
    return mat

def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            s+= str(matrix[c][r]) + ' '
        s+= '\n'
    print s

def ident( matrix ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            if r == c:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0
    return matrix

def scalar_mult( matrix, s ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            matrix[c][r]*= s
            
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    point = 0
    for row in m2:
        tmp = row[:]
        for r in range(4):
            m2[point][r] = (m1[0][r] * tmp[0] +
                            m1[1][r] * tmp[1] +
                            m1[2][r] * tmp[2] +
                            m1[3][r] * tmp[3])
        point += 1
    return m2

def new_matrix(rows = 4, cols = 4):
    mat = []
    for c in range( cols ):
        mat.append( [] )
        for r in range( rows ):
            mat[c].append( 0 )
    return mat
