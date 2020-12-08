import numpy as np
class Matrix():
     def __init__(self):
          self.n=int(input("你想要几阶的矩阵(30阶可以欧)"))
          print("说明：输入关系，每次一个数，以空格隔开，结尾一定要以空格结尾\n")
          print("举例如下：<1,2>,<2,3>你应该输入1 2 2 3'空格'\n")
          print("如果想输入一个n阶全零矩阵，关系输入时，直接ENTER确定即可")
          self.str1=input("输入关系")
          self.matrix1=np.zeros((self.n,self.n),dtype=np.int)
     def create_matrix(self):
          list1=[]
          list1_r=[]
          j=0
          s=''
          for i in self.str1:
               if i!=' ':
                    s+=i
               elif i==' ':
                    if j%2==0:
                         list1.append(int(s))
                         s=''
                         j=j+1
                    else:
                         list1_r.append(int(s))
                         s=''
                         j=j+1
          #print(list1,list1_r)
          print("你输入的是：{",end="")
          for i in range(0,len(list1)):
               self.matrix1[list1[i]-1][list1_r[i]-1]=1
               print("<"+str(list1[i])+","+str(list1_r[i])+">",end="")
          print("}")
          print(self.matrix1)
     
     def get(self):
          return self.matrix1

def composite(matrix1,matrix2): #矩阵的复合
     n=matrix1.shape
     matrix3=np.dot(matrix1,matrix2)
     print(matrix3)
     print("复合后的关系是：{",end="")
     for i in range(0,n[0]):
          for j in range(0,n[0]):
               if matrix3[i][j]==1:
                    print("<"+str(i+1)+","+str(j+1)+">",end="")
               elif matrix3[i][j]>1:
                    matrix3[i][j]=1
                    print("<"+str(i+1)+","+str(j+1)+">",end="")
     print("}")
     print("复合矩阵是：")
     print(matrix3)

def reflexivity(matrix):
     n=matrix.shape
     s=0
     for i in range(0,n[0]):
          if matrix[i][i] ==1:
               s=i
          else:
               break
     if s==0 :
          print("矩阵具有反自反性")
     elif s==n[0]-1:
          print("矩阵具有自反性")
     else:
          print("矩阵既不具有自反性，也不具有反自反性")

def symmetry(matrix):
     n=matrix.shape
     sign1=0      #相等且为1
     sign2=0      #不相等
     for i in range(1,n[0]):
          for j in range(0,i):
               if matrix[i][j]==matrix[j][i]==1:
                    sign1=sign1+1
               elif matrix[i][j]!=matrix[j][i]:
                    sign2=sign2+1
     if sign1==0 and sign2>0:
          print("反对称")
     elif sign1>0 and sign2==0:
          print("对称")
     elif sign1>0 and sign2>0:
          print("既不对称，也不反对称")
     elif sign1==0 and sign2==0:
          print("即对称也反对称")
def transform(matrix):
     n=matrix.shape
     s=0
     for i in range(0,n[0]):
          if s>0:
               break
          for j in range(0,n[0]):
               if s>0:
                    break
               if matrix[i][j]==1:
                    for k in range(0,n[0]):
                         if matrix[j][k]==1:
                              if matrix[i][k]==0:
                                   print("不满足传递性")
                                   s=s+1
                                   break

     if s==0:
          print("满足传递性")



     
matrix1=Matrix()
matrix1.create_matrix()
matrix3=matrix1.get()
'''matrix2=Matrix()
matrix2.create_matrix()
matrix4=matrix2.get()
composite(matrix3,matrix4)
symmetry(matrix3)'''
transform(matrix3)










     
