n_q1 = int(input())
while n_q1 !=0:
    div_point = input().split()

    div_point_x = int(div_point[0])
    div_point_y = int(div_point[1])

    q1 = []

    for n in range(0, n_q1):
        q1.append([int(i) for i in input().split()])

    for ppo in q1:
        if ppo[1]-div_point_y == 0 or ppo[0]-div_point_x == 0:
            print("divisa")
        elif ppo[1]-div_point_y > 0 and ppo[0]-div_point_x > 0:
            print("NE")
        elif ppo[1]-div_point_y > 0 and ppo[0]-div_point_x < 0:
            print("NO")
        elif ppo[1]-div_point_y < 0 and ppo[0]-div_point_x > 0:
            print("SE")
        elif ppo[1]-div_point_y < 0 and ppo[0]-div_point_x < 0:
            print("SO")
    n_q1 = int(input())