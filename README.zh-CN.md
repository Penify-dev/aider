# aider - 终端中的AI结对编程

Aider是一个命令行工具，让您可以与大语言模型进行结对编程，
编辑存储在本地git仓库中的代码。
Aider将直接编辑本地源文件中的代码，
并使用合理的提交消息[进行git commit更改](https://aider.chat/docs/faq.html#how-does-aider-use-git)。
您可以启动新项目或使用现有的git仓库。
Aider的独特之处在于，它允许您请求更改[已存在的大型代码库](https://aider.chat/docs/repomap.html)。
Aider与GPT-4o、Claude 3 Opus、GPT-3.5配合良好，
并支持[连接到几乎任何大语言模型](https://aider.chat/docs/llms.html)。

<p align="center">
  <img src="assets/screencast.svg" alt="aider screencast">
</p>

<p align="center">
  <a href="https://discord.gg/Tv2uQnR88V">
    <img src="https://img.shields.io/badge/Join-Discord-blue.svg"/>
  </a>
</p>

- [快速开始](#快速开始)
- [功能](#功能)
- [用法](#用法)
- [教程视频](https://aider.chat/docs/install.html#tutorial-videos)
- [聊天内命令](#聊天内命令)
- [提示](#提示)
- [安装](https://aider.chat/docs/install.html)
- [连接到大语言模型](https://aider.chat/docs/llms.html)
- [大语言模型排行榜](https://aider.chat/docs/leaderboards/)
- [语音转代码](https://aider.chat/docs/voice.html)
- [聊天记录示例](https://aider.chat/examples/)
- [常见问题](https://aider.chat/docs/faq.html)
- [Discord](https://discord.gg/Tv2uQnR88V)
- [博客](https://aider.chat/blog/)


## 快速开始

有关更多详细信息，请参阅[安装说明](https://aider.chat/docs/install.html)，
但您可以这样快速开始：

```
$ pip install aider-chat

# 使用GPT-4o
$ export OPENAI_API_KEY=your-key-goes-here
$ aider

# 使用Claude 3 Opus:
$ export ANTHROPIC_API_KEY=your-key-goes-here
$ aider --opus
```


## 功能

* 通过在命令行运行`aider <file1> <file2> ...`并指定一组源文件来与aider讨论和编辑代码。Aider让大语言模型能够查看和编辑这些文件的内容。
* Aider可以用大多数流行语言编写和编辑代码：Python、JavaScript、TypeScript、PHP、HTML、CSS等。
* Aider与GPT-4o、Claude 3 Opus、GPT-3.5配合良好，并支持[连接到几乎任何大语言模型](https://aider.chat/docs/llms.html)。
* 请求代码的新功能、更改、改进或错误修复。要求新的测试用例、更新的文档或代码重构。
* Aider将大语言模型建议的编辑直接应用到您的源文件。
* Aider将[自动将每个更改集提交到本地git仓库](https://aider.chat/docs/faq.html#how-does-aider-use-git)，并附带描述性提交消息。这些频繁的自动提交提供了一个安全网。撤销更改或使用标准git工作流来管理更长的更改序列非常容易。
* 您可以一次使用多个源文件与aider工作，因此aider可以在单个更改集/提交中对所有文件进行协调的代码更改。
* Aider可以[为大语言模型提供整个git仓库的映射](https://aider.chat/docs/repomap.html)，这有助于它理解和修改大型代码库。
* 您还可以在与aider聊天时使用编辑器手动编辑文件。Aider会注意到这些带外编辑，并保持对文件最新版本的更新。这让您可以在aider聊天和编辑器之间来回切换，与大语言模型协作编码。
* 如果您使用具有视觉能力的OpenAI模型（GPT-4o、GPT-4 Turbo等），可以将图像文件添加到聊天中。


## 用法

使用您想要编辑的源代码文件运行`aider`。
这些文件将被"添加到聊天会话"，以便大语言模型可以查看它们的
内容并根据您的指示进行编辑。

```
aider <file1> <file2> ...
```

要有选择性，只添加大语言模型需要编辑的文件。
如果您添加一堆不相关的文件，大语言模型可能会不堪重负
和混乱（而且会花费更多代币）。
Aider将自动
与大语言模型共享其他相关文件的片段，以便它可以
[理解代码库的其余部分](https://aider.chat/docs/repomap.html)。

您也可以在git仓库的任何位置启动aider，而无需在
命令行上指定文件。它将发现仓库中的所有文件。
然后，您可以使用下面描述的`/add`和`/drop`聊天命令
在聊天会话中添加和删除单个文件。
如果您或大语言模型在对话中提到仓库的任何文件名，
aider会询问您是否要将它们添加到聊天中。

Aider还有许多其他选项，可以通过
命令行开关、环境变量或配置文件进行设置。
有关详细信息，请参阅`aider --help`。


## 聊天内命令

Aider支持聊天中的命令，所有命令都以`/`开头。以下是一些最有用的聊天内命令：

* `/add <file>`: 将匹配的文件（包括图像文件）添加到聊天会话。
* `/drop <file>`: 从聊天会话中删除匹配的文件。
* `/undo`: 如果最后一个git提交是由aider完成的，则撤销它。
* `/diff`: 显示最后一个aider提交的差异。
* `/run <command>`: 运行shell命令，并可选择将输出添加到聊天。
* `/voice`: 向aider说话以[通过语音请求代码更改](https://aider.chat/docs/voice.html)。
* `/help`: 显示所有命令的帮助。

有关更多信息，请参阅[完整命令文档](https://aider.chat/docs/commands.html)。


## 提示

* 思考需要编辑哪些文件来进行更改，并将它们添加到聊天中。
Aider可以帮助大语言模型自己弄清楚要编辑哪些文件，但最有效的方法是自己将所需的文件添加到聊天中。
* 大型更改最好作为一系列经过深思熟虑的小步骤来执行，在这些步骤中您规划方法和整体设计。像对待初级开发人员一样引导大语言模型完成更改。先要求重构以准备，然后再要求实际更改。花时间要求代码质量/结构改进。
* 如果大语言模型没有提供有用的响应，请使用Control-C安全地中断它。部分响应将保留在对话中，因此您可以在使用更多信息或指示回复大语言模型时引用它。
* 使用`/run`命令运行测试、linter等，并将输出显示给大语言模型，以便它可以修复任何问题。
* 使用Meta-ENTER（在某些环境中为Esc+ENTER）输入多行聊天消息。或者在第一行单独输入`{`以开始多行消息，在最后一行单独输入`}`以结束它。
* 如果您的代码抛出错误，请使用`/run`或将其粘贴到聊天中，与大语言模型共享错误输出。让大语言模型找出并修复错误。
* 大语言模型了解许多标准工具和库，但可能会在API和函数参数的某些细节上出错。您可以将文档片段粘贴到聊天中以解决这些问题。
* 大语言模型只能看到您特别"添加到聊天"的文件的内容。Aider还会发送[整个git仓库的映射](https://aider.chat/docs/repomap.html)。因此，如果大语言模型认为您的请求需要，它可能会要求查看其他文件。

## 聊天记录示例

[示例记录页面](https://aider.chat/examples/)展示了如何与aider聊天来编写和编辑代码。

## 安装

请参阅[安装说明](https://aider.chat/docs/install.html)。

## 常见问题

有关更多信息，请参阅[常见问题](https://aider.chat/docs/faq.html)。

## 用户的赞美之词

* *迄今为止最好的AI编码助手。* -- [Matthew Berman](https://www.youtube.com/watch?v=df8afeb1FY8)
* *毫无疑问，这是迄今为止最好的AI编码助手工具。* -- [IndyDevDan](https://www.youtube.com/watch?v=MPYFPvxfGZs)
* *Aider...轻松将我的编码生产力提高了四倍。* -- [SOLAR_FIELDS](https://news.ycombinator.com/item?id=36212100)
* *这是一个很酷的工作流程...Aider的人体工程学对我来说完美。* -- [qup](https://news.ycombinator.com/item?id=38185326)
* *这真的就像您的高级开发人员就住在Git仓库中 - 真是太棒了！* -- [rappster](https://github.com/paul-gauthier/aider/issues/124)
* *多么神奇的工具。令人难以置信。* -- [valyagolev](https://github.com/paul-gauthier/aider/issues/6#issue-1722897858)
* *Aider是如此令人惊叹！* -- [cgrothaus](https://github.com/paul-gauthier/aider/issues/82#issuecomment-1631876700)
* *它比我启动并制作前几个工作版本要快得多。* -- [Daniel Feldman](https://twitter.com/d_feldman/status/1662295077387923456)
* *感谢您提供Aider！它真的感觉像是对编码未来的一瞥。* -- [derwiki](https://news.ycombinator.com/item?id=38205643)
* *它太棒了。它让我可以自由地做我以前觉得超出舒适区的事情。* -- [Dougie](https://discord.com/channels/1131200896827654144/1174002618058678323/1174084556257775656)
* *这个项目很出色。* -- [funkytaco](https://github.com/paul-gauthier/aider/issues/112#issuecomment-1637429008)
* *了不起的项目，绝对是我用过的最好的AI编码助手。* -- [joshuavial](https://github.com/paul-gauthier/aider/issues/84)
* *我绝对喜欢使用Aider...它让软件开发的体验变得轻松多了。* -- [principalideal0](https://discord.com/channels/1131200896827654144/1133421607499595858/1229689636012691468)
* *我一直在从多次肩部手术中恢复...并广泛使用了aider。它让我能够继续保持生产力。* -- [codeninja](https://www.reddit.com/r/OpenAI/s/nmNwkHy1zG)
* *我是aider成瘾者。我完成了更多工作，但用时更少。* -- [dandandan](https://discord.com/channels/1131200896827654144/1131200896827654149/1135913253483069470)
* *在浪费了100美元的代币试图找到更好的东西之后，我又回到了Aider。它完全把其他所有东西都甩在身后，根本没有竞争对手。* -- [SystemSculpt](https://discord.com/channels/1131200896827654144/1131200896827654149/1178736602797846548)
* *在现有代码库中进行实际开发工作的最佳代理。* -- [Nick Dobos](https://twitter.com/NickADobos/status/1690408967963652097?s=20)
