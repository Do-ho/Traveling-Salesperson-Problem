from matplotlib import pyplot as plt

def image(order_li, dots):
    y_li = []
    x_li = []
    for order in order_li:
        x_li.append(dots[order][0])
        y_li.append(dots[order][1])

    plt.figure() # marker 인자를 같이 적는다.
    plt.plot(x_li, y_li, marker='o') 
    plt.show()

# 사용 예시
dots = [[0, 0],
    [372, 519],
    [918, 673],
    [577, 721],
    [451, 3],
    [939, 924],
    [729, 220],
    [118, 622],
    [884, 367],
    [406, 704],
    [149, 900],
    [119, 569],
    [879, 784],
    [254, 306],
    [380, 351],
    [391, 7],
    [166, 252],
    [499, 459],
    [978, 535],
    [476, 140],
    [478, 424],
    [436, 217],
    [795, 648],
    [514, 435],
    [153, 988],
    [111, 708],
    [514, 140],
    [911, 622],
    [314, 790],
    [776, 545],
    [385, 888],
    [486, 802],
    [938, 723],
    [146, 70],
    [525, 195],
    [572, 480],
    [735, 373],
    [758, 779],
    [664, 378],
    [49, 953],
    [214, 171],
    [395, 821],
    [183, 105],
    [36, 30],
    [660, 850],
    [726, 364],
    [924, 523],
    [970, 674],
    [608, 152],
    [482, 962],
    [92, 292],
    [408, 369],
    [752, 748],
    [282, 566],
    [991, 878],
    [162, 564],
    [576, 823],
    [298, 906],
    [935, 499],
    [810, 523],
    [225, 181],
    [444, 90],
    [480, 348],
    [688, 635],
    [26, 983],
    [387, 949],
    [436, 393],
    [984, 213],
    [514, 859],
    [481, 78],
    [503, 32],
    [674, 928],
    [964, 514],
    [205, 511],
    [587, 935],
    [201, 542],
    [132, 382],
    [177, 1],
    [578, 347],
    [54, 862],
    [950, 485],
    [4, 455],
    [594, 852],
    [835, 104],
    [905, 724],
    [612, 197],
    [974, 251],
    [586, 868],
    [755, 828],
    [724, 331],
    [612, 442],
    [457, 788],
    [549, 534],
    [331, 769],
    [939, 828],
    [943, 557],
    [291, 151],
    [468, 606],
    [629, 722],
    [823, 487],
    [1000,1000],
]
# order_li = [48, 26, 19, 21, 34, 85, 89, 45, 36, 38, 78, 90, 35, 17, 23, 20, 62, 66, 51, 14, 13, 16, 60, 40, 42, 96, 61, 69, 70, 4, 15, 77, 33, 43, 0, 50, 76, 81, 73, 75, 55, 11, 7, 25, 79, 39, 64, 24, 10, 57, 65, 30, 41, 91, 31, 68, 49, 74, 87, 82, 56, 44, 71, 88, 5, 54, 94, 12, 84, 32, 47, 2, 27, 95, 18, 72, 80, 58, 46, 22, 52, 37, 98, 3, 9, 93, 28, 53, 1, 97, 92, 63, 29, 59, 99, 8, 86, 67, 83, 6, 48]
# order_li = [48, 26, 19, 21, 34, 85, 89, 45, 36, 38, 78, 90, 35, 17, 23, 20, 62, 66, 51, 14, 13, 16, 60, 40, 42, 96, 61, 69, 70, 4, 15, 77, 33, 43, 0, 50, 76, 81, 73, 75, 55, 11, 7, 25, 79, 39, 64, 24, 10, 57, 65, 30, 41, 91, 31, 68, 49, 74, 87, 82, 56, 44, 71, 88, 5, 54, 94, 12, 84, 32, 47, 2, 27, 95, 18, 72, 80, 58, 46, 22, 52, 37, 98, 3, 97, 9, 93, 28, 53, 1, 92, 63, 29, 59, 99, 8, 86, 67, 83, 6, 48]
order_li = [6, 89, 45, 36, 59, 29, 63, 98, 3, 57, 10, 24, 64, 39, 79, 25, 7, 55, 14, 34, 26, 19, 61, 69, 70, 4, 15, 21, 62, 17, 97, 9, 91, 31, 68, 56, 82, 87, 44, 37, 52, 12, 84, 22, 92, 1, 53, 75, 73, 16, 40, 60, 13, 51, 66, 20, 23, 35, 90, 99, 46, 72, 18, 95, 27, 2, 47, 32, 94, 54, 5, 88, 71, 74, 49, 65, 30, 41, 93, 28, 11, 81, 76, 50, 42, 33, 43, 0, 77, 96, 78, 38, 58, 80, 8, 86, 67, 83, 48, 85, 6]
image(order_li, dots)