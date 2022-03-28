## vim

### manjaro vim config

vim根据不同的场景有不同的配置办法，不同的配置之间有可能会覆盖．

```vim
/usr/share/vim/vim82/defaults.vim
```

manjaro使用`pacman -Syu`更新vim后，自带的配置文件会被重置，需要再次配置．

```vim
" mine start
set nu
set autoindent
set tabstop=4
set shiftwidth=4
" mine end
```

source defaults.vim
