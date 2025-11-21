# aider 是您终端中的 AI 结对编程

Aider 是一个命令行工具，让您与 LLM 结对编程，
编辑存储在本地 git 仓库中的代码。
Aider 将直接编辑本地源文件中的代码，
并 [使用合理的提交消息提交更改](https://aider.chat/docs/faq.html#how-does-aider-use-git)。
您可以开始一个新项目或使用现有的 git 仓库。
Aider 的独特之处在于，它允许您请求对 [预先存在的较大代码库](https://aider.chat/docs/repomap.html) 进行更改。
Aider 与 GPT-4o、Claude 3 Opus、GPT-3.5 配合良好
并支持 [连接到几乎任何 LLM](https://aider.chat/docs/llms.html)。

<p align="center">
  <img src="assets/screencast.svg" alt="aider screencast">
</p>

<p align="center">
  <a href="https://discord.gg/Tv2uQnR88V">
    <img src="https://img.shields.io/badge/Join-Discord-blue.svg"/>
  </a>
</p>

- [入门](#getting-started)
- [功能](#features)
- [使用](#usage)
- [教程视频](https://aider.chat/docs/install.html#tutorial-videos)
- [聊天中命令](#in-chat-commands)
- [提示](#tips)
- [安装](https://aider.chat/docs/install.html)
- [连接到 LLM](https://aider.chat/docs/llms.html)
- [LLM 排行榜](https://aider.chat/docs/leaderboards/)
- [语音转代码](https://aider.chat/docs/voice.html)
- [示例聊天记录](https://aider.chat/examples/)
- [FAQ](https://aider.chat/docs/faq.html)
- [Discord](https://discord.gg/Tv2uQnR88V)
- [博客](https://aider.chat/blog/)


## 入门

请参阅
[安装说明](https://aider.chat/docs/install.html)
以获取更多详细信息，但您可以
像这样快速开始：

```
$ pip install aider-chat

# 使用 GPT-4o
$ export OPENAI_API_KEY=your-key-goes-here
$ aider

# 使用 Claude 3 Opus：
$ export ANTHROPIC_API_KEY=your-key-goes-here
$ aider --opus
```


## 功能

* 通过运行 `aider <file1> <file2> ...` 从命令行与 aider 聊天，讨论和一起编辑一组源文件。Aider 让 LLM 看到并编辑这些文件的内容。
* Aider 可以编写和编辑大多数流行语言的代码：python、javascript、typescript、php、html、css 等。
* Aider 与 GPT-4o、Claude 3 Opus、GPT-3.5 配合良好，并支持 [连接到几乎任何 LLM](https://aider.chat/docs/llms.html)。
* 请求新功能、更改、改进或代码错误修复。请求新的测试用例、更新的文档或代码重构。
* Aider 将 LLM 建议的编辑直接应用到您的源文件。
* Aider 将 [自动将每个变更集提交到您的本地 git 仓库](https://aider.chat/docs/faq.html#how-does-aider-use-git)，并附带描述性提交消息。这些频繁的自动提交提供了安全网。很容易撤销更改或使用标准 git 工作流来管理更长的更改序列。
* 您可以一次使用多个源文件与 aider 一起使用，因此 aider 可以在单个变更集/提交中对所有文件进行协调代码更改。
* Aider 可以 [为 LLM 提供整个 git 仓库的地图](https://aider.chat/docs/repomap.html)，这有助于它理解和修改大型代码库。
* 您也可以在与 aider 聊天时手动使用编辑器编辑文件。Aider 会注意到这些带外编辑，并保持与文件最新版本的同步。这让您可以在 aider 聊天和编辑器之间来回切换，与 LLM 协作编码。
* 如果您使用具有视觉能力的 OpenAI 模型（GPT-4o、GPT-4 Turbo 等），您可以将图像文件添加到聊天中。


## 使用

使用您想要编辑的源代码文件运行 `aider`。
这些文件将被“添加到聊天会话”，以便 LLM 可以看到它们
的内容，并根据您的指示编辑它们。

```
aider <file1> <file2> ...
```

要选择性，只添加 LLM 需要编辑的文件。
如果您添加了一堆不相关的文件，LLM 可能会感到不知所措
和困惑（并且成本更多令牌）。
Aider 将自动
与 LLM 共享其他相关文件的片段，以便它可以
[理解您的代码库的其余部分](https://aider.chat/docs/repomap.html)。

您也可以只在 git 仓库中的任何地方启动 aider，而不命名
命令行上的文件。它将发现仓库中的所有文件。然后，您可以使用下面的 `/add` 和 `/drop` 聊天命令在聊天会话中添加和删除单个文件。
如果您或 LLM 在对话中提到任何仓库的文件名，
aider 会询问您是否要将它们添加到聊天中。

Aider 还有许多其他选项，可以通过
命令行开关、环境变量或配置文件设置。
请参阅 `aider --help` 以获取详细信息。


## 聊天中命令

Aider 支持从聊天中开始的命令，所有命令都以 `/` 开头。这里是一些最有用的聊天中命令：

* `/add <file>`: 将匹配的文件添加到聊天会话，包括图像文件。
* `/drop <file>`: 从聊天会话中删除匹配的文件。
* `/undo`: 如果是由 aider 完成的，则撤销最后一个 git 提交。
* `/diff`: 显示最后一个 aider 提交的差异。
* `/run <command>`: 运行 shell 命令，并可选地将输出添加到聊天中。
* `/voice`: 与 aider 说话以 [使用您的声音请求代码更改](https://aider.chat/docs/voice.html)。
* `/help`: 显示所有命令的帮助。

请参阅 [完整命令文档](https://aider.chat/docs/commands.html) 以获取更多信息。


## 提示

* 考虑哪些文件需要编辑以进行更改，并将它们添加到聊天中。
Aider 可以帮助 LLM 自己找出要编辑的文件，但最有效的方法是自己将所需的文件添加到聊天中。
* 大型更改最好作为一系列深思熟虑的小步骤执行，您计划方法和整体设计。与 LLM 一起逐步更改，就像与初级开发人员一样。请求重构以准备，然后请求实际更改。花时间请求代码质量/结构改进。
* 如果 LLM 没有提供有用的响应，请使用 Control-C 安全中断 LLM。部分响应保留在对话中，因此当您回复 LLM 时，您可以参考它以提供更多信息或方向。
* 使用 `/run` 命令运行测试、linter 等，并向 LLM 显示输出，以便它可以修复任何问题。
* 使用 Meta-ENTER（在某些环境中为 Esc+ENTER）输入多行聊天消息。或者在第一行输入 `{` 单独开始多行消息，并在最后一行输入 `}` 单独结束。
* 如果您的代码抛出错误，请使用 `/run` 或将其粘贴到聊天中与 LLM 共享错误输出。让 LLM 找出并修复错误。
* LLM 知道很多标准工具和库，但可能对 API 和函数参数的细微细节有误。您可以将文档片段粘贴到聊天中以解决这些问题。
* LLM 只能看到您专门“添加到聊天”的文件的内容。Aider 还发送了 [整个 git 仓库的地图](https://aider.chat/docs/repomap.html)。因此，如果 LLM 觉得需要，它可能会要求查看其他文件。


## 示例聊天记录

[示例记录页面](https://aider.chat/examples/) 显示了如何与 aider 聊天以编写
和编辑代码。

## 安装

请参阅 [安装说明](https://aider.chat/docs/install.html)。

## FAQ

有关更多信息，请参阅 [FAQ](https://aider.chat/docs/faq.html)。

## 用户的好话

* *到目前为止最好的 AI 编码助手。* -- [Matthew Berman](https://www.youtube.com/watch?v=df8afeb1FY8)
* *毫无疑问，这是迄今为止最好的 AI 编码助手工具。* -- [IndyDevDan](https://www.youtube.com/watch?v=MPYFPvxfGZs)
* *Aider ... 轻松地将我的编码生产力提高了四倍。* -- [SOLAR_FIELDS](https://news.ycombinator.com/item?id=36212100)
* *这是一个很酷的工作流程... Aider 的人体工程学对我来说是完美的。* -- [qup](https://news.ycombinator.com/item?id=38185326)
* *这真的就像让你的高级开发人员住在你的 Git 仓库里 - 真的很棒！* -- [rappster](https://github.com/paul-gauthier/aider/issues/124)
* *多么惊人的工具。它令人难以置信。* -- [valyagolev](https://github.com/paul-gauthier/aider/issues/6#issue-1722897858)
* *Aider 是如此令人惊叹的东西！* -- [cgrothaus](https://github.com/paul-gauthier/aider/issues/82#issuecomment-1631876700)
* *它比我自己起步和制作前几个工作版本要快得多。* -- [Daniel Feldman](https://twitter.com/d_feldman/status/1662295077387923456)
* *感谢 Aider！它真的感觉像是对编码未来的瞥见。* -- [derwiki](https://news.ycombinator.com/item?id=38205643)
* *它太棒了。它让我可以做以前觉得超出我舒适区的事情。* -- [Dougie](https://discord.com/channels/1131200896827654144/1174002618058678323/1174084556257775656)
* *这个项目是杰出的。* -- [funkytaco](https://github.com/paul-gauthier/aider/issues/112#issuecomment-1637429008)
* *惊人的项目，肯定是我用过的最好的 AI 编码助手。* -- [joshuavial](https://github.com/paul-gauthier/aider/issues/84)
* *我绝对喜欢使用 Aider ... 它让软件开发感觉轻得多。* -- [principalideal0](https://discord.com/channels/1131200896827654144/1133421607499595858/1229689636012691468)
* *我正在从多次肩部手术中恢复 ... 并广泛使用了 aider。它让我能够继续生产力。* -- [codeninja](https://www.reddit.com/r/OpenAI/s/nmNwkHy1zG)
* *我是一个 aider 瘾君子。我在更短的时间内完成了更多工作。* -- [dandandan](https://discord.com/channels/1131200896827654144/1131200896827654149/1135913253483069470)
* *在浪费了 100 美元的令牌试图找到更好的东西后，我回到了 Aider。它绝对把其他一切都吹走了，没有任何竞争。* -- [SystemSculpt](https://discord.com/channels/1131200896827654144/1131200896827654149/1178736602797846548)
* *现有代码库中实际开发工作的最佳代理。* -- [Nick Dobos](https://twitter.com/NickADobos/status/1690408967963652097?s=20)