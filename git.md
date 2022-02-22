## git 

git - the stupid content tracker

`git help git`

Git is a fast, acalable, distributed revision control system with an unusually rich command set that provides both high-level operations and full access to internals.

See gittutorial to get started, the see giteveryday for a useful minimum set of commands. The Git User's Manual has a more in-depth introduction.

After you mastered the basic concepts, you can come back to this page to learn what commands Git offers. You can learn more about individual Git commands with "git help command". gitcli manual page gives you an overview of the command-line command syntax.

### git - 简明指南

- 本地init方式创建新仓库

使用git前，需要先建立一个仓库(repository)。使用当前目录作为git本地仓库，需要先执行`git init`初始化。

- 通过clone的方式创建新仓库

```git
git clone -o gitee https://gitee.com/zhudingsuifeng/restart.git ant
```

- 工作流

本地仓库由git维护的三棵"树"组成。第一个是`工作目录`，他持有实际文件;第二个是暂存区(index)，就像个缓存区域，临时保存改动;最后是`HEAD`，指向最后一次提交的结果．

![git tree](https://www.runoob.com/manual/git-guide/img/trees.png)

工作目录，持有实际文件。

```git
git add <filename>   # 添加更改到暂存区
git add *
git commit -a -m "changed some files"
# 将所有被修改或者已删除的且已经被git管理的文档提交到本地仓库。-a不会造成新文件被提交。
```

暂存区(Index,Stage)，缓存区域，临时保存改动。

```git
git commit -m "附加提交信息"   # 实际提交改动到HEAD，但是还没有push到gitee/github远程仓库
```

HEAD，指向最后一次提交的结果。

-  推送改动

现有改动已经存储在本地仓库的HEAD，执行`git push`命令将改动推送到远程仓库。

`git push origin_repository_name branch_name`

如果不是通过clone创建的本地仓库，此时还没有关联远程仓库，可以使用
`git remote add origin_repository_name branch_name`
命令将本地仓库与远程仓库相关连，之后再push推送改动就可以了．

- 分支

分支使用来隔离不同开发路径的方式，创建仓库时，master是本地仓库默认分支．通常是在其他(dev)分支上开发，完成后再将功能分支合并到主分支上．

![git tree](https://www.runoob.com/manual/git-guide/img/branches.png)

```git
git checkout -b dev      # 创建一个dev分支，同时切换当前分支到dev分支
git checkout master      # 切换会master分支
git branch -d dev        # 删掉dev分支
git push gitee dev       # 如果不把dev分支推送到远程仓库gitee，dev分支就是本地私有的，对其他人是未知的
```

- 更新与合并

```git
git pull                 # 从远程仓库拉取更新到本地仓库，等价于本地分支获取(fetch)并合并(merge)远端改动．
git merge dev            # 合并dev分支到当前分支，也可以指定其他分支合并到当前分支
git diff master dev      # 查看不同分支之间的差异，方便处理冲突conflicts
```

- 标签

为软件发布创建标签，便于记忆与管理．

```git
git tag 1.0.0 id         # 创建提交内容的版本号，id是内容的对应ID
git log                  # 获取提交内容的ID
```

- 替换本地改动

```git
git checkout -- <filename>   # 使用HEAD中最新内容替换掉工作目录中的文件filename．已经添加到暂存区index的改动或者新文件都不受影响
git remote add gitee gitee git@gitee.com:zhudingsuifeng/ant.git
git fetch gitee <master>:<master>   # 获取服务器上最新版本
git reset --hard gitee/master       # 将本地主分支指向gitee/master，所有未提交commit的内容都会被丢弃掉
```


### common Git commands uesd in various situations

#### start a working area (see also: git help tutorial)

```git
	clone			Clone a repository into a new directory
	init 			Create an empty Git repository or reinitialize an existing one
```

有没有什么办法将每次提交的时间自动更新显示在文档中，标识内容的时效性。

### git教程

git安装配置
git工作流程
git工作区、暂存区和版本库
git创建仓库
git基本操作
git分支管理
git查看提交历史
git标签

### github/gitee配置

同一个项目有两种地址方式，一种是https方式，一种是ssh方式．

https url可以直接有效打开网址，但是用户每次通过git提交的时候都要输入用户名和密码．
ssh url通过在github配置ssh key后，使我们在git提交代码时跳过验证过程，简化操作流程．

```git
https://github.com/zhudingsuifeng/restart.git
git@github.com:zhudingsuifeng/restart.git
git config --global user.name 'zhudingsuifeng'
git config --global user.email '1002557401@qq.com'
git config --list  # 查看当前git环境所有配置
```

#### https



#### ssh key

生成ssh key并在github配置公钥．

` ssh-keygen -t ed25519 -C "your_email@example.com"`

复制~/.ssh/id_ed25519.pub内容到github中，setting->SSH and GPG keys．

```ssh
ssh -T git@github.com   # 测试是否成功配置ssh key.
```

之前已经是https链接，想要使用ssh提交，需要修改项目目录下.git文件夹下的config文件，将地址修改为ssh地址．

### 远程仓库分支与本地仓库分支冲突解决

当在gitee创建远程仓库的时候选择readme，本地init仓库的时候重新创建readme文件，push时被拒绝．

> 更新被拒绝，因为远程仓库包含本地尚不存在的提交．这通常是因为另外一个仓库已向该引用进行了推送．再次推送前，可能需要先整合远程变更．

**原因就是远程仓库在分支树上处于更前位置，远程仓库与本地仓库存在冲突．为了解决冲突，需要把远程仓库拉取到本地的其他分支，将远程仓库与本地仓库之间的冲突变为本地仓库不同分支之间的冲突，通过merge分支解决冲突．**

已创建远程仓库ant，默认远程分支master，创建本地仓库，并解决冲突．

```git
$ mkdir ant
$ cd ant
git init
git add readme.md
git commit -m '解决冲突'
git branch -a

* master

git remote -v
git remote add gitee git@gitee.com:zhudingsuifeng/ant.git   # Add a remote named <name> for the repository at <URL>.
git remote -v

gitee   git@gitee.com:zhudingsuifeng/ant.git(fetch)
gitee   git@gitee.com:zhudingsuifeng/ant.git(push)

git push gitee master
! [rejected]   master -> master (fetch first)

git fetch gitee master:dev   # 拉取gitee远程仓库repository的分支master到本地分支dev，会自动创建对应分支
git branch -a

  dev
* master
  remotes/gitee/master 

git diff dev   # 查看远程最新分支dev与本地分支master的区别
git merge dev  # 将当前分支master与dev分支合并

有可能会报错-> fatal:拒绝合并无关的历史  -> 这有可能是远程分支包含其他本地没有的文件所致

git merge dev --allow-unrelated-histories   # 解决无关历史问题
git add *      # 将合并产生的文件新版本提交到本地缓存
git commit -m '合并冲突'
git push gitee master   # 推送成功
git branch -d dev       # 删除临时分支
git branch -a           # dev分支已被删除

* master
  remotes/gitee/master 
```

### github

github创建repository存储库的时候，最好创建一个空的，license也不要选，不然与gitee混用推送有可能不成功。

目前(20220219)，git原生命令并不能在本地命令行直接创建github远程仓库，所以需要先创建github远程仓库．

**github提供了api，可以通过执行编写的脚本来创建github远程仓库．**

在github创建好远程仓库后，可以通过以下两种方式创建本地仓库，关联github远程仓库并推送提交

1. 将github远程仓库clone到本地后再push提交内容

```git
git clone /path/to/repository      # 创建本地仓库克隆版本
git clone git@github.com:zhudingsuifeng/restart.git     # 采用ssh链接方式创建远程仓库克隆版本
git clone git@github.com:zhudingsuifeng/restart.git bee # 指定目录
git clone -o github git@github.com:zhudingsuifeng/restart.git bee   # 指定远程仓库名称为github
git clone -o https://github.com/zhudingsuifeng/restart.git ant      # https链接方式
```

由于种族歧视的原因，github将原来远程仓库默认主分支名称由master改为main．

```git
git branch -a

* main
  remotes/github/HEAD -> github/main
  remotes/github/main

git remote -v

github  https://github.com/zhudingsuifeng/restart.git(fetch)
github  https://github.com/zhudingsuifeng/restart.git(push)
```

> 可以通过在github操作将默认主分支由main -> master
> Settings->Repositories->Repository default branch->(master) Update
> 该操作只能对修改以后创建的仓库repository产生作用，而对已经建立的仓库repository无影响．

> 为了将指定仓库repository默认分支branch修改为master，可以选中指定仓库repository，如restart
> zhudingsuifeng/restart->Settings->Branches->Default branch->Rename`main`to master

为了将本地clone的仓库与远程仓库相匹配，本地默认主分支也要由main->master

- 可以删除本地仓库重新clone远程仓库

```git
$ pwd 
/home/fly/ant
$ cd ..
$ rm -rf ant
$ git clone -o github https://github.com/zhudingsuifeng/restart.git ant
```

- 也可以在已clone本地仓库的基础上修改分支branch后重新关联远程仓库repository

```git
git branch -a

* main
  remotes/github/HEAD -> github/main
  remotes/github/main

git branch -m main master            # 重命名本地local分支名称main -> master
# -m, --move Move/rename a branch, together with its config and reflog.
git branch -a

* master
  remotes/github/HEAD -> github/main
  remotes/github/main

git fetch github                     # Download objects and refs from another repository
git branch -a

* master
  remotes/github/HEAD -> github/main
  remotes/github/main
  remotes/github/master

git branch -u github/master master   # -u <upstream>, --set-upstream-to=<upstream>
# git branch -u <upstream> <branchname>   # 制定本地分支branchname关联远程分支upstream
# Set up <branchname>'s tracking insformation so <upstream> is considered <branchname>'s upstream baranch.
# If no <branchname> is specified, then it defaults to the current branch.
git remote set-head master -a        # Sets the default branch for the named remote.
git branch -a

* master
  remotes/github/HEAD -> github/master   # github/HEAD set to master
  remotes/github/main
  remotes/github/master
```

#### 删除远程跟踪分支

```git
git branch -rl                   # -r, --remotes Combine with -l, --list to list the remote-tracking branches.

  github/HEAD -> github/master   # github/HEAD set to master
  github/main
  github/master
git branch -rd github/main       # 删除远程跟踪分支github/main
git branch -rl

  github/HEAD -> github/master   # github/HEAD set to master
  github/master
```

2. 本地初始化一个仓库，设置关联远程仓库地址后提交push内容

假设远程github仓库repository默认主分支已经修改为master

```git
$ mkdir ant
$ cd ant
$ echo "# test" >> README.md
git init
git add READMD.md
git commit -m "first commit"
git branch -a

* master        # 本地主分支默认为master，在提交commit之后才会创建，init时并不会创建分支

git remote add github https://github.com/zhudingsuifeng/restart.git
git push -u github master
```

#### github经常无法访问

域名，又称网域，是有一串用点分割的名字组成的Internet上某一台计算机或计算机组的名称，用于在数据传输时对计算机的定位标识．

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

### gitee

需要在gitee创建远端仓库用于与本地git关联．

创建好仓库后，可以通过以下两种方式向仓库提交代码．

1. 先将仓库clone到本地，修改后再push到Gitee的仓库

```git
git clone https://gitee.com/zhudingsuifeng/restart.git                # 克隆远程仓库到本地restart
git clone https://gitee.com/zhudingsuifeng/restart.git ant            # 克隆到指定目录ant
git clone -o gitee https://gitee.com/zhudingsuifeng/restart.git ant   # 指定远程仓库名称为gitee
```

修改代码后，在仓库目录下执行下面命令

```git
$ touch readme.md                   　
git add .                           # 将当前目录所有文件添加到git暂存区
git commit -m "my first commit "    # 提交并备注提交信息
git push origin master              # 将本地提交推送到远程origin仓库的master分支
origin 是默认远程仓库名称，也可以叫其他名称，如gitee，master 是默认主分支名称
```

2. 本地初始化一个仓库，设置远程仓库地址后再做push

```git
git init
git remote add gitee https://gitee.com/zhudingsuifeng/restart.git
# 为了区分与github默认远程仓库名称也叫origin，我们将gitee远程仓库名称命名为gitee
git pull gitee master         # 拉取远程仓库内容同步到本地仓库
git add .
git commit -m "第一次提交"
git push giee master
```

新建仓库时，如果在gitee平台远程仓库中已经存在readme或其他文件，而本地仓库初始化为空文件夹，这时提交可能会存在冲突．解决冲突需要选择是保留线上文件或者舍弃线上文件，如果舍弃线上文件，可以选择强制推送．

`git push gitee master -f`

如果行要保留线上文件，需要先拉取远程仓库文件再重新推送．

`git pull gitee master`

冲突的原因是线上存在本地未出现的文件，就是说在初次发生关联时，远程仓库有本地仓库没有的文件，gitee,github远程仓库就会认为远程仓库分支处在分支的更超前位置，提交失败．

#### gitee仓库镜像管理(Gitee<->Github双向同步)

> 仓库镜像管理功能用于配置和管理仓库镜像，可以实现不同平台之间仓库分支，标签和提交信息的自动同步．
> Push镜像用于将Gitee的仓库自动镜像到GitHub.Pull镜像用于将GitHub的仓库镜像到Gitee.
> gitee仓库镜像管理的功能不是自动开通的，需要申请，符合要求的GVP项目或推荐项目才能开通此功能．

### 使用脚本创建github/gitee远程仓库

命令行创建gitee远程仓库的本质是使用`curl`工具与https://gitee.com交互，模拟人的点击操作．

使用命令行创建gitee远程仓库需要用到私人令牌，生成步骤如下:

gitee->设置->安全设置->私人令牌->提交(保存好私人令牌)

### git服务器搭建
