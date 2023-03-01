import numpy as np

  
def convolve(image, kernel):
    # 获取图像和核函数的尺寸
    image_rows, image_cols = image.shape
    kernel_rows, kernel_cols = kernel.shape
    
    # 计算卷积输出的尺寸
    result_rows = image_rows - kernel_rows + 1
    result_cols = image_cols - kernel_cols + 1
    
    # 初始化输出卷积数组
    result = np.zeros((result_rows, result_cols))
    
    # 对图像中的每一个子区域与核进行卷积
    for i in range(result_rows):
        for j in range(result_cols):
            sub_image = image[i:i+kernel_rows, j:j+kernel_cols]
            result[i, j] = np.sum(sub_image * kernel)
    
    return result

if __name__  == "__main__":
    
    image = np.array([[1,2,3],[4,5,6],[7,8,9]])
    kernel = np.array([[0,1,0],[1,-4,1],[0,1,0]])

    result = convolve(image,kernel)
    #print(result)
