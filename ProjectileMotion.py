import math
import time





# u=(eval(input("initial velocity of ball=")))
# theta=(eval(input("angle of launch")))
# xpos=0
# ypos=0
# time_step=0.1

g =9.81


def projection_object(u,theta,xpos,ypos,time_step):
    theta_rad = theta * math.pi / 180

    u_y = u * math.sin(theta_rad)

    u_x = u*math.cos(theta_rad)

    xpos_new=xpos+(u_x*time_step)
    xpos_new=(u_x*time_step)

    v_y = u_y - g * time_step

    theta_final=math.atan(v_y/u_x)*180/math.pi

    #ypos_new=ypos-((u_y*time_step)-(g/2*time_step**2))
    ypos_new =((u_y * time_step) - (g / 2 * time_step ** 2))
    v_final=math.sqrt((v_y**2 +u_x**2))
    #theta_final = math.atan(ypos_new / xpos_new) * 180 / math.pi

    # theta_final = math.asin(v_y /v_final) * 180 / math.pi
    if xpos_new<0:
        theta_final=theta_final+180
    # theta_final= math.acos(u_x/v_final)
    # print ("velocity y final=" + str(v_y))
    # print("velocity x final=" + str(u_x))
    # print("theta final=" + str(theta_final))
    # print("xpos_new, ypos_new=" + str(xpos_new)+" , " + str(ypos_new))
    # print("v final=" + str(v_final))
    # print("")

    # time.sleep(0.5)
    #projection_object(v_final, theta_final, xpos_new, ypos_new, 0.1)
    # if v_final>u:
    #     return

    return (v_final,theta_final,xpos_new,ypos_new,0.1)

# B=projection_object(u,theta,xpos,ypos,time_step)
#
# print(B)
#
# # C=projection_object([D])
# # print(C)
#
# while True:
#     B=projection_object(B[0], B[1], B[2], B[3], B[4])
#
#     if B[3]<0:
#         break
