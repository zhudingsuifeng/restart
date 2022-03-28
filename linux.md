## linux

### linux更换默认shell

1. 查看系统支持的shell

```shell
$ cat /etc/shells

# Pathnames of valid login shells.
# See shells(5) for details.

/bin/sh
/bin/bash
/bin/zsh
/usr/bin/zsh
/usr/bin/git-shell

or

$ chsh -l


/bin/sh
/bin/bash
/bin/zsh
/usr/bin/zsh
/usr/bin/git-shell
```

2. 更换默认shell为zsh(需要zsh的全路径)

```shell
sudo chsh -s /usr/bin/zsh   # 注意chsh - change your login shell
```
