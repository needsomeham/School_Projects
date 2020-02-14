import math
import string

def is_grashof(links: []):
    links.sort()
    if links[0] + links[3] <= links[1] + links[2]:
        return True
    return False

def tran_angles(rockerType):
    if rockerType == 'Crank Rocker':
        angle1 = math.acos( (b**2 + c**2 - (d + a)**2 )/(2*b*c))
        angle2 = math.pi - math.acos( (b**2 + c**2 - (d + a)**2 )/(2*b*c))
        return angle1, angle2

    if rockerType == 'Rocker Rocker':
        angle1 = 0
        angle2 = math.acos( ( (a+b)**2 + c**2)/(2*c*(a+b)))
        return angle1,angle2

    if rockerType == 'Crank Crank':
        return "You are an idiot","stupid"


def toggle_nonGrashof():
    try:
        theta1 = math.acos( (a**2 + d**2 - b**2 - c**2)/(2*a*d) + (b*c)/(a*d) )
    except ValueError:
        theta2 = math.acos( (a**2 + d**2 - b**2 - c**2)/(2*a*d) - (b*c)/(a*d) )
        return to_degrees(theta2),to_degrees( -theta2)
    return to_degrees(theta1), to_degrees(-theta1)

def to_degrees(angle):
    deg = (180*angle) / math.pi
    return deg

def to_radians(angle):
    rad = (angle*math.pi)/180
    return rad

def if_negative(angle):
    if angle<0:
        return 360 + angle
    return angle

def find_all_fourbar_angles():
    K1 = d/a
    K2 = d/c
    K3 = (a**2 - b**2 + c**2 + d**2)/(2*a*c)

    # Finding angles for theta 4
    A = math.cos(theta) - K1 - K2*math.cos(theta) + K3
    B = -2*math.sin(theta)
    C = K1 - (K2+1)*math.cos(theta) + K3

    theta41rad = 2*math.atan((-B-math.sqrt(B**2-4*A*C))/(2*A))
    theta42rad = 2*math.atan((-B+math.sqrt(B**2-4*A*C))/(2*A))

    theta41 = if_negative(to_degrees(theta41rad))
    theta42 = if_negative(to_degrees(theta42rad))

    # Finding angles for theta 3
    K4 = d/b
    K5 = (c**2 - d**2 - a**2 - b**2)/(2*a*b)
    D = math.cos(theta) - K1 + K4*math.cos(theta) + K5
    E = -2*math.sin(theta)
    F = K1 + (K4-1)*math.cos(theta) + K5

    theta31rad = 2*math.atan((-E-math.sqrt(E**2 - 4*D*F))/(2*D))
    theta32rad = 2*math.atan((-E+math.sqrt(E**2 - 4*D*F))/(2*D))

    theta31 = if_negative(to_degrees(theta31rad))
    theta32 = if_negative(to_degrees(theta32rad))

    return theta31,theta32,theta41,theta42

def grubler(L,J1,J2):
    M = 3*(L-1) - 2*(J1) - J2
    return M

def find_type(links: []):
    a = inLink =  links[0]
    h = couplelink = links[1]
    b = outLink = links[2]
    g = groundLink = links[3]
    theta = links[4]

    T1 = g + h - a - b
    if T1 > 0:
        T1 = True
    T2 = b + g - a - h
    if T2 > 0:
        T2 = True
    T3 = b + h - a - g
    if T3 > 0:
        return True

    # Crank Crank
    if (not T1) and (not T2) and T3:
        return True, True

    # Crank Rocker
    if T1 and T2 and T3:
        return True, False

    # Rocker Crank
    if T1 and (not T2) and (not T3):
        return False, True

    # Rocker Rocker
    if (not T1) and T2 and (not T3):
        return False, False

    # Other cases are all nonGrashof and Rocker Rocker
    else:
        return False, False

def get_alphabet():
    return list(string.ascii_lowercase)


if __name__ == '__main__':

    # Setting Globals for rest of code to borrow
    global a,b,c,d, theta
    letters = get_alphabet()

    # Fourbar links defined as in, couple, out, ground, angle (from ground to in)
    allLinks = [ [6,2,7,9,30],
                 [7,9,3,8,85],
                 [3,10,6,8,45],
                 [8,5,7,6,25,],
                 [8,5,8,6,75],
                 [5,8,8,9,15],
                 [6,8,8,9,25],
                 [20,10,10,10,50],
                 [4,5,2,5,80],
                 [20,10,5,10,33],
                 [4,6,10,7,88],
                 [9,7,10,7,60],
                 [9,7,11,8,50],
                 [9,7,11,6,120],
                 ]

    # Solving each fourbar set up from master list above
    for i in range(len(allLinks)):
        config = allLinks[i]
        a = config[1]
        b = config[2]
        c = config[3]
        d = config[0]
        theta = to_radians(config[4])
        links = [config[0],config[1],config[2],config[3]]
        th1, th2, th3, th4 = find_all_fourbar_angles()

        # printing all solutions
        print(f'Given row {letters[i]} with link sizes {a}, {b}, {c}, {d} and an angle of {config[4]} degrees')
        print("Is grashof?", is_grashof(links))
        print('All possible angles are:')
        print(f'Theta 3,1: {round(th1,4)} \nTheta 3,2: {round(th2,4)} \nTheta 4,1: {round(th3,4)} \nTheta 4,2: {round(th4,4)}')
        if i == 3:
            a1,a2 = tran_angles('Crank Rocker')
            print(f'Transmission Angles are: \n{round(a1,4)} \n{round(a2,4)}')
        if not is_grashof(links):
            t1,t2 = toggle_nonGrashof()
            print(f'Toggle positions are: \n{round(t1,4)} \n{round(t2,4)}')
        print("")
