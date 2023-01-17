import math

def ori_value(x):
    a=math.log(x)
    return a

def linear(x1,x2,y1,y2,x):
    y=y1 + (x-x1)/(x2-x1)*(y2-y1)
    return y



def main():
    x=[1,2,3,4]
    y=[0,0.693,1.099,1.386]
    x_t=float(input("please input desired x value: "))
    y0=ori_value(x_t)
    if (x_t >x[0] and x_t <x[1]):
        y_t=linear(x[0],x[1],y[0],y[1],x_t)
    elif(x_t >x[1] and x_t <x[2]):
        y_t=linear(x[1],x[2],y[1],y[2],x_t)
    elif(x_t >x[2] and x_t <x[3]):
        y_t=linear(x[2],x[3],y[2],y[3],x_t)
    elif(x_t >x[3] and x_t <x[4]):
        y_t=linear(x[3],x[4],y[3],y[4],x_t)
    else:
        print("x needs to be between 0 and 4")
    print(y0,y_t)
    





if __name__ == '__main__':
    main()