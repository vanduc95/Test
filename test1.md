**Ứng dụng Horizon vào Docker**
=======
Bài viết này sẽ hướng dẫn mọi người cách làm các task về Docker trong Horizon sau:

 - Tạo 1 panel **container** chứa bảng hiển thị thông tin các container và có các action **create container**, **delete container**, **filter container**
 -  Biểu đồ hình đường biểu diễn **resource usage** của container.

1. Cài đặt và thiết lập ban đầu
-------
### 1.1 Cài đặt docker-py
Để có thể lấy thông tin về các container cũng như thông tin về resource usage chúng ta cần cài đặt **docker-py**
**Docker-py** là một thư viện Python cho phép chúng ta quản lí, điều khiển Docker thông qua API. 

    pip install docker-py
   Đọc [document](https://docker-py.readthedocs.io/en/latest/api/) để biết thêm về cách sử dụng **docker-py**

### 1.2 Tạo dashboard mới
Chúng ta cần tạo một dashboard mới theo hướng dẫn sau:

    mkdir openstack_dashboard/dashboards/custom_horizon 

    ./run_tests.sh -m startdash custom_horizon \
    --target openstack_dashboard/dashboards/custom_horizon
    
    mkdir openstack_dashboard/dashboards/custom_horizon/container
    
    ./run_tests.sh -m startpanel images_OPS \
    --dashboard=openstack_dashboard.dashboards.custom_horizon \
    --target=openstack_dashboard/dashboards/custom_horizon/container
   Sau đó, thư mục custom_horizon của chúng ta sẽ có định dạng thư mục như sau:
   

    custom_horizon
    ├── dashboard.py
    ├── dashboard.pyc
    ├── __init__.py
    ├── __init__.pyc
    ├── container
    │   ├── __init__.py
    │   ├── panel.py
    │   ├── templates
    │   │   └── container
    │   │       └── index.html
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── static
    │   └── container
    │       ├── css
    │       │   └── custom_horizon.css
    │       └── js
    │           └── custom_horizon.js
    └── templates
        └── custom_horizon
            └── base.html

2. Tạo bảng hiển thị thông tin về các container
-------

 

 
