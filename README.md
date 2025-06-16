# xl-driver-demo

通过 Python 调用 [XL-Driver-Library](https://www.vector.com/us/en/products/products-a-z/libraries-drivers/xl-driver-library/#) 实现收发 [Vector 硬件](https://www.vector.com/us/en/products/products-a-z/hardware/#) 的消息

# 预览

![image](https://github.com/user-attachments/assets/2050443e-39fa-4f28-98ec-e19d60b87e28)

# 功能

- 选择 CAN 硬件的通道
- 建立连接
- 发送报文（待完成）
- 监听总线

# 注意

通过 Vector 提供的 Xl-Driver-Library 开发工具***过于繁琐***，建议使用 python 第三方库：[udsoncan](https://udsoncan.readthedocs.io/en/latest/index.html)，参考 udsoncan 的[官方示例](https://udsoncan.readthedocs.io/en/latest/udsoncan/examples.html#using-uds-over-python-can)
