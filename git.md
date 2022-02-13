## git 

有没有什么办法将每次提交的时间自动更新显示在文档中，标识内容的时效性。

图片可以上传到gitee

#### 入门

使用git前，需要先建立一个仓库(repository)。

使用当前目录作为git本地仓库，需要先初始化。

```git
git init                # 初始化本地仓库
git init new            # 将指定目录new初始化为本地仓库
git add filename        # 添加新文件到暂存区
git commit -m "add file"   # 提交版本
git commit -a -m "changed some files"
# 将所有被修改或者已删除的且已经被git管理的文档提交到本地仓库。-a不会造成新文件被提交。
```

删除

git rm file
```git
git branch test     # 创建新的本地分支
git checkout test   # 更改当前分支到test
git merge test      # 合并当前分支与test分支
git branch -d test  # 删除test分支
```


### git教程

git安装配置
git工作流程
git工作区、暂存区和版本库
git创建仓库
git基本操作
git分支管理
git查看提交历史
git标签
git Github
git Gitee
git服务器搭建

同一个项目有两种地址方式，一种是https方式，一种是ssh方式．

https url可以直接有效打开网址，但是用户每次通过git提交的时候都要输入用户名和密码．
ssh url通过在github配置ssh key后，使我们在git提交代码时跳过验证过程，简化操作流程．

```git
https://github.com/zhudingsuifeng/restart.git
git@github.com:zhudingsuifeng/restart.git
```

```git
git config --global user.name "zhudingsuifeng"
git config --global user.email "your_email@example.com"
git config --list  # 查看当前git环境所有配置
```

### ssh key

生成ssh key并在github配置公钥．

` ssh-keygen -t ed25519 -C "your_email@example.com"`

复制~/.ssh/id_ed25519.pub内容到github中，setting->SSH and GPG keys．

```ssh
ssh -T git@github.com   # 测试是否成功配置ssh key.
```

之前已经是https链接，想要使用ssh提交，需要修改项目目录下.git文件夹下的config文件，将地址修改为ssh地址．


### github

github创建repository存储库的时候，最好创建一个空的，license也不要选，不然后面推送不成功。

总是显示远端branch超出local branch

The default branch has been renamed!

`main` is now named **master**

if you have a local clone, you can update it by running the following commands.


```git
git clone /path/to/repository      # 创建本地仓库克隆版本
git clone git@github.com:zhudingsuifeng/restart.git     # 创建远程仓库克隆版本
```

#### 工作流

本地仓库由git维护的三棵"树"组成。
工作目录，持有实际文件。

```git
git add <filename>   # 添加更改到暂存区
git add *
```

暂存区(Index,Stage)，缓存区域，临时保存改动。

```git
git commit -m "附加提交信息"   # 实际提交改动
```

HEAD，指向最后一次提交的结果。

#### 推送改动

将改动从本地仓库的HEAD推送到远程仓库。

`git push origin_repository_name branch_name`

#### 分支

#### 更新与合并


#### 标签


#### 替换本地改动


### github经常无法访问

域名()，又称网域，是有一串用点分割的名字组成的Internet上某一台计算机或计算机组的名称，用于在数据传输时对计算机的定位标识．

尽管IP地址能够唯一的标记网络上的计算机，但IP地址是一长串数字，不直观，而且用户记忆十分不方便，于是人们又发明了另一套字符型的地址方案，即所谓的域名地址．IP地址和域名是一一对应的，这份域名地址的信息存放在一个叫域名服务器(DNS,Domain name server)的主机内，使用者只需了解易记的域名地址，其对应转换工作就留给了域名服务器．域名服务器就是提供IP地址和域名之间的转换服务的服务器．

可以自己修改/etc/hosts文件

```vim
sudo vi /etc/hosts

# GitHub Start
140.82.113.3  github.com
140.82.114.20 gist.github.com
# GitHub End
```

/etc/hosts为了访问github.com，可以自己实现dns功能，在https://www.ipaddress.com中输入域名，得到对应的IP，在/etc/hosts中添加对应内容，后面网址有可能就能正常访问了．

```git
git branch -m main master
git fetch github
git branch github/master master
git remote set-head master -a
```

默认分支branch
main -> master

### gitee

需要在gitee创建远端仓库用于与本地git关联．

创建好仓库后，可以通过以下两共方式向仓库提交代码．

1. 先将仓库clone到本地，修改后再push到Gitee的仓库

git clone https://gitee.com/zhudingsuifeng/restart.git

修改代码后，在仓库目录下执行下面命令

```git
$ git add .                           # 将当前目录所有文件添加到git暂存区
$ git commit -m "my first commit "    # 提交并备注提交信息
$ git push origin master              # 将本地提交推送到远程仓库
# origin 是远程仓库名称，也可以叫其他名称，如gitee，master 是默认主分支
```

2. 本地初始化一个仓库，设置远程仓库地址后再做push

```git
$ git init
$ git remote add origin https://gitee.com/zhudingsuifeng/restart.git
$ git pull origin master         # 拉取远程仓库内容同步到本地仓库
$ git add .
$ git commit -m "第一次提交"
$ git push origin master
```

新建仓库时，如果在gitee平台远程仓库中已经存在readme或其他文件，而本地仓库初始化为空文件夹，这时提交可能会存在冲突．解决冲突需要选择是保留线上文件或者舍弃线上文件，如果舍弃线上文件，可以选择强制推送．

`$ git push origin master -f`

如果行要保留线上文件，需要先拉取远程仓库文件再重新推送．

`$ git pull origin master`

冲突的原因是线上存在本地未出现的文件，就是说在初次发生关联时，远程仓库有本地仓库没有的文件，github就会认为远程仓库处在分支的更超前位置，提交失败．

#### gitee仓库镜像管理(Gitee<->Github双向同步)

> 仓库镜像管理功能用于配置和管理仓库镜像，可以实现不同平台之间仓库分支，标签和提交信息的自动同步．
> Push镜像用于将Gitee的仓库自动镜像到GitHub.Pull镜像用于将GitHub的仓库镜像到Gitee.
> gitee仓库镜像管理的功能不是自动开通的，需要申请，符合要求的GVP项目或推荐项目才能开通此功能．
