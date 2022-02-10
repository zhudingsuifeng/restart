## ssh

### sshd

安装

service需要root用户

```sshd
service sshd status  # 查看sshd服务状态
service sshd stop    # 停止sshd服务
service sshd start   # 启动sshd服务
service sshd restart # 重启sshd服务
```


### ssh 登录linux

ssh <username>@<hostname or IP address>

username 想要登录的用户名
hostname or IP address 为linux实例自定义域名或者公网IP.

没有配置密钥的话，登录linux需要输入登录用户的密码．


### ssh密钥

公钥，私钥


查看ssh密钥
linux下的ssh密钥通常存储在~/.ssh目录，不同的算法生成的密钥名字不同，但是都会有一对公钥和私钥．

使用rsa算法生成的密钥，id_rsa.pub存储公钥，id_rsa存储私钥．



### 生成ssh密钥

```ssh
ssh-keygen -t ed25519 -C "your_email@example.com"
# Generating public/private ed25519 key pair ...
```

生成的密钥同样存储在~/.ssh目录，id_ed25519.pub存储公钥，id_ed25519存储私钥．

在gitee部署公钥后，可以在终端()中输入以下命令测试ssh联通性．

｀ssh -T git@gitee.com`

### 配置ssh自动断开时间

客户端链接腾讯云服务，长时间无操作自动断开链接解决办法．

```vim
vi /etc/ssh/sshd_config    # sshd 配置文件

ClientAliveInterval 0      # 服务端每隔多少秒向客户端发送一个心跳数据
ClientAliveCountMax 3      # 客户端多少次没有相应，服务器自动断掉链接
```

```sshd
ClientAliveInterval 60      # 服务端每隔多少秒向客户端发送一个心跳数据
ClientAliveCountMax 180     # 客户端多少次没有相应，服务器自动断掉链接
```

重启sshd服务配置才能生效

`service sshd restart`

