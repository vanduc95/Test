**Ứng dụng Horizon vào Docker**
=======
Bài viết này sẽ hướng dẫn mọi người cách làm các task về Docker trong Horizon sau:

 - Tạo 1 panel **container** chứa bảng hiển thị thông tin các container và có các action **create container**, **delete container**, **filter container**
 -  Biểu đồ hình đường biểu diễn **resource usage** của container.

Ở hướng dẫn này mình chỉ giải thích tác dụng của các đoạn code quan trọng, mọi người nên đọc trước bài hướng dẫn về luông hoạt động khi tạo ra một **Table** trong Horizon tại [đây](#) 

[Source code](#)

1. Cài đặt và thiết lập ban đầu
-------
### 1.1 Cài đặt docker-py
Để có thể lấy thông tin về các container cũng như thông tin về resource usage chúng ta cần cài đặt **docker-py**
**Docker-py** là một thư viện Python cho phép chúng ta quản lí, điều khiển Docker thông qua API. 

    pip install docker-py
   Đọc [document](https://docker-py.readthedocs.io/en/latest/api/) để biết thêm về cách sử dụng **docker-py**

### 1.2 Tạo dashboard mới
Chúng ta cần tạo một [dashboard](https://github.com/openstack/horizon/blob/stable/mitaka/doc/source/tutorials/dashboard.rst) mới theo hướng dẫn sau:

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
Tạo một file `tables.py` dưới thư mục `container` và copy đoạn code sau:
```
from horizon.utils import filters as filters_horizon
from django.utils.translation import ugettext_lazy as _

import horizon

class ContainerDockerTable(tables.DataTable):
    id = tables.Column('id', verbose_name='Container Id')
    image = tables.Column('image', verbose_name='Image')
    command = tables.Column('command', verbose_name='Command')
    created = tables.Column('created', verbose_name='Created',
                            filters=(filters_horizon.parse_isotime,filters_horizon.timesince_sortable),)
    state = tables.Column('state', verbose_name='State')
    name = tables.Column('name', verbose_name='Name')

    class Meta(object):
        name = "container_docker"
        verbose_name = _("Container Docker")
```
 Ở đây, chúng ta định nghĩa một lớp **ContainerDockerTable** gồm 6 thuộc tính là `id` , `image`, `command`, `create`, `state` và `name`.
 
 Trong cột **create** ta có đoạn code: 
 

    filters=(filters_horizon.parse_isotime,filters_horizon.timesince_sortable)

Đoạn code này có tác dụng format lại thời gian. Ví dụ `2016-09-13 17:41:17` sẽ được format thành `5 days, 21 hours`.

Tiếp theo, trong file `views.py` ta tạo một lớp**Container** gồm các thuộc tính như sau:
```
class Container:
    def __init__(self, containerId, image, command, created, state, name):
        self.id = containerId
        self.image = image
        self.command = command
        self.created = created
        self.state = state
        self.name = name
```
Trong lớp **IndexView** chúng ta cần phương thức `get_data(self)` trả về một list các đối tương **Container**:
```
class IndexView(tables.DataTableView):
    # A very simple class-based view...
    template_name = 'custom_horizon/container/index.html'
    table_class = tbl_container.ContainerDockerTable
    page_title = _("Container")

    def get_data(self):
        # Add data to the context here...
        cli = Client(base_url='unix://var/run/docker.sock')
        containers = []
        
        for ct in cli.containers(all=True):
            # convert data
            created = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ct['Created']))
            name = ct['Names'][0][1:]
            
            containers.append(
                Container(ct['Id'][:12], ct['Image'], ct['Command'], created, ct['State'], name))
                
        return containers
```
Thông tin các container sẽ được trả về dưới dạng **dict**, ở đây ta cần convert lại 2 thuộc tính là `create` và `name`  để nội dung hiển thị lên bảng dễ hiểu hơn.
 
 Ta cũng cần có một `url` và một file `index.html` để có thể render được dữ liệu sang dạng bảng.  Các bạn xem code để biết thêm chi tiết.

3. Tạo actions cho table
-------
### 3.1 Action **"Create"**
