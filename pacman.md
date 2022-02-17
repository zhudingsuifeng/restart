## pacman

Pacman is a package management utility that tracks installed packages on a Linux system. It features dependency support, package groups, install and uninstall scripts, and the ability to sync your local machine with a remote repository to automatically upgrade packages.

pacman是Arch Linux软件包管理器.pacman可以安装，删除和升级软件包，并尝试自动处理依赖关系．

**pacman通过使用软件包数据库(本地)和主服务器(远程)同步软件包列表来保持系统是最新的．**

`pacman <operation> [options] [targets]`

对于新手，不知道从何处着手，就从`pacman -h`开始．

### pacman {-h --help}

Display syntax for the given operation. If no operation was supplied, then the general syntax is shown.

`$ pacman -h   # 显示pacman帮助信息 `

### pacman {-V --version}

Display version and exit.

```pacman
$ pacman -V   # 显示pacman版本信息

Pacman V6.0.1 - libalpm V13.0.1
```

### pacman {-D --database}

Operate on the package database.

### pacman {-F --files}

Query the files database. This operation allows you to look for packages owning certain files or display files owned by certain packages.

```pacman
$ pacman -F pacman               # 按文件名查找软件库(包括已安装和未安装)中的包
$ pacman -Fl pacman              # 查询远程库中软件包包含的文件
$ which pacman
/usr/bin/pacman
$ pacman -F /usr/bin/pacman      # 查询包含某个文件的包名
usr/bin/pacman 由　core/pacman 6.0.1-3 所拥有
$ pacman -Fy                     # 同步文件数据库
```

### pacman {-Q --query}

Query the package database. This operation allows you to view installed packages and their files, as well as meta-information about individual packages.

pacman -Q 查询本地软件包数据库，针对已安装内容．

```pacman 
$ pacman -Q --help
$ pacman -Q              # 列出已经安装的所有软件包
$ pacman -Q git          # 查看具体app是否已经安装，如果已安装显示具体版本信息，未安装则报错
$ pacman -Qi git         # 列出已安装包app的详细信息
$ pacman -Ql zsh         # 列出已安装zsh包所包含的所有文件
$ pacman -Qo git         # 查找git文件属于哪个app
/usr/bin/git 由 git 2.35.1-1 所拥有
$ pacman -Qs git         # 搜寻符合指定字符串的已安装本地的软件包
$ pacman -Ss pacman
core/pacman 6.0.1-3 (base-devel)
$ pacman -Qg base-devel  # 查询哪些已安装package belong this group, 包组一般显示在包名后面的(括号中)
$ pacman -Qdt            # 列出所有不再作为依赖的软件包
```
### pacman {-R --remove}

Remove package(s) from the system. 

```pacman
# pacman -R package      # 删除单个软件包，保留其全部已经安装的依赖关系
# pacman -Rs package     # 删除指定软件包，及其所有没有被其他已安装软件包使用的依赖关系．
# pacman -Rc package     # 删除package包和依赖于package的包，即依赖树由此斩断
# pacman -Rsc package    # 删除package包和package依赖的包?
# -c --cascade           # 删除软件包及所有依赖于此的软件包
# -s --recursive         # 删除不需要的依赖关系
```

### pacman {-S --sync}

pacman -S 查询同步数据库，针对远程仓库，包含安装与未安装内容．

```pacman
$ pacman -S --help
$ pacman -Sg             # 查询所有包组 --groups
# Display all the members for each package group specified. If no group names are provided, all groups will be listed. 
$ pacman -Sg base-devel  # 查询组base-devel所包含的软件包
$ pacman -Ss pacman      # 搜索pacman相关的包，包组一般显示在包名后面的(括号中)
$ pacman -Si pacman      # 从数据库中搜索pacman的信息
# pacman -S git          # Down load and install app including dependencies.
# pacman -Sd git         # 忽略依赖问题，安装git
# pacman -Sf git         # 强制安装git包
# pacman -Sy             # 仅同步源，从服务器下载新的软件包数据库
# -y --refresh Download a fressh copy of the master package database from the server(s) defined in pacman.conf.
# pacman -Sy git         # 同步源之后安装git包
# pacman -Su             # 更新系统中所有已安装包
# -u --sysupgrade Upgrades all packages that are out-of-date. Each currently-installed package will be examined and upgraded if a newer package exists.
# pacman -Syy            # 强制更新软件包数据库
# pacman -Syu            # Update package list and upgrade all packages afterwards.
# pacman -Syu git        # Update package list, upgrade all packages, and then install app if it wasn't already installed.
# pacman -Sc             # 清理/var/cache/pacman/pkg/旧软件包和/var/lib/pacman/无用的软件库
# pacman -Scc            # 清理/var/cache/pacman/pkg/所有软件包和/var/lib/pacman/无用的软件库
# pacman -Su --ignore git   # 升级时忽略app
```

### pacman {-T --deptest}

Check each dependency specified and return a list of dependdeccies that are not currently satisfied on the system.

判断某一应用是否依赖于其他指定应用，支持>,=,< 配合版本使用．如果依赖指定应用则无返回，否则返回该应用．

```pacman
$ pacman -Si git   # 查看数据库中该应用详细信息

# 依赖于: curl expat perl perl-error perl-mailtools openssl pcre2 grep shadow zlib

$ pacman -T git "curl"
$ pacman -T git "perl"
$ pacman -T git "deptest"
deptest

$ pacman -Si vim

# 依赖于: vim-runtime=8.2.4106-1 gpm ...

$ pacman -T vim "vim-runtime>8"
```

### pacman {-U --upgrade}

Upgrade or add package(s) to the system and install the required dependencies from sync repositories. Either a URL or file path can be specified.

```pacman
# pacman -U /path/to/package/name-version.pkg.tar.zst   # 安装一个本地包(不从源里下载)
# pacman -U http://www.example.com/name.pkg.tar.zst     # 安装一个远程包(不在pacman配置的源里面)
```

### 常用pacman组合

```pacman
$ pacman -Si vim   # 显示数据库中有关vim的详细信息.软件库: extra
$ pacman -Qi vim   # 显示已经安装本地存储的有关vim的详细信息．安装日期，安装原因
```

有问题可以经常使用`man pacman & pacman -h`，还可以访问pacman_(简体中文)-ArchWiki
