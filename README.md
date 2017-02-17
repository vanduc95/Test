Introduction to networking in OpenStack
=========



#1. Basic networking

##Ethernet
Ethernet là một trong những công nghệ phổ biến nhất để tạo ra mạng cục bộ (LAN). 

Trong mô hình OSI, Ethernet là giao thức ở tầng **datalink** mô tả cách thức để các thiết bị mạng có thể định dạng dữ liệu và truyền chúng tới các thiết bị khác trên cùng một mạng.

 Mỗi thiết bị trên mạng Ethernet được định danh duy nhất  bởi địa chỉ MAC. Nhờ địa chỉ MAC, hai thiết bị giao tiếp được với nhau bằng cách gửi đi các *frame* đã đóng gói địa chỉ MAC nguồn và địa chỉ MAC đích và chúng được chuyển tiếp nhờ thiết bị mạng được gọi là switch.

##VLANs
VLAN ( virtual LAN) là một kĩ thuật mạng cho phép chia một miền quảng bá vật lí ra thành nhiều mạng cục bộ độc lập nhau.  Mỗi mạng cục bộ được đặc trưng bởi một định danh, đó là VLAN ID. Cụ thể, khi sử dụng VLAN, nếu 2 máy cùng kết nối tới cùng một switch nhưng được định nghĩa ở 2 mạng VLAN khác nhau thì không thể giao tiếp được với nhau.  

Tham khảo chi tiết [tại đây](https://github.com/cloudcomputinghust/openstack-manual/blob/master/Introduction-to-OpenStack-networking/OpenStack-networking-Layer2-Introduction.md)

##ARP 

Trong hệ thông mạng có 2 loại địa chỉ được gán cho một máy tính là địa chỉ IP và địa chỉ MAC.  Trong thực tế, các card mạng chỉ có thể hiểu và liên lạc với nhau bằng địa chỉ MAC. Vì vậy, để các máy có thể hiểu và liên lạc với nhau trong môi trường mạng, cần có một cơ chế diễn giải địa chỉ giữa IP và MAC. Đó là giao thức **Address Resolution Protocol** viết tắt là  **ARP**

**Cơ chế của ARP như sau:** 

Giả sử máy A có địa chỉ IP là **192.168.1.5/24** và muốn gửi một packet tới máy B với địa chỉ IP là **192.168.1.7**.

 - Đầu tiên, máy A sẽ gửi một ARP request bao gồm địa chỉ MAC của máy A
   và địa chỉ IP của máy B.
 - Vì là gói tin broadcast nên các máy trên mạng sẽ nhận được gói tin và
   xử lí. Máy B nhận được request  đúng là IP của nó thì sẽ gửi lại cho
   máy A một response chứa địa chỉ MAC của máy B.
 - Lúc này máy A đã có địa chỉ MAC của máy B và máy A có thể bắt đầu
   truyền gói tin cho máy B.

##DHCP

DHCP (Dynamic Host Configuration Protocol) là giao thức cho phép cấp phát địa chỉ IP một cách tự động cho clients. Mục đích quan trọng nhất là tránh trường hợp hai máy tính khác nhau lại có cùng địa chỉ IP.

DHCP gồm 2 thành phần chính là **DHCP client** và **DHCP server**. Trong đó DHCP client là một thiết bị mạng yêu cầu địa chỉ IP còn DHCP server có nhiệm vụ lắng nghe và cấp phát IP cho client.

Quá trình cấp phát IP được mô tả như hình dưới đây 

![enter image description here](https://camo.mybb.com/e01de90be6012adc1b1701dba899491a9348ae79/687474703a2f2f7777772e6a71756572797363726970742e6e65742f696d616765732f53696d706c6573742d526573706f6e736976652d6a51756572792d496d6167652d4c69676874626f782d506c7567696e2d73696d706c652d6c69676874626f782e6a7067)

 - DHCP client gửi một discover ("Tôi là client có địa chỉ MAC
   **08:00:27:b9:88:74**, tôi cần một địa chỉ IP").
 - DHCP server gửi một offer ("OK **08:00:27:b9:88:74**, tôi sẽ gửi cho
   bạn địa chỉ IP **10.10.0.112**").
 - DHCP client gửi một request ("Tôi đồng ý lấy địa chỉ này").
 - DHCP server gửi một acknowledgement ("OK, IP  **10.10.0.112 ** là của
   bạn").

Trong OpenStack, phần mềm thứ 3 có tên là [dnsmasq](http://www.thekelleys.org.uk/dnsmasq/doc.html)  được dùng để implement dịch vụ DHCP server.

2. Network components
--------------------------
##Switch

Switch thông thường được biết đến như là một "thiết bị chuyển mạch". Nó là thiết bị mạng thuộc tầng 2 trong mô hình OSI (Data Link Layer). Nó có thể coi là một Bridge có nhiều cổng. Switch chuyển tiếp các frame dựa trên địa chỉ MAC. Switch tập trung các kết nối và quyết định chọn đường dẫn để truyền dữ liệu hiệu quả. Frame được chuyển mạch từ cổng input đến cổng output và đến được node đích như mong muốn

![enter image description here](https://vietadsgroup.vn/Uploads/files/switch-lam-gi.jpg)

##Router
Router là thiết bị mạng thuộc tầng 3 trong mô hình OSI (Network layer). Nó còn được gọi là "thiết bị định tuyến hoặc bộ định tuyến" có chức năng chuyển các gói dữ liệu (packet) qua một liên mạng đến các đầu cuối dựa trên địa chỉ IP thông qua một tiến trình gọi là định tuyến.

![enter image description here](http://vnreview.vn/image/14/69/73/1469738.jpg?t=1448523262236)
