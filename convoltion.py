import numpy as np
#np.set_printoptions(threshold=np.inf)

if __name__ == '__main__':

  input_height = 28
  input_width = 28
  input_channels = 3

  #卷积核
  kernel_height = 3
  kernel_width = 3

  output_channels = 3

  input_data = np.random.rand(input_height,input_width,input_channels)
  kernel = np.random.rand(kernel_height,kernel_width,input_channels,output_channels)

  #零填充
  pad_h = kernel_height // 2 # 1
  pad_w = kernel_width // 2  # 1
  input_data_padded = np.pad(input_data,((pad_h,pad_h),(pad_w,pad_w),(0,0)),mode ='constant')

  #print(kernel.shape)
  #print(input_data_padded)

  # 初始化数据
  output_height = input_height
  output_width = input_width
  output_channels = kernel.shape[3]
  output_data = np.zeros((output_height,output_width,output_channels))

  #print(output_data)

