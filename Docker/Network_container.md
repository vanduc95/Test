Tài liệu này cung cấp cái nhìn tổng quát về networking trong contrainer. Mô tả các network được tạo mặc định và làm thế nào để tự tạo một network (user-defined networks). Ngoài ra tài liệu còn hướng dẫn cách kết nối giữa Docker container và host, giữa các container với nhau.
# Default Networks
Khi cài đặt Docker, nó sẽ tự động tạo ra 3 networks. Bạn có thể liệt kê ra các network này bằng cách sử dụng lệnh ```docker network ls```
```sh
$ docker network ls
NETWORK ID          NAME                DRIVER
7fca4eb8c647        bridge              bridge
9f904ee27bf5        none                null
cf03ee007fb4        host                host
```
Mặc định, khi tạo một container, Docker daemon kết nối chúng với network ```bridge```. Tuy nhiên ta có thể tự thiết lập network với câu lệnh ```docker run --net=<NETWORK>```.
## None Network
Các container thiết lập network này sẽ không được cấu hình mạng. Điều này có ích khi container đó không cần đến mạng hoặc nếu bạn muốn tự mình thiết lập mạng cho nó. 
## Host Network
Nếu dùng ```--net=host``` thì các container sẽ sử dụng mạng của máy chủ, điều này có thể sẽ gây nguy hiểm. Nó cho phép bạn có thể thay đổi ```host network``` ở trong container. Và khi bạn chạy ứng dụng với quyền root ở trong container, nó sẽ có nguy cơ điều khiển từ xa tới các máy chủ thông qua các container. 

Nói chung, ta không nên sử dụng cấu hình này vì lí do an ninh, nhưng nó có thể hữu ích khi ta cần hiệu suất mạng tốt nhất bởi vì nó là nhanh nhất.
## Bridge Network
Network ```bridge``` là default network trong Docker.

Chúng ta có thể xem thông tin chi tiết về network ```bridge``` bằng cách sử dụng câu lệnh:
```sh
$ docker network inspect bridge
```
Network ```bridge``` được đại diện bởi ```docker0``` trong cấu hình ```ifconfig```. Khi thêm một container, chúng sẽ có một địa chỉ IP có cùng dải mạng với ```docker0```
```sh
$ ifconfig

docker0   Link encap:Ethernet  HWaddr 02:42:47:bc:3a:eb  
          inet addr:172.17.0.1  Bcast:0.0.0.0  Mask:255.255.0.0
          inet6 addr: fe80::42:47ff:febc:3aeb/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:9001  Metric:1
          RX packets:17 errors:0 dropped:0 overruns:0 frame:0
          TX packets:8 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:1100 (1.1 KB)  TX bytes:648 (648.0 B)
```
Điều này cho phép các container có thể giao tiếp được với máy host cũng như giao tiếp được với các container khác trên cùng 1 host.

Để xem thông tin chi tiết về một network, ta dùng lệnh ```docker network inspect <name_network>```, nó sẽ trả về thông tin dưới dạng 1 file json.

Với các ```default network```, chúng ta chỉ có thể liệt kê và inspect mà không thể xóa chúng. Chúng là mặc định khi cài Docker. Tuy nhiên có thể tự tạo một ``` user-defined networks```, nó có thể remove khi bạn không cần đến nó nữa.
# User-defined networks
