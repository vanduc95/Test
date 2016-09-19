**Ứng dụng Horizon vào Docker**
=======
Bài viết này sẽ hướng dẫn mọi người cách làm các task về Docker trong Horizon sau:

 - Tạo 1 panel **container** chứa bảng hiển thị thông tin các container và có các action **create container**, **delete container**, **filter container**
 -  Biểu đồ hình đường biểu diễn **resource usage** của container.

1. Cài đặt docker-py
-------
Để có thể lấy thông tin về các container cũng như thông tin về resource usage chúng ta cần cài đặt **docker-py**
**Docker-py** là một thư viện Python cho phép chúng ta quản lí, điều khiển Docker thông qua API. 

    pip install docker-py
