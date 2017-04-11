Linux Bridge
========
Bài viết note lại các kiến thức tìm hiểu được về Linux-bridge

# Linux Bridge – The Basics

Nguyễn Văn Đức 

Linux bridge là một phần mềm đươc tích hợp vào trong nhân Linux để giải quyết vấn đề ảo hóa phần network trong các máy vật lý. Mặc dù được gọi là bridge, nhưng thực chất linux-bridge tạo ra một switch ảo, sử dụng với ảo hóa KVM/QEMU để các VMs có thể kết nối được với nhau cũng như kết nối được ra bên ngoài.

Một linux-bridge có thể được tạo, xóa và quản lí nhờ command line tool được gọi là **brctl**. Để sử dụng **brctl** trên Ubuntu hoặc Debian , chúng ta cần cài package sau: 

	$ sudo apt-get install bridge-utils

Chúng ta sẽ tìm hiểu một số command line cơ bản của **brctl** trong phần sau.

#The Simple Use Case
Như chúng ta đã biết, khi tạo một máy ảo mới, có nhiều options cấu hình network cho máy ảo. Một trong hai options phổ biến được sử dụng đó là `bridge networking` và `network address translation (NAT)`. Vậy sự khác nhau của 2 options này là gì?

![](/home/vanduc/Documents/Github/OpenStack_Network/img/bridge_vs_NAT.png) 

Nhìn vào hình trên, đường thẳng cạnh "bức tường lửa" đại diện cho external network (mạng bên ngoài). Vòng tròn màu đỏ đại diện cho switch ảo sử dụng NAT. Khi sử dụng NAT, các VMs sẽ không được cấp địa chỉ của external network, thay vào đó nó sẽ được cấp một private ip từ DHCP server. Các VMs có thể kết nối được với các host trên external network nhưng ngược lại các host trên external lại không thể tạo kết nối với các VMs được. 

Để giải quyết nhược điểm này, chúng ta có thể sử dụng linux-bridge.

Bây giờ chúng ta sẽ tìm hiểu sâu hơn một chút về linux bridge bằng cách nhìn vào một use case cơ bản sau:  Chúng ta sẽ tạo một VM trên một host sử dụng KVM. Máy ảo này sẽ được cấu hình với một card mạng ảo (vNIC). Để VM có thể giao tiếp được với các host trên external network và ngược lại, chúng ta sẽ phải nối vNIC của VM với card mạng vật lí eth0 của host. Việc này sẽ được hỗ trợ bởi linux bridge. Hình dưới là mô hình mà chúng ta cần đạt được.

![](/home/vanduc/Documents/Github/OpenStack_Network/img/Linux-Bridge-Simple-UseCase.png) 



























