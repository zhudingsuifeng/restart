### AUR(Arch User Repository)

AUR表示Arch用户仓库(Arch User Repository)。它是针对基于Arch的Linux发行版用户的社区驱动的仓库。包含名为PKGBUILD的包描述，可以让你使用makepkg从源代码编译软件包，然后通过pacman(Arch Linux中的软件包管理起)安装。

在AUR页面`https://aur.archlinux.org`上搜索要安装的软件包，获取对应git地址。

```
git clone [package URL]
cd [package name]
makepkg -si              # 安装软件-i --install 成功编译后安装软件包-s --syncdeps 使用pacman 安装缺失的依赖关系
```

PKGBUILD是一个shell脚本，包含Arch Linux在构建软件包时需要的信息。

PKGBUILD - Arch Linux package build description file

Arch Linux用makepkg创建软件包。当makepkg运行时，它会在当前目录寻找PKGBUILD文件，并依照其中的指令编译或获取所需的依赖文件，并生成pkgname.pkg.tar.xz软件包。生成的包内有二进制文件和安装指令，可以使用pacman进行安装。

makepkg是一个软件包自动编译脚本。使用时需要一个Unix环境和PKGBUILD。makepkg是由pacman包提供的。

也可以通过`yaourt`包管理工具安装AUR软件包

```
yaourt (搜索模式|软件包文件)
yaourt {-Q --query}
yaourt {-S --sync}
yaourt {-U --upgrade}
yaourt {-G --getpkgbuild}
yaourt {-P --pkgbuild} [-i --install]
```

### 安装sogoupinyin

```
yaourt sogoupinyin

aur/fcitx-sogoupinyin 4.0.0.1605-1
	Sogou Pinyin for Linux
aur/sogoupinyin-skin-roulan 0.9-1
	An Elegant Skin for fcitx-sogoupinyin
==> 输入 n 以安装需要的软件包
==> ----------------------------
==> 输入序号Yaourt就会从AUR下载PKGBUILD构建脚本，问是否需要编辑这个构建脚本。一般不需要编辑。
==> Edit PKGBUILD ? [Y/n]("A" to abort)
==> 检查依赖包，询问是否继续构建Arch软件包。
==> Continue building sogoupinyin ? [Y/n]
==> Continue installing sogoupinyin ? [Y/n]
```

注意，Yaourt命令本身不需要加sudo前缀，如果添加了sudo前缀，Yaourt会提示你这个操作是不安全的。在构建完成Arch包后才需要输入密码调用root权限将Arch包安装到系统上。
