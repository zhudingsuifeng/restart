## git 

git - the stupid content tracker

`git help git`

Git is a fast, acalable, distributed revision control system with an unusually rich command set that provides both high-level operations and full access to internals.

See gittutorial to get started, the see giteveryday for a useful minimum set of commands. The Git User's Manual has a more in-depth introduction.

After you mastered the basic concepts, you can come back to this page to learn what commands Git offers. You can learn more about individual Git commands with "git help command". gitcli manual page gives you an overview of the command-line command syntax.

git是一个内容寻址文件系统(content addressable file system)．git的核心部分是一个简单的键值对数据库(key-value data store).

可以向数据库插入任意类型的内容，并返回一个键值，通过该键值可以再次检索该内容．这些数据全部存储在objects目录里．

key是一个hash,hash前两个字符用于命名子目录，余下38个字符则用作文件名．

### git tutorial

**所有版本控制系统只能跟踪文本文件的改动**

Git是一个分布式版本控制系统，区别于客户端-服务器式的集中式版本控制系统.

Github就是一个方便交换修改而非必须的"中心服务器"．

.git目录中，objects目录存储所有数据内容(hash)，refs目录存储指向数据(分支)的提交对象的指针(commit hash)，HEAD文件指示目前被检出的分支，index文件保存暂存区信息(git ls-files --stage).

### git配置

Git提供了一个git config工具，用来配置或读取相应的工作环境变量．

- /etc/gitconfig:对系统中所有用户都普遍适用．git config --system 读写的就是这个文件．

- ~/.gitconfig:适用于当前用户．git config --global 读写的就是这个文件．

- .git/config:适用于当前项目．

> .git/config,~/.gitconfig,/etc/gitconfig三个文件影响范围由小到大，优先级由大到小．

```git
git config --global user.name 'zhudingsuifeng'
git config --global user.email '1002557401@qq.com'
git config --list  # 查看当前git环境所有配置
```

### 创建版本库

1. 本地init方式创建新仓库

使用git前，需要先建立一个仓库(repository)。使用当前目录作为git本地仓库，需要先执行`git init`初始化。

git init后，Git仓库会生成一个.git目录，它包含了资源的所有元数据．

2. 通过clone的方式创建新仓库

```git
git clone git@github.com:zhudingsuifeng/restart.git     # 采用ssh链接方式创建远程仓库克隆版本
git clone git@github.com:zhudingsuifeng/restart.git ant # 指定目录
git clone -o github git@github.com:zhudingsuifeng/restart.git ant   # 指定远程仓库名称为github
git clone -o https://github.com/zhudingsuifeng/restart.git ant      # https链接方式
git clone -o gitee https://gitee.com/zhudingsuifeng/restart.git ant
```

### 工作区域和文件状态(版本管理)

#### 工作区域

git本地有三个工作区域:工作目录(working directory)，暂存区(stage/index)，本地仓库(repository/git directory)．如果加上远程的git仓库(remote repository)就可以分为四个工作区域．

![git tree](https://www.runoob.com/manual/git-guide/img/trees.png)

使用`git init`新建仓库之后，当前目录就是工作区(working directory).工作区下的隐藏目录.git是版本库/本地仓库(repository).本地仓库中的index文件(.git/index)就是暂存区(index/stage).版本库中还包含git自动创建的第一个分支master，以及指向master的指针/游标(HEAD).

git四个区域，工作目录(working directory)，暂存区(index/stage)，资源库(repository/git direcotry)，远程仓库(remote directory)是可以互相转换的．

![git directory](https://www.runoob.com/wp-content/uploads/2015/02/git-command.jpg)

- 工作目录(workspace/working directory)，执行`git init`的当前目录，实际持有文件。

在工作目录中新建文件，如果没有通过`git add <file>`将文件改动添加到暂存区index/stage，此时文件处于未跟踪状态，某些git对于文件的管理是不能实现的。

```git
git status           # 查看仓库当前状态
git diff             # Changes in the working tree not yet staged for the next commit.工作区内容与暂存区比较
git diff filename    # 查看缓存区index/stage与工作区filename文件差别
git diff --cached    # Changes between the index and your last commit.暂存区改动与版本库内容比较
git diff HEAD        # Changes in the working tree since your last commit.工作区内容与版本库内容比较
git diff HEAD HEAD~1 # 当前commit和前一个commit的比较
git add <file>       # 添加指定file文件修改更改到暂存区
git add *            # 添加所有修改和新增文件到暂存区index/stage
git commit -a -m "changed some files"
# 将所有被修改或者已删除的且已经被git管理的文档提交到本地仓库。-a不会造成新文件被提交。
git clean            # Remove untracked files from then working tree.
git mv file xxx      # Move or rename a file, a directory, or a symlink.直接mv被git认为是删除原有文件后添加一个新文件
```

- 暂存区(Index,Stage)，缓存区域，临时保存改动，保存在.git/index文件中．

```git
git commit -m "附加提交信息"   # 实际提交改动到HEAD，但是还没有push到gitee/github远程仓库
# 把暂存区的修改提交到当前分支，提交之后暂存区就被清空了
git ls-files --stage           # Show staged contents' mode bits, object name and stage number in the output.
git ls-files -s                # --stage 显示暂存区内容的对象名称
git ls-files -c                # --cached 显示缓存的文件
git ls-files -d                # --deleted 显示已删除的文件
git ls-files -m                # --modified 显示已修改的文件
git ls-files -k                # --killed 显示文件系统需要删除的文件
git reset -- <file>            # 回退所有暂存区file的内容，暂存区该file所有add全部回退，并不改变file文件内容
git checkout .                 # 使用暂存区全部内容覆盖工作目录
git checkout -- <file>         # 使用暂存区file修改覆盖工作目录中的file，用来撤销本地修改，会改变file文件实际内容
git rm --cached <file>         # 删除暂存区文件/回退最后一次add的file内容，工作区文件不改变
git rm <file>                  # 将文件从暂存区和工作区中删除，已经被提交commit到本地仓库的文件被删除，并将删除动作作为改动添加到暂存区index/stage，会有提示可以通过`git restore --staged`恢复
git rm -f <file>               # 如果删除前修改过并且已经添加到暂存区的话，需要使用`-f`强制删除
git restore --staged <file>    # 将暂存区的文件从暂存区回撤，但是不会更改文件内容
git restore <file>             # 撤销(在工作空间但不在暂存区)文件的更改，会更改文件内容
```

- 本地仓库(repository)位于.git目录，除index文件表示的暂存区index/stage，还有的其他文件和对象，用于存储commit的版本和一系列指针/游标.

```git
git commit -m "版本信息"       # 将暂存区stage/index的内容提交到版本库repository
git commit -a -m "版本信息"    # 将已跟踪文件的修改直接提交到版本库repository
git commit -v                  # 显示提交时所有改动diff信息，并不真的提交
git commit --amend             # Replace the tip of the current branch by creating a new commit.将需要修改的内容git add到暂存区，--amend会修改最近一次commit，而不是新增一个commit，index中的内容也会一起commit
git reset HEAD                 # git reset defaults to HEAD，使用HEAD覆盖暂存区index/stage内容，文件内容不受影响
git reset --hard HEAD@{2}      # 撤销并删除相应的更新
git reset --hard gitee/master  # 将本地主分支指向gitee/master，所有未提交commit的内容都会被丢弃掉
git reset --soft HEAD@{3}      # 撤销相应更新，把这些更新的内容放到stage中
git reset HEAD <file>          # 指定文件file
git checkout HEAD .            # 使用commit提交的HEAD内容覆盖工作目录和暂存区
git checkout HEAD <file>       # 使用commit提交的HEAD内容覆盖工作目录file文件与暂存区file，会变更文件内容
git checkout -- <file>         # 使用暂存区file覆盖工作目录file文件，已添加到暂存区index/stage的改动不会被覆盖
git revert <SHA1>              # 回滚到指定提交commit的内容，通常会造成冲突conflict,需要解决冲突后，--continue
```

`HEAD`可以指向分支，也可以指向提交commit，存储在.git/HEAD．当指向branch时执行commit,checkout和merge等都会导致HEAD移动，当不指向branch而指向提交commit时，HEAD会处在detached分离/游离状态．

`HEAD` names the ref that you commit to repository. In most cases it's probably refs/heads/master.

```git
vi .git/HEAD
ref: refs/heads/master         # HEAD指向master分支，指针/游标
vi .git/refs/heads/master      # master分支最新提交的commit(40位sha-1值)

git checkout -b dev            # Create a new branch named dev and 切换当前分支为dev分支
git branch -a
* dev                          # checkout dev后，HEAD指向dev分支，表现为dev分支之前有星号
  master

git log
commit id (HEAD -> dev)        # 通过git log也能看出HEAD指向dev分支
```

`ORIG_HEAD`存放commit。当进某些危险操作时，如reset,merge或者rebase,git会将HEAD指针原来指向的commit对象的sha-1值保存在.git/ORIG_HEAD文件中。

```git
git reset --hard ORIG_HEAD     # 可以回退到危险操作之前状态
```

`FETCH_HEAD`表示某个branch在服务器上的最新状态。执行过fetch操作的项目都会存在.git/FETCH_HEAD文件，文件中的每一行对应于远程服务器上的一个分支。当前分支指向的FETCH_HEAD就是文件第一行对应的分支。

`detached HEAD` 当执行`git checkout commit`的时候，也就是指向提交，会变为detached(分离的) HEAD的状态。

```git
git log                        # show commit logs
git log --graph                # 以图形化的方式显示提交历史关系
git blame <file>               # show what reision and author last modified each line of a line.按文件查看历史记录
git log --oneline --graph --all   # 以图的方式显示分支历史
git reflog　　　　　　　　　　 # 显示HEAD移动历史，查看分支日志
git reflog --online            # 以简介的方式显示HEAD变动历史(每一行代表一次移动)
git checkout fed2b51(sha-1值)  # 将当前位置切换为某次提交
git branch -a 

* (HEAD detached at fed2b51)   # HEAD移动到某次提交
  master

git checkout -b dev            # 从某次提交创建分支branch，分叉
```

- 推送/获取远程版本(push/fetch/clone/pull)

现有改动已经存储在本地仓库的HEAD，执行`git push`命令将改动推送到远程仓库。

`git push origin_repository_name branch_name`

如果不是通过clone创建的本地仓库，此时还没有关联远程仓库，可以使用
`git remote add origin_repository_name branch_name`
命令将本地仓库与远程仓库相关连，之后再push推送改动就可以了．

```git
git remote               # 列出所有远程主机

gitee
github
git remote show gitee    # 显示远程主机详细信息

* 远程 gitee
  获取地址：git@gitee.com:zhudingsuifeng/restart.git
  推送地址：git@gitee.com:zhudingsuifeng/restart.git
  HEAD 分支：master
  远程分支：
    master 已跟踪
  为 'git push' 配置的本地引用：
    master 推送至 master (最新)
git remote rename <gitee> <gitdev>   # 修改远程主机名
git branch -r            # 查看远程分支

  gitee/master
  gitee/HEAD -> gitee/master
git remote -v            # 显示远程网址

gitee  git@gitee.com:zhudingsuifeng/restart.git (fetch)
gitee  git@gitee.com:zhudingsuifeng/restart.git (push)

git remote rm gitee                 # remove
git remote remove gitee             # 删除本地指定的远程地址
git remote add gitee git@gitee.com:zhudingsuifeng/restart.git  # 关联新的远程仓库
git remote set-head gitee master    # Sets or deletes the default branch for the named remote.
git fetch gitee master              # 将远程仓库gitee的分支master内容拉取到本地仓库
git push gitee master    # 将本地版本库改动推送到远程版本库gitee的master分支
git clone -o gitee git@gitee.com:zhudingsuifeng/restart.git ant   # clone 远程版本库到本ant目录，并设置远程版本库为gitee
git pull gitee master    # merge into the current branch the remote repository gitee and branch master
git pull                 # 从远程仓库拉取更新到本地仓库，等价于本地分支获取(fetch)并合并(merge)远端改动．
git fetch gitee          # 下面两条命令效果等同于上面一条
git merge gitee/master
git fetch gitee <master>:<dev>   # 获取远程库gitee的master分支到本地dev分支
```

`git fetch`是将远程主机的最新内容拉到本地，用户再检查了以后决定是否合并到本地分支中。

`git pull`将远程主机的最新内容拉取到本地后直接合并，即：`git pull = git fetch + git merge`，这样可能会产生冲突，需要手动解决。

#### 文件状态

与工作区域相对应的就是文件状态，文件状态的转变也就意味着文件在工作区域中的移动．

`git status <file>`用于查看file文件当前状态．

![file status](https://git-scm.com/book/en/v2/book/02-git-basics/images/lifecycle.png)

- 未跟踪(untracked)，文件在文件夹中，但是并没有加入到git库，不参与版本控制．通过`git add`状态变为stage.

- 未修改(unmodify)，文件已经入库，未修改，即版本库中文件commit内容与当前文件内容一致．这种类型的文件有两种去处，如果被修改，变为modified，如果使用`git rm`移出版本库，则成为untracked文件，其实文件被删除了．

- 已修改(modified)表示修改了文件，并未做其他操作．这个文件有两个去处，通过`git add`可进入暂存staged状态，使用`git checkout`则丢弃修改，返回到unmodify状态，`git checkout`即从库中取出文件，覆盖当前修改．

- 已暂存(staged)表示对已修改文件的当前版本做了标记，使之包含在下次提交中．执行`git commit`则将修改同步到库中，这时库中的文件和本地文件又变为一致，文件为unmodify状态．执行`git reset HEAD <file>`则取消暂存，文件状态变为modified.

`git rm --cached <file>`直接从暂存区删除文件，工作去不做改变，文件状态变为untracked

![change file status](https://images2017.cnblogs.com/blog/63651/201709/63651-20170909091456335-1787774607.jpg)

### 分支管理

分支使用来隔离不同开发路径的方式，创建仓库时，master是本地仓库默认分支．通常是在其他(dev)分支上开发，完成后再将功能分支合并到主分支上．

git分支本质上是指向提交对象commit object的可变指针，默认分支是master，多次提交后，得到指向最后提交对象的master分支。master分支会在每次提交时自动向前移动。HEAD是指向分支(指针)的指针，随分支移动。

![git tree](https://www.runoob.com/manual/git-guide/img/branches.png)

```git
git branch               # 列出本地分支
git branch -r            # 列出远程分支
git branch -a            # 列出所有分支
git branch -v            # --verbose show shaq and commit subject line for each head, along with relationship to upstream branch.
git branch dev           # 创建分支dev
git branch dev <commit>  # 创建分支dev指向特定commit快照
git branch --track <branch> <remote-branch>   # 创建分支并与制定的远程分支建立追踪关系
git checkout -b dev gitee/dev                 # 在远程分支的基础上创建本地分支
git branch --set-upstream-to=gitee/dev dev    # 指定本地dev分支与远程gitee/dev分支的关联
git checkout dev         # 切换分支到dev
git checkout -b dev      # 创建一个dev分支，同时切换当前分支到dev分支
git checkout master      # 切换回master分支
git checkout -           # 切换到上一个分支
git diff master dev      # 查看不同分支之间的差异，方便处理冲突conflicts
git merge dev            # 合并dev分支到当前分支，快进式合并(fast-farward merge)，会直接将master分支指向合并分支，会丢失分支信息
git cherry-pick <commit> # 选择一个提交commit，合并进当前分支
git merge dev --no-ff -m "merge with no-ff" dev   # --no-ff禁用Fast forward模式，-m合并时产生一个新commit.
git branch -d dev        # 删掉dev分支
git push gitee --delete <branch>   # 删除远程分支
git branch -dr <remote/branch>     # 同上
git push gitee dev       # 如果不把dev分支推送到远程仓库gitee，dev分支就是本地私有的，对其他人是未知的
git rebase               # Reapply commits on top of another base tip
```

![branch分叉](http://gitbook.liuhui998.com/assets/images/figure/rebase1.png)

git提交分叉后，可以用pull命令将分支上的修改拉下来并且与当前修改合并，结果看起来就像一个新的"合并提交"(merge commit).

![git pull merge commit](http://gitbook.liuhui998.com/assets/images/figure/rebase2.png)

如果想让mywork分支历史看起来像是没经过合并，是线性到当前的，可以使用`git rebase`.可以将mywork分支里的提交commit保存为补丁patch存储到.git/rebase目录，然后将mywork分支更新到最新的origin分支，并把补丁应用到mywork分支上，原来的mywork分支里的commit将变为分离的。

```git 
git switch mywork
git rebase origin
git rebase --continue   # 解决完冲突后继续提交commit
git rebase --abort      # 终止当前的rebase
```

![git rebase](http://gitbook.liuhui998.com/assets/images/figure/rebase3.png)

使用`git gc`垃圾收集命令，那些被丢弃的(detached)的提交就会被删除。

![git gc](http://gitbook.liuhui998.com/assets/images/figure/rebase4.png)



每次提交，git都把他们串成一条时间线，这条时间先就是一个分支．git默认分支master叫做主分支．HEAD不是指向提交，而是指向master，master才是指向提交，HEAD指向的是当前分支．

开始时，master分支是一条线，git用master指向最新的提交，再用HEAD指向master，就能确定当前分支，以及当前分支的提交点．

![branch_master](https://img2018.cnblogs.com/blog/63651/201809/63651-20180920210647291-1528543055.png)

每次提交，master分支都会向前移动一步，随着不断提交，master分支的线也越来越长．

![branch_commit](https://img2018.cnblogs.com/blog/63651/201809/63651-20180920210256578-751843766.gif)

`git checkout -b dev` 创建dev分支，指向master相同的提交，再把HEAD指向dev分支．

![branch_dev](https://cdn.liaoxuefeng.com/files/attachments/919022363210080/l)

使用`git checkout <branch>`切换分支，`git checkout -- <file>`撤销修改，容易混淆，更推荐使用switch命令切换分支．

```git
git switch -c dev     # --create Create a new branch named dev before switching to the branch.
git switch dev        # 切换到已有分支
```

`git commit -m 'D'` 对工作区的修改提交后，dev指针往前移动，而master指针不变．

![dev_commit](https://cdn.liaoxuefeng.com/files/attachments/919022387118368/l)

```git
git checkout master   # 先切换到master分支
git merge dev         # 将dev分支合并到master分支
```

![branch_merge](https://cdn.liaoxuefeng.com/files/attachments/919022412005504/0)

合并分支之默认会采用`Fast forward`模式，这种模式，将dev分支合并到master分支后删除dev分支，会丢失掉dev分支信息．

可以通过`--no-ff`方式强制禁用`Fast forward`模式，git就会在merge时生成一个新的commit，从分支历史上就可以看出分支信息．

```git 
git switch -c dev
git add readme.md
git comit -m "add merge"
git switch master
git merge --no-ff -m "merge with no-ff" dev   # -m commit描述
git log --graph --pretty=oneline
```

![merge --no-ff](https://cdn.liaoxuefeng.com/files/attachments/919023225142304/0)

`git branch -d dev` 删除dev分支就是吧dev指针给删掉，删掉dev分之后又回到只剩下一条master分支．

![branch_delete](https://cdn.liaoxuefeng.com/files/attachments/919022479428512/0)

master分支是非常稳定的，通常用来发布版本．一般在dev分支进行开发，稳定的内容再合并到master分支．

每个人都有自己的分支，实现了模块功能后合并到dev分支．

分支创建，切换，合并，删除

![branch_all](https://img2018.cnblogs.com/blog/63651/201809/63651-20180920210908347-486995158.gif)

当不同分支对同一文件进行修改并提交后，合并两个分支，容易产生冲突conflict.

![branch_conflict](https://cdn.liaoxuefeng.com/files/attachments/919023000423040/0)

git用`<<<<<<<<`，`=======`，`>>>>>>>>`来标记不同分支的内容，解决冲突后commit形成新的唯一commit.

![conflict_commit](https://cdn.liaoxuefeng.com/files/attachments/919023031831104/0)

### 藏匿(stashing)

在一个分支上修改之后，如果还没有将修改提交到分支上，此时进行切换分支，那么另一个分支上也能看到新的修改．

所有分支都共用一个工作区．可以使用`git stash`将当前分支的修改会被存到栈中而隐藏起来，这样就可以干净地切换到其他分支.

```git
git stash                # 隐藏修改到栈中
git checkout -b dev      # 应藏当前工作目录修改后，切换分支得到一个全新干净分支
git stash list           # 显示隐藏的修改 List the stash entries that you currently have.
git stash pop            # 恢复之前隐藏的内容
```

### 标签

为软件发布创建标签，便于记忆与管理．与commit快照绑定的有意义的名字.

```git
git tag 1.0              # 创建标签，默认打在最新提交的commit快照
git tag                  # 查看tag标签
git log --oneline        # 获取提交commit内容的sha-1值
git tag 1.1 <commit>     # 给指定commit提交快照打标签
git show 1.1             # 查看标签具体信息
git tag -a 1.2 -m "version 1.2 released" <commit>   # -a指定标签名,-m附加信息
git push <gitee> <tagname>   # 推送标签
git push <gitee> --tags  # 推送所有标签
git tag -d <tagname>     # 删除指定本地标签
git push <gitee>:refs/tags/<tagname>   # 删除远程标签，需要先删除本地标签
git blame <file>         # 按照文件查看commit提交记录
```

![git_diff](https://images2017.cnblogs.com/blog/63651/201709/63651-20170914095506203-2063795525.png)

### git常用

```git
git status                            # 查看当前文件状态.Changes to be committed:文件是暂存状态(即将提交的变更)
git log                               # 显示当前分支版本历史
git log --stat                        # 显示commit历史及每次commit发生变更的文件
git log -S <keyword>                  # 根据关键词keyword搜索commit提交历史
git log --follow <file>               # 显示file文件的版本历史，包括文件名
git whatchanged <file>                # 比git log --follow <file> 信息更丰富
git blame <file>                      # 显示用户对指定文件的修改记录
git shortlog                          # 显示提交过的用户和用户commit message
git ls-files --stage                  # 查看index文件内容100644普通文件644权限
git diff                              # 显示暂存区和工作区的差异
git diff --cached <file>              # 显示暂存区和上一个commit的差异
git diff HEAD                         # 显示工作区与当前分支最新commit之间的差异
git diff master..dev                  # 显示两个分支之间的差异
git diff master...dev                 # 显示master与dev共有父分支与dev分支之间的差异
git diff

diff --git a/ttt.md b/ttt.md          # 第一行表示a版本的ttt.md(变动前)与b版本的ttt.md(变动后)比较．
index 4d4dd45..ec4357c 100644         # 第二行index后面两个文件hash值(index区的4d4dd45，与工作区的ec4357c对象进行比较)
                                      # 100644六位数字是对象的模式mode(100代表普通文件，644代表文件权限)
--- a/ttt.md                          # ---表示变动前的版本
+++ b/ttt.md                          # +++表示变动后的版本
@@ -7,3 +7,4 @@ dev                   # -修改前，7,3第7行开始的3行，+修改后，7,4第7行开始4行

 >>>>>>> dev
 4444444444                           # 没有变动
+5555555555                           # + 增加部分
                                      # - 减少部分
git hash-object ttt.md                # 工作目录文件ttt.md的hash值，前7位是diff中index的右边hash
ec4357c135686fd093b57e091da5ca846af05b54
git ls-files --stage                  # 显示暂存区内容的对象名称，包含文件模式，hash
100644 f2b6f80491dc889f88b436422fea7427ae1630a7 0       readme.md
100644 4d4dd4535fbab8c3edbdb1eab429bcf3e01fcbcd 0       ttt.md    # hash前7位是diff中显示的左边hash
git ls-files --stage <file>           # 指定文件
git ls-tree HEAD                      # List the contents of a tree object
100644 blob f2b6f80491dc889f88b436422fea7427ae1630a7    readme.md
100644 blob 85c6d03b5bba69142904ae2cb11d7c53dd44a6e3    ttt.md    # commit的hash

git diff --cached <ttt.md>            # 比较commit(HEAD)和stage的区别

diff --git a/ttt.md b/ttt.md
index 85c6d03..4d4dd45 100644         # 85c6d03HEAD的hash，4d4dd45stage的hash
--- a/ttt.md
+++ b/ttt.md
@@ -6,3 +6,4 @@
 dev
 
 >>>>>>> dev
+4444444444

git diff HEAD <ttt.md>                # 比较commit(HEAD)和working space的区别

diff --git a/ttt.md b/ttt.md
index 85c6d03..ec4357c 100644         # 85c6d03HEAD的hash，ec4357c working tree的hash
--- a/ttt.md
+++ b/ttt.md
@@ -6,3 +6,5 @@
 dev

 >>>>>>> dev
+4444444444
+5555555555

git diff --shortstat "@{0 day ago}"   # 显示今天写了多少行代码
git show <commit>                     # 显示commit提交的元数据和内容变化
git show --name-only <commit>         # 显示commit提交发生变化的文件

git log --oneline                     # This is a shorthand for "--pretty=oneline --abbrev-commit" used together.
git log --oneline --follow <file>     # 
git log --oneline                     # Pretty-print the comtents of tne commit logs in a given format.
git log --oneline [tab能联想]         # --abbrev-commit Show a prefix that names the object uniquely.

3dc1b85 (HEAD -> master) merge
d4debae (dev) dev
10c9b0d 3333333
cfe202b tttt
b27c1f9 tttttttt
5f7a655 ttttttttt
bb404b4 hhhhhhh
77bd726 hhhhhhhh
69e2ba7 (gitee/master) tttttttttttttt
e23cb10 Merge branch 'dev'
416f0cc init
63efdc7 HEAD
62ffb67 change
f611455 init

git log 77bd726..b27c1f9              # 显示两次commit hash之间(不包括左边hash，更早的hash)的commit log

git restore                           # Restore working tree files 
git restore .                         # To restore all files in the current directory
rm <file>
git restore <file>                    # retore <file> from the index，用index恢复working space
git restore --staged <file>           # To restore a <file> in the index to match the version in HEAD，用master中commit的内容恢复index
git restore --source=HEAD --staged --worktree <file>   # both the index and the working tree用master中commit同时恢复index和workding tree
git restore --source master~2 <file>  # 使用指定commit的内容恢复working tree
git ls-files                          # Show cached files in the output(default).查看所有缓存文件，只显示文件名
git ls-files -o                       # --others Show other files in the output，查看未被跟踪的文件
git ls-files -s                       # --stage Show staged contents' mode bits, object name and stage number in the output.
git ls-files -m                       # --modified Show modified files in the output.
git ls-files -d                       # --deleted Show deleted files in the output.
rm <file>                             # remove untracked file
git rm <file>                         # remove tracked file
git rm -f <file>                      # --force Override the up-to-date check.
git rm --cached <file>                # 删除暂存区的文件，不删除工作区的文件
git reset HEAD <file>                 # the same as pre
```

假设master分支目前在提交(commit):'980e3'上，把他推送(push)到gitee上并命名标签'v1.0'，则如下引用等价

```git
980e3
HEAD 
master
gitee/master
refs/remotes/gitee/master
refs/heads/master
v1.0
refs/tags/v1.0
```

### git grep 搜索

```git
git grep check                        # 在working space文件中搜索check 
git grep -n check                     # 显示行号
git grep --name-only check            # 只显示文件名，不显示具体内容
git grep -c check                     # 显示文件名和每个文件中匹配行数
git grep check <ref>                  # 在指定版本里搜索
```

### git内部原理

```git
git rev-list            # Lists commit objects in reverse chronalogical order 
git cat-file            # Provide content or type and size information for repository objects
```

### git对象

每个对象(object)包括三个部分:类型，大小和内容．大小就是指内容的大小，内容取决与对象的类型，有四种类型的对象:blob,tree,commit和tag.

```git
echo 'hello git' |git hash-object --stdin     # 获取'hello git'对应hash
git ls-files --stage index.txt                # 显示index.txt文件对应hash
100644 8d0e41234f24b6da002d962a26c2495ea16a425f 0       index.txt
git cat-file -p 8d0e41234f24b6da002d962a26c2495ea16a425f   # 查看hash对应的文件内容hello git
git cat-file -p master^{tree}                 # master分支上最新的提交所指向的树tree对象
git cat-file -p "master^{tree}"               # zsh中^被用于通配模式，需要用""引起来
```

`git add`将文件内容hash的blob object对象保存到.git/objects，将index保存到staging area

为文件创建hash对象的时候，git不关心文件名，只关心文件里面的内容．

```git
echo 'hello git'>index.txt   # 高层命令实现
git add index.txt
echo 'hello git'|git hash-object -w --stdin   # 底层命令实现 -w 存储数据对象
git update-index --add --cacheinfo 100644 8d0e41234f24b6da002d962a26c2495ea16a425f   # 100644普通文件，100755可执行文件，120000符号链接
git commit -m 'commit'               # git在commit的时候创建tree对象，其实是把索引转化成tree对象
git log --oneline
75bd1d1 (HEAD -> master) commit
git cat-file -t 75bd1d1              # 查看object type，commit
git cat-file -p 75bd1d1
tree 7d966033536d6e90dd262ea8e10f7f8f13a06645
parent d181b1f5e5c02174eae932ef8b072d32bfbf62d9
author zhudingsuifeng <1002557401@qq.com> 1647346702 +0800
committer zhudingsuifeng <1002557401@qq.com> 1647346702 +0800

commit

git cat-file -t 7d96603              # tree
git cat-file -p 7d96603
100644 blob 8d0e41234f24b6da002d962a26c2495ea16a425f    index.txt
100644 blob f2b6f80491dc889f88b436422fea7427ae1630a7    readme.md
100644 blob ec4357c135686fd093b57e091da5ca846af05b54    ttt.md

cat .git/refs/heads/master           # 75bd1d1ef153b85e716e85f33e35f1369128782c
git cat-file -p HEAD                 # HEAD指向master，所以显示内容相同
git cat-file -p master
tree 7d966033536d6e90dd262ea8e10f7f8f13a06645
parent d181b1f5e5c02174eae932ef8b072d32bfbf62d9
author zhudingsuifeng <1002557401@qq.com> 1647346702 +0800
committer zhudingsuifeng <1002557401@qq.com> 1647346702 +0800

commit
```
HEAD里面的内容是master，master内容是当前ref，当前ref内容是commit object hash，commit对象内容是tree object hash，tree对象内容是文件夹(tree object)/文件(blob object)信息，而blob对象存储文件爱你具体内容．

commit提交时，整个状态对应关系是确定的，所以说commit对象就是当前系统的快照snapshot.

![blob object](http://gitbook.liuhui998.com/assets/images/figure/object-blob.png)

blob对象通常用来存储文件的内容，可以使用`git show <SHA1>`查看一个blob对象里的内容．

blob对象就是一块二进制数据，如果两个文件在一个目录树中有同样的数据内容，那么他们将会共享同一个blob对象．

![tree object](http://gitbook.liuhui998.com/assets/images/figure/object-tree.png)

tree对象有一床指向blob对象或者其他tree对象的指针，他一般用来表示内容之间的目录层次关系．

`git show <SHA1>`命令同样可以查看tree对象，但是`git ls-tree <SHA1>`更详细．

```git
git write-tree                 # Create a tree object from the current index
git read-tree                  # 
git ls-tree <3dc1b85>          # List the contents of a tree object

100644 blob f2b6f80491dc889f88b436422fea7427ae1630a7    readme.md
100644 blob 85c6d03b5bba69142904ae2cb11d7c53dd44a6e3    ttt.md
git commit-tree <SHA1>         # 用指定的tree object to create a commit object
echo 'first commit'|git commit-tree <SHA1>
echo 'seccond commit'|git commit-tree <SHA1> -p <SHA1>   # -p 指定父提交
git log --stat <SHA1>          # Generate a diffstat.
```

tree对象包含一串条目，包括:mode,对象类型，SHA1值和文件名．

![commit object](http://gitbook.liuhui998.com/assets/images/figure/object-commit.png)

commit对象指向一个tree对象，并且带有相关的描述信息．

一个commit有以下部分组成，

- tree对象，tree对象的SHA1签名，代表着目录在某一时间点的内容．

- parent父对象，提交commit的SHA1签名代表这当前提交前一步的项目历史，commit对象可以有多个parent对象(合并提交时).如果一个提交没有父对象，我们就叫他根提交root commit.每个项目必须至少有一个根提交．

- author作者，做了此次修改的人的名字，还有修改日期．

- committer提交者，实际创建提交commit的人的名字，提交日期，author and committer maybe not 同一个人．

- 注释，用来描述此次提交．

```git
git show -s --pretty=raw 

commit 3dc1b85ffc02bf74a0533b5fc6e2c106963029d8
tree 09143275c5490e78c9b5fc78a8206f89e601ca8b
parent 10c9b0d484a99e1121e49635fa0bfccd68a0055c
parent d4debae5c2749bff0a01a4330ca2b65813ba1e9a
author zhudingsuifeng <1002557401@qq.com> 1646837948 +0800
committer zhudingsuifeng <1002557401@qq.com> 1646837948 +0800

    merge
git log --pretty=raw    # Pretty-print the contents of the commit logs in a given format.

commit 3dc1b85ffc02bf74a0533b5fc6e2c106963029d8
tree 09143275c5490e78c9b5fc78a8206f89e601ca8b
parent 10c9b0d484a99e1121e49635fa0bfccd68a0055c
parent d4debae5c2749bff0a01a4330ca2b65813ba1e9a
author zhudingsuifeng <1002557401@qq.com> 1646837948 +0800
committer zhudingsuifeng <1002557401@qq.com> 1646837948 +0800

    merge

commit d4debae5c2749bff0a01a4330ca2b65813ba1e9a
tree e5d98cd1a5ad887bc35ff615e6d060f7d1356c32
parent 69e2ba7c92ecc53cae703315dc8b65ec1a9c50d5
author zhudingsuifeng <1002557401@qq.com> 1646754316 +0800
committer zhudingsuifeng <1002557401@qq.com> 1646754316 +0800

    dev
```

对象模型关系

```git
$>tree
.
|-- README
`-- lib
    |-- inc
    |   `-- tricks.rb
    `-- mylib.rb

2 directories, 3 files
```

![object relationship](http://gitbook.liuhui998.com/assets/images/figure/objects-example.png)

每个目录都创建了tree对象，每个文件都创建了blob对象，commit对象指向tree对象．

tag标签对象

![tag object](http://gitbook.liuhui998.com/assets/images/figure/object-tag.png)

一个标签对象包括一个对象名(SHA1签名),对象类型，标签名，标签创建人的名字，还有可能包含签名信息．

标签tag对象是一个永不移动的分支引用，永远指向同一个提交对象．

```git
git tag v1.0                 # 创建tag,默认打在最新commit
git tag -a v1.1 -m "tag message" <commit>
git show v1.0                # 显示v1.0详细信息
git cat-file tag v1.0        # 查看tag object信息

object 3dc1b85ffc02bf74a0533b5fc6e2c106963029d8
type commit
tag v1.0
tagger zhudingsuifeng <1002557401@qq.com> 1647273270 +0800

tag test
```

分支的本质是一个指向某一些列提交之首的指针或引用．

HEAD文件通常是一个符号引用(symbolic reference)，指向目前所在的分支．所谓符号引用，表示它是一个指向其他引用的指针．

执行`git commit`会创建一个提交commit对象，并用HEAD文件中引用所指向的SHA1值设置其父提交字段．

```git
git update-ref refs/heads/<branch> <SHA1>   # 创建分支
git symbolic-ref HEAD                       # 查看HEAD引用对应值
git symbolic-ref HEAD <refs/heads/test>     # 设置HEAD引用的值
```

HEAD引用，tag标签引用，远程引用(remote reference)

手动执行`git gc`或者向远程服务器执行push，git会对仓库进行重新打包以节省空间．

```git
git gc          # 清理空间
git fsck        # 仓库一致性检查，主要是悬空对象(dangling objects)，有时是找回丢失内容的最后希望
.git/objects/pack/pack-<SHA1>.idx   # 打包文件保存位置
.git/objects/pack/pack-<SHA1>.pack

git verify-pack -v .git/objects/pack/pack-<SHA1>.idx   # 查看打包内容
```

![git diff 不同工作区之间的比较](https://img-blog.csdnimg.cn/img_convert/e3acce52aafa2acf1406fd0fe1ce3114.png)

#### reset/revert/checkout/fetch/pull

`git revert`会改变分支记录，因为产生了新的提交。

`git restore`不会影响分支记录。

`git revert` is about making a new commit that reverts the changes made by other commit.

`git restore` is about restoring files in the working tree from either the index or another commit. This command does not update your branch. The command can also be used to restore files in the index from another commit.

`git reset` is about updating your branch, moving the tip in order to add or remove commits from the branch. This operation changes the commit history.

修改了workding directory里的文件，git会发现working directory的内容和index的内容不一致．
`git status`  # Changes not staged for commit

文件仅仅changed是不能commit的，git要求只能提交index里的内容．
`git add`将changed的内容同步到index区域．
`git status`  # Changes to be committed

`git commit`后HEAD的状态和index区域以及workding directory内容一致．

reset使用来修改提交历史的，如果你想撤回已提交的内容，可以使用`git revert`或者`git reset`.

![reset and revert](https://image-static.segmentfault.com/281/097/2810977273-57a4836213ad0_fix732)

`git reset`会修改版本历史，会丢弃掉一些版本历史．而`git revert`是根据commit逆向生成一个新的commit，不会破坏版本历史．

**commit被push到远程仓库，一般不会reset，不然会影响其他人的开发**

不带文件参数的reset影响的是不同区域内的所有内容．`git reset`有三个不同的参数,--soft, --mixed, --hard

```git
working index HEAD target         working index HEAD
----------------------------------------------------
  A       B     C    D     --soft   A       B     D
                           --mixed  A       D     D
                           --hard   D       D     D
                           --merge (disallowed)

working index HEAD target         working index HEAD
----------------------------------------------------
  A       B     C    C     --soft   A       B     C
                           --mixed  A       C     C
                           --hard   C       C     C
                           --merge (disallowed)
```

带文件参数的reset不会影响HEAD，只会将commit里对应文件内容回放到index区域，没有了所谓--hard,--soft.

```git
git reset --mixed HEAD <file>   # 将HEAD文件file内容回放到index,并且HEAD不会移动
git reset <file>                # 等效
git reset <hash> <file>         # 将index内文件恢复到指定版本，可以直接commit
```

checkout与reset --hard都不带文件参数时作用相似，但有以下不同

1. reset 会覆盖workding directory里的所有内容，checkout不会覆盖working directory中修改过且没有git add的文件．

2. reset 把branch移动到HEAD指向的地方，checkout把HEAD移动到另一个branch

![reset or checkout](https://image-static.segmentfault.com/103/313/1033130145-57a48436a5fcd_fix732)

checkout带文件参数时，`git checkout <branch> <file>`同时更新了index区域和workding directory中的file内容

```git
git checkout .                  # 用暂存区所有内容替换工作区文件
git checkout -- .               # same as git checkout . --指代暂存区index/stage
git checkout <file>             # overwrite working tree with the contents in the index
git checkout -- <file>          # if you want to checkout these file out of the index.
git checkout <branch> -- <file> # 维持HEAD指向不变，用branch所指向的提交中file替换暂存区和工作区中的文件
git checkout HEAD .             # 用HEAD指向的master分支全部文件替换工作目录文件内容，如果文件是新建的，master分支中没有则不会被替换
git checkout HEAD <file>        # 指定文件
git checkout                    # 汇总显示工作区，暂存区与HEAD的差别
git checkout HEAD               # same as git checkout
```

### 不同场景下的回退

- 工作区中未添加到暂存区和版本库的文件，执行`git add`操作，将文件添加到index/stage，回退index内容

```git
git init
echo 'init'>>readme.md
git add readme.md
git rm --cached <file>          # 将文件从暂存区移除，但是工作区没有消失
git add readme.md
git restore --staged readme.md  # 没有分支被创建,HEAD没有指向的时候不起作用
git add readme.md
git reset HEAD readme.md        # 没有分支被创建,HEAD没有指向的时候不起作用
```

`git restore --staged <file>`和`git reset HEAD <file>`不能是整个版本库的第一个文件，因为这两个命令都是依赖HEAD指针的，此时只是执行了`git init`初始化仓库，`git add <file>`将文件添加到index/stage暂存区中，通过`git branch -a`可以看到此时还没有任何分支被创建，`git reflog --oneline`也找不到HEAD。当`git commit -m 'init'`后，默认master分支被创建，HEAD指向master分支。

git restore Restore working tree fiels 

Restore specified paths in the working tree with some contents from a restore source. If a path is tracked but does not exist in the restore source, it witll be removed to match the sorce.

The command can alse be used to restore the content in the index with `--staged`, or restore both the workding tree and the index with `--staged --worktree`.

By default, if `--staged` is given, the contents are restored from HEAD, otherwise from the index. Use `--source` to restore from a different commit.

- 版本库中的文件，修改或者删除后未执行`git add`操作，只是对工作区workding space做了修改，回退index和worktree内容，主要是回退workging tree 工作目录内容

```git
echo 'remove file'>>readme.md
git rm <file>                   # 将文件从工作区和暂存区同时删除文件
git rm <file>                   # 文件在index索引中有变更，使用--cached 保留本地文件，使用-f 强制删除index和working tree中内容
git restore readme.md           # 使用暂存区stage/index中文件替换工作区指定文件，文件回退
git checkout -- <file>          # 使用暂存区stage/index中文件替换工作区指定文件，文件回退
git checkout HEAD <file>        # 使用HEAD指向最新commit的内容同时替换inedx/stage和working space内容
git checkout                    # 汇总显示工作区，暂存区与HEAD的差别，只关注与HEAD的区别，而不关注是工作区还是暂存区
git checkout HEAD               # 汇总显示工作区，暂存区与HEAD的差别，只关注与HEAD的区别，而不关注是工作区还是暂存区
git reset --hard HEAD           # 使用HEAD指向最新commit的内容同时替换inedx/stage和working space内容
```

- 版本库中的文件，修改或删除后执行了`git add`操作，文件已添加到index/stage，回退stage内容

```git
git restore --staged <file>     # 使用repository版本库中的文件覆盖暂存区的数据
git reset HEAD <file>           # reset 指定文件只能是--mixed，即使用指定commit的内容替换HEAD和stage内容，而working space内容不变
git hash-object <file>          # 获取工作区workding directory文件hash值
git ls-files -s <file>          # --stage 获取stage/index中文件hash值 Show staged contents' mode bits, object name and stage number in the output.
git ls-files -c <file>          # --cached Show cached files(name) in the output (default)
git restore --staged <file>     # 是文件的替换，效果是不管git add多少次，一次restore --staged回到解放前
git rm --cached <file>          # 一次rm --cached对应一次git add，多次add需要多次回退才能回到最初状态
```

- 版本库中的文件，修改或删除后执行了`git add`,`git commit`操作，文件已添加到index并且提交到repository

`git commit`命令执行后就形成了历史，叫做提交日志，想要回退就得有篡改历史的能力，`git reset HEAD^`提供了把本地文件反向修改，然后再次提交的能力。

`git reset`不带文件参数可以有--soft,--mixed,--hard三种选项，--soft只影响HEAD，--mixed影响HEAD和index,--hard影响HEAD,index和工作目录worktree.

```git
git reset --soft HEAD~1         # 将HEAD回退到最新版本的前一版本，即倒数第二版本
git reset --mixed HEAD@{1}      # 将HEAD和index回退到最新版本的前一版本，即倒数第二版本
git reset --hard "HEAD^"        # 将HEAD,index和worktree回退到最新版本的前一版本，即倒数第二版本
git reset --soft "HEAD^^"       # 将HEAD回退到最新版本的前二版本，即倒数第三版本
git reset HEAD <file>           # default --mixed and only --mixed，HEAD不会移动，只会影响index/stage
```

- 版本库中的文件，修改或删除后执行了`git add`,`git commit`，`git push`操作，文件已添加到index并且提交到repository，并且推送到远程仓库push to remote repository

相较于对版本库文件修改或删除之后，执行`git add, git commit`，修改内容已经推送到远程仓库，要想回退，只需要将本地仓库回退后重新推送push，因为本地回退了，所以远程仓库记录是领先于本地仓库的，这时候push会失败。Updates were rejected because the tip of your current branch is behind its remote counterpart.

```git
git push gitee master           # failed to push ref
git push -f gitee master        # 强制推送
```

- 两次`git commit`之后产生两条日志，只还原倒数第二次提交，对最近一次提交无影响

`git reset`与`git checkout`重要的区别是，`reset`会移动`HEAD`分支的指向，即`HEAD->master`同时指向其他的commit，而`checkout`只会将`HEAD`指向其他的分支如dev，master分支是不移动的。

分支的本质就是指向提交对象commit object的指针，HEAD是指向分支的指针，可以认为是指针的别名。

`git reset HEAD@{3}`将`HEAD->master`指向之前的第三次提交，并不是意味着中间几次提交被删除了，这几次提交还在的，reset只是移动了指针，并没有将数据删除，还可以通过`reset reset HEAD@{1}`移动回来。

```git
git reset HEAD~2                # 回退最近两次修改的所有内容,reset虽然不会删除文件，但是会篡改提交历史
git reflog --oneline            # reflog 显示引用移动历史
git revert HEAD@{1}             # 在倒数第二次提交的基础上直接修改，会造成冲突，解决冲突后，正常add commit就可以了
```

### git远程链接

同一个项目有两种地址方式，一种是https方式，一种是ssh方式．

- https

`https://github.com/zhudingsuifeng/restart.git`可以直接有效打开网址，但是用户每次通过git提交的时候都要输入用户名和密码．

- ssh key

`git@github.com:zhudingsuifeng/restart.git`需要在github配置ssh key后使用，可以在git提交代码时跳过验证过程，简化操作流程．

`ssh-keygen -t ed25519 -C "your_email@example.com"   # 生成ssh key并在github配置公钥．`

复制~/.ssh/id_ed25519.pub内容到github中，setting->SSH and GPG keys．

```ssh
ssh -T git@github.com   # 测试是否成功配置ssh key.
```

之前已经使用https链接的，想要使用ssh提交，需要修改项目目录下.git文件夹下的config文件，将地址修改为ssh地址．

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
