#import matplotlib.pyplot as plt


def fanspeed_array_calculate(profile):
    fanspeed_array = [0]*100
    for temp in range(0,100):
        for i in range(0,len(profile["temp"])):
            if temp < profile["temp"][i]:
                m = (profile["fanspeed"][i] - float(profile["fanspeed"][i-1]))/(profile["temp"][i]-profile["temp"][i-1])
                fanspeed_array[temp] = int(round(m*(temp-profile["temp"][i]) + profile["fanspeed"][i]))
                break
            else:
                continue
    return fanspeed_array


def default_fanprofile():
    fanspeed_profile = {"fanspeed": [0, 0, 28, 33, 42, 52, 64, 86, 100, 100],
                        "temp":     [0, 30, 31, 40, 50, 60, 70, 80, 90, 100]}
    return fanspeed_array_calculate(fanspeed_profile)


if __name__ == '__main__':
    fanspeed_profile = {"fanspeed":[0,0,28,33,42,50,60,80,100,100],
                            "temp":[0,30,31,40,50,60,70,80,90,100]}
    fanspeed_list = fanspeed_array_calculate(fanspeed_profile)
    print fanspeed_list
#    plt.plot(range(0, 100), fanspeed_list)
#    plt.show()





