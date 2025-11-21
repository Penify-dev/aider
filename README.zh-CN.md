
# aider 是您终端中的 AI 结对编程工具

Aider 是一个命令行工具，让您可以与大语言模型（LLM）结对编程，编辑存储在本地 git 仓库中的代码。
Aider 会直接编辑您本地源文件中的代码，并使用合理的提交信息[自动 git 提交更改](https://aider.chat/docs/faq.html#how-does-aider-use-git)。
您可以开始一个新项目或使用现有的 git 仓库。
Aider 的独特之处在于它可以让您请求对[已存在的大型代码库](https://aider.chat/docs/repomap.html)进行更改。
Aider 与 GPT-4o、Claude 3 Opus、GPT-3.5 配合良好，并支持[连接到几乎任何 LLM](https://aider.chat/docs/llms.html)。

<p align="center">
  <img src="assets/screencast.svg" alt="aider 演示">
</p>

<p align="center">
  <a href="https://discord.gg/Tv2uQnR88V">
    <img src="https://img.shields.io/badge/Join-Discord-blue.svg"/>
  </a>
</p>

- [快速开始](#快速开始)
- [功能特性](#功能特性)
- [使用方法](#使用方法)
- [教程视频](https://aider.chat/docs/install.html#tutorial-videos)
- [聊天命令](#聊天命令)
- [使用技巧](#使用技巧)
- [安装说明](https://aider.chat/docs/install.html)
- [连接到 LLM](https://aider.chat/docs/llms.html)
- [LLM 排行榜](https://aider.chat/docs/leaderboards/)
- [语音编程](https://aider.chat/docs/voice.html)
- [聊天记录示例](https://aider.chat/examples/)
- [常见问题](https://aider.chat/docs/faq.html)
- [Discord 社区](https://discord.gg/Tv2uQnR88V)
- [博客](https://aider.chat/blog/)


## 快速开始

查看[安装说明](https://aider.chat/docs/install.html)了解更多详情，您可以这样快速开始：

```
$ pip install aider-chat

# 使用 GPT-4o
$ export OPENAI_API_KEY=your-key-goes-here
$ aider 

# 使用 Claude 3 Opus：
$ export ANTHROPIC_API_KEY=your-key-goes-here
$ aider --opus
```


## 功能特性

* 通过在命令行运行 `aider <file1> <file2> ...` 与 aider 讨论您的代码，指定一组要一起讨论和编辑的源文件。Aider 让 LLM 能够查看和编辑这些文件的内容。
* Aider 可以编写和编辑大多数流行语言的代码：python、javascript、typescript、php、html、css 等。
* Aider 与 GPT-4o、Claude 3 Opus、GPT-3.5 配合良好，并支持[连接到几乎任何 LLM](https://aider.chat/docs/llms.html)。
* 请求新功能、更改、改进或修复代码中的错误。要求新的测试用例、更新文档或代码重构。
* Aider 会将 LLM 建议的编辑直接应用到您的源文件中。
* Aider 会[自动将每个变更集提交到您的本地 git 仓库](https://aider.chat/docs/faq.html#how-does-aider-use-git)，并附带描述性的提交信息。这些频繁的自动提交提供了一个安全网。撤销更改或使用标准 git 工作流程管理更长的更改序列都很容易。
* 您可以同时使用多个源文件与 aider 协作，因此 aider 可以在单个变更集/提交中对所有文件进行协调的代码更改。
* Aider 可以[为 LLM 提供整个 git 仓库的映射](https://aider.chat/docs/repomap.html)，这有助于它理解和修改大型代码库。
* 您还可以在与 aider 聊天时使用编辑器手动编辑文件。Aider 会注意到这些带外编辑，并与文件的最新版本保持同步。这让您可以在 aider 聊天和编辑器之间来回切换，与 LLM 协作编程。
* 如果您使用支持视觉功能的 OpenAI 模型（GPT-4o、GPT-4 Turbo 等），可以将图像文件添加到聊天中。


## 使用方法

使用您想要编辑的源代码文件运行 `aider`。
这些文件将被"添加到聊天会话"，以便 LLM 可以查看它们的内容并根据您的指示进行编辑。

```
aider <file1> <file2> ...
```

要有选择性，只添加 LLM 需要编辑的文件。
如果您添加一堆不相关的文件，LLM 可能会不知所措和困惑（而且会花费更多 token）。
Aider 会自动与 LLM 共享来自其他相关文件的代码片段，以便它可以[理解您代码库的其余部分](https://aider.chat/docs/repomap.html)。

您也可以在 git 仓库的任何位置启动 aider，而无需在命令行上指定文件。它会发现仓库中的所有文件。然后，您可以使用下面描述的 `/add` 和 `/drop` 聊天命令在聊天会话中添加和删除单个文件。
如果您或 LLM 在对话中提到仓库的任何文件名，aider 会询问您是否要将它们添加到聊天中。

Aider 还有许多其他选项，可以通过命令行开关、环境变量或配置文件设置。
有关详细信息，请参阅 `aider --help`。


## 聊天命令

Aider 支持聊天中的命令，所有命令都以 `/` 开头。以下是一些最有用的聊天命令：

* `/add <file>`：将匹配的文件添加到聊天会话，包括图像文件。
* `/drop <file>`：从聊天会话中删除匹配的文件。
* `/undo`：撤销 aider 完成的最后一次 git 提交。
* `/diff`：显示 aider 最后一次提交的差异。
* `/run <command>`：运行 shell 命令，并可选择将输出添加到聊天中。
* `/voice`：对 aider 说话以[使用语音请求代码更改](https://aider.chat/docs/voice.html)。
* `/help`：显示所有命令的帮助信息。

有关更多信息，请参阅[完整命令文档](https://aider.chat/docs/commands.html)。


## 使用技巧

* 考虑需要编辑哪些文件来进行更改，并将它们添加到聊天中。Aider 可以帮助 LLM 自己找出要编辑哪些文件，但最有效的方法是您自己将所需的文件添加到聊天中。
* 大型更改最好作为一系列深思熟虑的小步骤来执行，您需要规划方法和整体设计。像指导初级开发人员一样引导 LLM 进行更改。先要求重构准备，然后要求实际更改。花时间要求代码质量/结构改进。
* 如果 LLM 没有提供有用的响应，请使用 Control-C 安全地中断它。部分响应会保留在对话中，因此当您向 LLM 回复更多信息或指导时可以引用它。
* 使用 `/run` 命令运行测试、linter 等，并将输出显示给 LLM，以便它可以修复任何问题。
* 使用 Meta-ENTER（在某些环境中为 Esc+ENTER）输入多行聊天消息。或者在第一行单独输入 `{` 开始多行消息，在最后一行单独输入 `}` 结束它。
* 如果您的代码抛出错误，请使用 `/run` 或将其粘贴到聊天中与 LLM 共享错误输出。让 LLM 找出并修复错误。
* LLM 了解许多标准工具和库，但可能会在 API 和函数参数的一些细节上出错。您可以将文档片段粘贴到聊天中以解决这些问题。
* LLM 只能看到您特别"添加到聊天"的文件内容。Aider 还会发送[整个 git 仓库的映射](https://aider.chat/docs/repomap.html)。因此，如果 LLM 认为您的请求需要，它可能会要求查看其他文件。

## 聊天记录示例

[示例记录页面](https://aider.chat/examples/)展示了如何与 aider 聊天来编写和编辑代码。

## 安装说明

请参阅[安装说明](https://aider.chat/docs/install.html)。

## 常见问题

有关更多信息，请参阅[常见问题](https://aider.chat/docs/faq.html)。

## 用户好评

* *迄今为止最好的 AI 编程助手。* -- [Matthew Berman](https://www.youtube.com/watch?v=df8afeb1FY8)
* *毫无疑问，这是迄今为止最好的 AI 编程助手工具。* -- [IndyDevDan](https://www.youtube.com/watch?v=MPYFPvxfGZs)
* *Aider ... 轻松地将我的编程效率提高了四倍。* -- [SOLAR_FIELDS](https://news.ycombinator.com/item?id=36212100)
* *这是一个很酷的工作流程... Aider 的人体工程学对我来说是完美的。* -- [qup](https://news.ycombinator.com/item?id=38185326)
* *这真的就像让您的高级开发人员直接住在您的 Git 仓库中 - 真是太棒了！* -- [rappster](https://github.com/paul-gauthier/aider/issues/124)
* *多么神奇的工具。太不可思议了。* -- [valyagolev](https://github.com/paul-gauthier/aider/issues/6#issue-1722897858)
* *Aider 是一个如此令人惊叹的东西！* -- [cgrothaus](https://github.com/paul-gauthier/aider/issues/82#issuecomment-1631876700)
* *它比我自己上手并制作前几个工作版本要快得多。* -- [Daniel Feldman](https://twitter.com/d_feldman/status/1662295077387923456)
* *感谢您开发 Aider！它真的让人感觉像是瞥见了编程的未来。* -- [derwiki](https://news.ycombinator.com/item?id=38205643)
* *太棒了。它让我能够做以前觉得超出舒适区的事情。* -- [Dougie](https://discord.com/channels/1131200896827654144/1174002618058678323/1174084556257775656)
* *这个项目非常出色。* -- [funkytaco](https://github.com/paul-gauthier/aider/issues/112#issuecomment-1637429008)
* *了不起的项目，绝对是我用过的最好的 AI 编程助手。* -- [joshuavial](https://github.com/paul-gauthier/aider/issues/84)
* *我绝对喜欢使用 Aider ... 它让软件开发体验变得如此轻松。* -- [principalideal0](https://discord.com/channels/1131200896827654144/1133421607499595858/1229689636012691468)
* *我一直在从多次肩部手术中恢复 ... 并广泛使用了 aider。它让我能够继续保持生产力。* -- [codeninja](https://www.reddit.com/r/OpenAI/s/nmNwkHy1zG)
* *我是 aider 的忠实粉丝。我完成了更多的工作，但花费的时间更少。* -- [dandandan](https://discord.com/channels/1131200896827654144/1131200896827654149/1135913253483069470)
* *在浪费了 100 美元的 token 试图找到更好的东西之后，我又回到了 Aider。它完全碾压其他所有工具，根本没有竞争对手。* -- [SystemSculpt](https://discord.com/channels/1131200896827654144/1131200896827654149/1178736602797846548)
* *在现有代码库中进行实际开发工作的最佳代理。* -- [Nick Dobos](https://twitter.com/NickADobos/status/1690408967963652097?s=20)
