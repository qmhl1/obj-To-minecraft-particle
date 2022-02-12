import multiprocessing
import cv2
import imutils
import sys




def partic(modell, output, picture,life):
    global b, g, r, yi, bai, shi
    image = cv2.imread(picture, cv2.IMREAD_UNCHANGED)
    img = imutils.rotate(image, 270)
    model = open(modell)
    output = open(output, 'w')
    rgba = []
    dian = -1  # rgb信息提取点
    for h_mel in model:
        # 重置计数器
        k = 0  # 计数器
        vt = 0  # vt判断
        vtt = 0
        time = 0  # 材质坐标判断
        start = 0  # 材质坐标输入启动器
        startt = 1  # 材质坐标个十白判断
        for mel in h_mel:
            k = k + 1
            if vt == 1:
                if startt == 1:
                    if time == 1:
                        if start == 3:
                            start = 0
                            ge = int(mel)
                            yi = bai * 100 + shi * 10 + ge
                        if start == 2:
                            start = start + 1
                            shi = int(mel)
                        if start == 1:
                            start = start + 1
                            bai = int(mel)
                    if time == 2:
                        if start == 3:
                            time = 0
                            start = 0
                            ge = int(mel)
                            er = bai * 100 + shi * 10 + ge
                            img_date = img[yi, er]
                            one_rgba = []
                            for zj_date in img_date:
                                one_rgba.append(int(zj_date))
                            rgba.append(one_rgba)
                        if start == 2:
                            start = start + 1
                            shi = int(mel)
                        if start == 1:
                            start = start + 1
                            bai = int(mel)
            if mel == "v":
                k = 1
            if mel == "t":
                if k == 2:
                    vtt = 1
            if vtt == 1:
                if k == 3:
                    if mel == " ":
                        vt = 1
            if mel == ".":
                startt = 1
                start = 1
                time = time + 1
    model = open(modell)
    dian = -1
    for h_mel in model:
        vt = 0
        k = 0
        rgb_times = 0
        for mel in h_mel:
            k = k + 1
            if vt == 2:
                
                if mel == "\n":
                    
                    dian = dian + 1
                    for rgb in rgba[dian]:
                        
                        rgb_times = rgb_times + 1
                        if rgb_times == 1:
                            r = rgb / 255
                        if rgb_times == 2:
                            g = rgb / 255
                        if rgb_times == 3:
                            b = rgb / 255
                        if rgb_times == 4:
                            al = rgb / 255
                            rgb_times = 0
                            output.write(" " + str(b) + " " + str(g) + " " + str(r) + " " + str(al) + " 240 0 0 0 " + str(life))
            if vt == 2:
                output.write(mel)
            if k == 1:
                if mel == "v":
                    vt = 1
            if k == 2:
                if vt == 1:
                    if mel == " ":
                        vt = 2


objname = "GaiZhiHua"
startframe = 0
allframe = 500


#startframe = sys.argv[2]
#allframe = sys.argv[1]


class myThread (multiprocessing.Process):
    def __init__(self, threadID, name, allframe, w_times):
        multiprocessing.Process.__init__(self)
        self.threadID = threadID
        self.name = name
        self.allframe = allframe
        self.w_times = w_times
    def run(self):
        print (self.threadID + "：点火！")
        par(self.name,self.allframe,self.w_times)
        print (self.threadID + "：关闭！")
def par(name,allframe,w_times):
    w_times += startframe #多服务器节点
    while True:
        if w_times > allframe:
            break
        str_times = w_times
        str_times = str(str_times)
        modell = name + str_times # + ".obj"
        output = name + str_times + ".txt"
        picture = name + ".png"
        if allframe > 1:
            life = 1
        else:
            life = 0
        partic(modell,output,picture,1)#life!!!!!!!!!!!!!!
        w_times = w_times + 12#线程数!!!!!!
if __name__ == '__main__':
    thread1 = myThread("1号发动机",objname,allframe,1)
    thread2 = myThread("2号发动机",objname,allframe,2)
    thread3 = myThread("3号发动机",objname,allframe,3)
    thread4 = myThread("4号发动机",objname,allframe,4)
    thread5 = myThread("5号发动机",objname,allframe,5)
    thread6 = myThread("6号发动机",objname,allframe,6)
    thread7 = myThread("7号发动机",objname,allframe,7)
    thread8 = myThread("8号发动机",objname,allframe,8)
    thread9 = myThread("9号发动机",objname,allframe,9)
    thread10 = myThread("10号发动机",objname,allframe,10)
    thread11 = myThread("11号发动机",objname,allframe,11)
    thread12 = myThread("12号发动机",objname,allframe,12)

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()
    thread10.start()
    thread11.start()
    thread12.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()
    thread9.join()
    thread10.join()
    thread11.join()
    thread12.join()
    print("啪！的一下，很快啊！")