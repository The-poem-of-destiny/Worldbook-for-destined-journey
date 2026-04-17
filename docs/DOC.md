请使用酒馆助手的同步脚本在编辑器中编写世界书

**理应保证本仓库的世界书内容为最新的**

## 环境准备

- Node.js >= 22
- Git

## 第一次使用？

1. 下载 Git 和 NodeJS 并安装，教程指路：[点击这里](https://stagedog.github.io/%E9%9D%92%E7%A9%BA%E8%8E%89/%E5%B7%A5%E5%85%B7%E7%BB%8F%E9%AA%8C/%E5%AE%9E%E6%97%B6%E7%BC%96%E5%86%99%E5%89%8D%E7%AB%AF%E7%95%8C%E9%9D%A2%E6%88%96%E8%84%9A%E6%9C%AC/%E7%8E%AF%E5%A2%83%E5%87%86%E5%A4%87/)

2. 下载脚本：[点击这里](https://gitgud.io/StageDog/tavern_sync/-/raw/main/dist/tavern_sync.mjs?inline=false)

> 你应该会得到一个叫 `tavern_sync.mjs` 的文件。将该文件存放在一个空的文件夹中

3. 在[酒馆助手](https://n0vi028.github.io/JS-Slash-Runner-Doc/guide/%E5%85%B3%E4%BA%8E%E9%85%92%E9%A6%86%E5%8A%A9%E6%89%8B/%E5%AE%89%E8%A3%85%E4%B8%8E%E6%9B%B4%E6%96%B0.html)的脚本库中添加脚本，内容填写:

```javascript
import 'https://testingcf.jsdelivr.net/gh/StageDog/tavern_sync/dist/script.js'
```

脚本名称随你喜欢，然后开启该脚本。

4. 回到你存放 `tavern_sync.mjs` 的文件夹，打开终端，输入以下命令并回车：

```bash
node tavern_sync.mjs
```

然后会有如下输出:

```bash
配置文件不存在，已自动生成在 '当前完整目录路径\tavern_sync.yaml'，请填写配置文件后重新运行
```

5. 在 `tavern_sync.yaml` 配置文件的文件夹下打开终端，依次运行如下命令:

```bash
mkdir 世界书
cd ./世界书/
git clone https://github.com/Hilothea/Worldbook-for-destined-journey.git
```

6. 在 `tavern_sync.yaml` 配置文件添加如下内容（原来自动生成的可保留）:

```yaml
...
配置:
  ...
  命定之诗:
    类型: 世界书
    酒馆中的名称: 命定之诗与黄昏之歌v2   # 后续名称有修改的话，这里需要修改为对应酒馆中的世界书名称
    本地文件路径: ./世界书/Worldbook-for-destined-journey/命定之诗
```

之后你便可在本地编辑器中编写世界书了

## 同步脚本常用操作

### 提取酒馆世界书

> 执行这个操作前，请保证你酒馆世界书内容比本仓库中的世界书内容更新

在 `tavern_sync.mjs` 的目录下打开终端，输入以下命令并回车：

```bash
node tavern_sync.mjs pull 命定之诗
```

### 修改世界书

`命定之诗.yaml` 配置文件中是世界书的条目列表，对应酒馆世界书设置为`自定义`排序后的显示结果

每个`-`块即对应一个世界书条目，所以你可以十分轻松地进行条目的新建、删除、修改、排序

[详细解释](https://stagedog.github.io/%E9%9D%92%E7%A9%BA%E8%8E%89/%E5%B7%A5%E5%85%B7%E7%BB%8F%E9%AA%8C/%E5%AE%9E%E6%97%B6%E7%BC%96%E5%86%99%E8%A7%92%E8%89%B2%E5%8D%A1%E3%80%81%E4%B8%96%E7%95%8C%E4%B9%A6%E6%88%96%E9%A2%84%E8%AE%BE/%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E/#id4)

#### 同步修改结果到酒馆

在 `tavern_sync.mjs` 的目录下打开终端，输入以下命令并回车：

```bash
node tavern_sync.mjs push 命定之诗
```

#### 实时修改

如果你想长时间更改, 又需要频繁地在酒馆测试更改后结果, 则可以开启监听功能:

```bash
node tavern_sync.mjs watch 命定之诗
```

在监听过程中, **你只需要修改本地文件, 酒馆就会自动同步你的修改**

以上只是简要的使用方法，完整教程请查看 [同步脚本教程](https://stagedog.github.io/%E9%9D%92%E7%A9%BA%E8%8E%89/%E5%B7%A5%E5%85%B7%E7%BB%8F%E9%AA%8C/%E5%AE%9E%E6%97%B6%E7%BC%96%E5%86%99%E8%A7%92%E8%89%B2%E5%8D%A1%E3%80%81%E4%B8%96%E7%95%8C%E4%B9%A6%E6%88%96%E9%A2%84%E8%AE%BE/%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E/)

## 提交本地修改并推送至远程仓库

修改本地文件后，运行以下命令将修改推送至远程仓库:

```bash
git add .
git commit -m "你对这次更新的简要描述"
git push origin main
```

如果遇到冲突，参考下面的内容

## 本地仓库与远程仓库的同步更新

这里是关于别人更新世界书并推送至仓库后，你该怎么更新的处理方法。

在本仓库的本地目录中打开终端，运行命令: `git pull origin main --rebase`

- `--rebase` 可以避免产生额外的 merge commit，让提交历史干净

如果出现冲突：

1. Git 会停下来，提示你哪些文件有冲突

用编辑器打开文件，手动解决冲突

冲突内容会是这样：

  ```txt
  <<<<<<< HEAD
  这是你本地的内容
  =======
  这是远程的内容
  >>>>>>> origin/main
  ```

2. 标记冲突已解决，然后继续 rebase

  ```bash
  git add .
  git rebase --continue
  ```

如果还有冲突，就重复上面的步骤
  
直到 rebase 成功结束

3. 推送（如果你本地有和远程不同修改）

```bash
git status # 确认你的修改均已添加
git push
```

## 编辑器选择

并没有限制，你可以使用任何你喜欢的编辑器（甚至是笔记本？）
