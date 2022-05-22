from PIL import Image
import numpy as np
def get_approx_SVD1(data,percent):#SVD并还原压缩后的数据，percent代表奇异值的百分比
    U, s, VT = np.linalg.svd(data) #进行SVD
    Sigma=np.zeros(np.shape(data))
    Sigma[:len(s),:len(s)]=np.diag(s)      #获得奇异值矩阵
    k=(int)(percent*len(s))   #k是奇异值个数的百分比的个数
    D=U[:,:k].dot(Sigma[:k,:k].dot(VT[:k,:])) #SVD还原后的数据
    D[D < 0] = 0
    D[D > 255] = 255
    return np.rint(D).astype("uint8")

def get_approx_SVD2(data,percent):#SVD并还原压缩后的数据，percent代表奇异值总和的百分比
    U, s, VT = np.linalg.svd(data)  #进行SVD
    Sigma=np.zeros(np.shape(data))
    Sigma[:len(s),:len(s)]=np.diag(s)
    count=(int)(sum(s))*percent
    k=-1  #k是奇异值总和的百分比的个数
    curSum=0 #初值为第一个奇异值
    while curSum <= count :
        k+=1
        curSum += s[k]
    print("U的大小：",U.shape,"奇异值的大小：",len(s),"k=",k,"VT的大小：",VT.shape)
    D=U[:,:k].dot(Sigma[:k,:k].dot(VT[:k,:])) #SVD还原后的数据
    D[D<0] = 0
    D[D>255] = 255
    return np.rint(D).astype("uint8")

#导入图像，进行SVD压缩，并重构图像

def rebuild_img(filename,p,get_approx_SVD):
#filename代表文件名，p代表百分比，#get_approx_SVD代表调用的SVD筛选方法
    img = Image.open(filename, 'r')#打开文件
    a = np.array(img)#获得色素值
    R0=a[:, :, 0] #获得红色的色素值
    G0=a[:, :, 1] #获得绿色的色素值
    G0=a[:, :, 2] #获得蓝色的色素值
    R = get_approx_SVD(R0,p)#对红色进行SVD还原
    G = get_approx_SVD(G0,p)#对绿色进行SVD还原
    B = get_approx_SVD(G0,p)#对蓝色进行SVD还原
    I = np.stack((R, G, B), 2)
    Image.fromarray(I).save("IMG_11" + str(p*100)+".jpg")#保存图片
    img=Image.open("IMG_11" + str(p * 100) + ".jpg", 'r')
    img.show()#显示图片

filename="digit.bmp"
for p in np.arange(0.2, 1.01, 0.2):
    print("p=",p)
    rebuild_img(filename,p,get_approx_SVD2)
for p in np.arange(0.2, 1.01, 0.2):
    rebuild_img(filename,p,get_approx_SVD1)