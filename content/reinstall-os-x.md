Title: 记第一次重装OS X
Date: 2014-07-21 17:18
Category: Mac
Tags: OS X, Yosemite
Slug: reinstall-os-x

昨天，重新安装了OS X 10.10 Yosemite。已经到了第三个预览版，日常用问题已经不大，与我相关的问题基本少数。安装过程只是无聊的等待而已，主要记录一下配置的过程，以防遗忘。

## 安装
1. 备份，这个没啥说的
2. 制作安装盘，参看：[英文说明](http://mac-how-to.wonderhowto.com/how-to/create-bootable-install-usb-drive-mac-os-x-10-10-yosemite-0155306/)、[中文说明](http://www.macx.cn/forum.php?mod=viewthread&tid=2128750&extra=page%3D1%26filter%3Dtypeid%26typeid%3D46%26typeid%3D46)。
3. 重启，开机时按住Option键，便可以找到刚刚制作的安装盘了。需要指出的一点是，如果直接就安装，是覆盖安装，会保留原系统里的用户文件，这样安装不是很干净，所以我选择抹掉原来分区进而重新安装的。

## 配置系统
> 无论如何，首先架梯！——公输盘

- 安装[GoAgentX](https://github.com/ohdarling/GoAgentX/releases)，配置shadowsocks信息。
- 安装[Homebrew](http://brew.sh/)，然后`brew install proxychains-ng`，是用在命令行的代理，命令行时用到的链接被墙就用得上它了。
- 安装[Homebrew Cask](http://caskroom.io/)，方便命令行安装App。
- 安装必备的其他软件。
    - App: [http://setapp.me/users/gimo](http://setapp.me/users/gimo)
    - 使用Homebrew安装的：
        - archey
        - git
        - python
        - tree
        - python
        - macvim
    - 使用cask安装的：
        - aliwangwang
        - google-chrome
        - qq
        - android-file-transfer
        - iterm2
        - rescuetime
        - atom
        - macdown
        - xtrafinder
        - dropbox
        - mplayerx
        - flux
        - pycharm
- 一些软件的配置
    - 对于macvim
        - 安装参数：`brew install macvim --override-system-vim --with-cscope --with-lua --HEAD`
        - .vimrc：[https://github.com/Masakichi/dotfiles](https://github.com/Masakichi/dotfiles)
    - 对于zsh
        - 安装[oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh)
        - .zshrc：[https://github.com/Masakichi/dotfiles](https://github.com/Masakichi/dotfiles)
        - 下载powerline补丁字体：[https://github.com/Lokaltog/powerline-fonts](https://github.com/Lokaltog/powerline-fonts)
        - 修改`/etc/shells`
        - 执行：`chsh -s /usr/local/bin/zsh`
    - 对于iTerm2
        - 下载colorscheme：[https://github.com/mbadolato/iTerm2-Color-Schemes](https://github.com/mbadolato/iTerm2-Color-Schemes)

- 安装 ntfs-3g 读写 ntfs 格式磁盘。详见：`https://gist.github.com/bjorgvino/f24e5c079b92f921b765`

## 截图
![yosemite-desktop]({filename}/images/yosemite-desktop.png)
