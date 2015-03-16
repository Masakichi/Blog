Title: 使用 virtualenvwrapper 管理 Python 环境
Date: 2014-08-04 15:31
Category: Python
Tags: virtualenv
Slug: use-virtualenvwrapper

重新安装系统有一段时间了，重新配置了各个 Project 的 virtualenv。由于散落在各个不同目录，难以管理。于是把几个环境放在一个目录方便管理，这个时候遇到了问题。发现 activate 环境时出了问题，如 [renaming-a-virtualenv-folder-without-breaking-it](http://stackoverflow.com/questions/6628476/renaming-a-virtualenv-folder-without-breaking-it)。于是便尝试使用了 [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/) 。

## 安装

详细步骤见[官网](http://virtualenvwrapper.readthedocs.org/en/latest/install.html)。简单的列举一下：

1. 通过pip安装：
`pip install virtualenvwrapper`

2. 将下面三行写入 .bashrc 或者 .zshrc 文件，下面的路径自己视情况而定。
```shell
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
```

## 基本使用

- 查看

`lsvirtualenv` 或者 `workon`

- 创建

`mkvirtualenv venv` 其中 venv 是 virtualenv 的名称。创建好的 venv 会在事先设定好的目录下。比如我的在 `~/.virtualenvs`

- 激活 

`workon venv`

- 删除

`rmvirtualenv` 需要注意的先要 deactivate 环境才能删除。

到此为止，基本上也够用了，不过这样就有点浪费这个软件了，下面介绍一些 virtulenv 不具备的方便功能。

## 进阶使用

主要是和项目配合使用。比如创建一个 Project 的同时产生一个 virtualenv，将一个 virtualenv 和现有项目绑定。这个有什么用呢？每当 `workon venv` 的时候，就会自动进入这个项目的目录，非常方便。

- 创建项目&virtualenv

`mkproject project` 就会创建一个目录，并与同名的 virtualenv 绑定。

- 绑定项目&virtualenv

`setvirtualenvproject [virtualenv_path project_path]`

如果没有参数，则会把当前 virtualenv 和 当前目录绑定。

- 和 zsh 配合

如果你使用 oh-my-zsh 的话，有一个插件可以使用。它有个功能是每当 cd 进入一个使用 git 的项目，就会自动启动对应的 virtualenv，可谓相当方便，这个在使用 PyCharm 的内置 Terminal 比较有用，只要 `cd .` 就可以激活 virtualenv。

## 总结

有的时候，花点时间学习一点新的东西，哪怕是一句命令，对于效率的提高是相当明显的。所以嘛要勇于接受新鲜事物，人就是不能安于现状！每次浪费一点时间而不选择简单优雅的做法，久而久之就麻痹了。多记一点快捷键、多学一点 Vim 技巧又不会怀孕不是？