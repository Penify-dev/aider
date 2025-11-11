
# aider - ターミナルでのAIペアプログラミング

Aiderは、ローカルのgitリポジトリに保存されたコードを編集するために、LLMとペアプログラミングができるコマンドラインツールです。
Aiderは、ローカルのソースファイル内のコードを直接編集し、適切なコミットメッセージで[git commitを実行](https://aider.chat/docs/faq.html#how-does-aider-use-git)します。
新しいプロジェクトを始めることも、既存のgitリポジトリで作業することもできます。
Aiderは、[既存の大規模なコードベース](https://aider.chat/docs/repomap.html)への変更を依頼できる点がユニークです。
AiderはGPT-4o、Claude 3 Opus、GPT-3.5で良好に動作し、[ほぼすべてのLLMに接続](https://aider.chat/docs/llms.html)できます。

<p align="center">
  <img src="assets/screencast.svg" alt="aider screencast">
</p>

<p align="center">
  <a href="https://discord.gg/Tv2uQnR88V">
    <img src="https://img.shields.io/badge/Join-Discord-blue.svg"/>
  </a>
</p>

- [はじめに](#はじめに)
- [機能](#機能)
- [使い方](#使い方)
- [チュートリアル動画](https://aider.chat/docs/install.html#tutorial-videos)
- [チャット内コマンド](#チャット内コマンド)
- [ヒント](#ヒント)
- [インストール](https://aider.chat/docs/install.html)
- [LLMへの接続](https://aider.chat/docs/llms.html)
- [LLMリーダーボード](https://aider.chat/docs/leaderboards/)
- [音声からコードへ](https://aider.chat/docs/voice.html)
- [チャット記録の例](https://aider.chat/examples/)
- [FAQ](https://aider.chat/docs/faq.html)
- [Discord](https://discord.gg/Tv2uQnR88V)
- [ブログ](https://aider.chat/blog/)


## はじめに

詳細は[インストール手順](https://aider.chat/docs/install.html)を参照してください。以下のように素早く開始できます：

```
$ pip install aider-chat

# GPT-4oで使用する場合
$ export OPENAI_API_KEY=your-key-goes-here
$ aider

# Claude 3 Opusで使用する場合:
$ export ANTHROPIC_API_KEY=your-key-goes-here
$ aider --opus
```


## 機能

* コマンドラインから`aider <file1> <file2> ...`を実行して、一緒に議論・編集したいソースファイルのセットを指定し、コードについてaiderとチャットできます。AiderはLLMがこれらのファイルの内容を見て編集できるようにします。
* Aiderは、python、javascript、typescript、php、html、cssなど、ほとんどの人気のある言語でコードを書いて編集できます。
* AiderはGPT-4o、Claude 3 Opus、GPT-3.5で良好に動作し、[ほぼすべてのLLMに接続](https://aider.chat/docs/llms.html)できます。
* コードに新機能、変更、改善、またはバグ修正を依頼できます。新しいテストケース、更新されたドキュメント、またはコードのリファクタリングを依頼できます。
* AiderはLLMが提案した編集を、ソースファイルに直接適用します。
* Aiderは[各変更セットを説明的なコミットメッセージと共にローカルgitリポジトリに自動コミット](https://aider.chat/docs/faq.html#how-does-aider-use-git)します。これらの頻繁な自動コミットはセーフティネットを提供します。変更を元に戻したり、標準的なgitワークフローを使用して長い一連の変更を管理したりすることが簡単です。
* 複数のソースファイルを同時にaiderで使用できるため、aiderは1つの変更セット/コミットでそれらすべてに対して協調的なコード変更を行うことができます。
* Aiderは[gitリポジトリ全体のマップをLLMに提供](https://aider.chat/docs/repomap.html)できるため、大規模なコードベースを理解して修正するのに役立ちます。
* aiderとチャットしながら、エディターを使用して手動でファイルを編集することもできます。Aiderはこれらの外部編集に気付き、ファイルの最新バージョンを常に把握します。これにより、aiderチャットとエディターを行き来しながら、LLMと共同でコーディングできます。
* ビジョン対応のOpenAIモデル（GPT-4o、GPT-4 Turboなど）を使用している場合は、画像ファイルをチャットに追加できます。


## 使い方

編集したいソースコードファイルを指定して`aider`を実行します。
これらのファイルは「チャットセッションに追加」され、LLMがその内容を見て、指示に従って編集できるようになります。

```
aider <file1> <file2> ...
```

選択的に、LLMが編集する必要があるファイルだけを追加してください。
無関係なファイルをたくさん追加すると、LLMは混乱する可能性があります（また、より多くのトークンがかかります）。
Aiderは、関連する他のファイルからのスニペットをLLMと自動的に共有するため、[コードベースの残りの部分を理解](https://aider.chat/docs/repomap.html)できます。

gitリポジトリ内の任意の場所でコマンドラインでファイル名を指定せずにaiderを起動することもできます。リポジトリ内のすべてのファイルが検出されます。その後、以下で説明する`/add`および`/drop`チャットコマンドを使用して、チャットセッション内で個別のファイルを追加および削除できます。
あなたまたはLLMが会話の中でリポジトリのファイル名に言及した場合、aiderはそれらをチャットに追加するかどうか尋ねます。

Aiderには、コマンドラインスイッチ、環境変数、または設定ファイルで設定できる他の多くのオプションもあります。
詳細については、`aider --help`を参照してください。


## チャット内コマンド

Aiderは、すべて`/`で始まるチャット内のコマンドをサポートしています。最も便利なチャット内コマンドの一部を次に示します：

* `/add <file>`: 画像ファイルを含む、一致するファイルをチャットセッションに追加します。
* `/drop <file>`: 一致するファイルをチャットセッションから削除します。
* `/undo`: aiderによって行われた最後のgitコミットを元に戻します。
* `/diff`: 最後のaiderコミットの差分を表示します。
* `/run <command>`: シェルコマンドを実行し、オプションで出力をチャットに追加します。
* `/voice`: aiderに話しかけて[音声でコード変更を依頼](https://aider.chat/docs/voice.html)します。
* `/help`: すべてのコマンドに関するヘルプを表示します。

詳細については、[完全なコマンドドキュメント](https://aider.chat/docs/commands.html)を参照してください。


## ヒント

* 変更を行うためにどのファイルを編集する必要があるかを考え、それらをチャットに追加してください。
AiderはLLMが編集するファイルを自分で見つけるのを助けることができますが、最も効率的なアプローチは、必要なファイルを自分でチャットに追加することです。
* 大きな変更は、アプローチと全体的な設計を計画する、思慮深い小さなステップのシーケンスとして実行するのが最適です。ジュニア開発者に対するようにLLMに変更を説明してください。最初にリファクタリングを依頼し、次に実際の変更を依頼します。コードの品質/構造の改善を依頼する時間を取ってください。
* LLMが有用な応答を提供していない場合は、Control-Cを使用して安全に中断してください。部分的な応答は会話に残るため、より多くの情報や指示でLLMに返信するときにそれを参照できます。
* `/run`コマンドを使用して、テスト、リンターなどを実行し、出力をLLMに表示して、問題を修正できるようにします。
* Meta-ENTER（一部の環境ではEsc+ENTER）を使用して、複数行のチャットメッセージを入力します。または、最初の行に`{`だけを入力して複数行メッセージを開始し、最後の行に`}`だけを入力して終了します。
* コードがエラーをスローしている場合は、`/run`を使用するか、チャットに貼り付けてエラー出力をLLMと共有します。LLMにバグを見つけて修正させます。
* LLMは多くの標準ツールやライブラリについて知っていますが、APIや関数の引数に関する細かい詳細を誤る可能性があります。これらの問題を解決するために、ドキュメントのスニペットをチャットに貼り付けることができます。
* LLMは、特に「チャットに追加」したファイルの内容のみを見ることができます。Aiderは[gitリポジトリ全体のマップ](https://aider.chat/docs/repomap.html)も送信します。そのため、LLMは、リクエストに必要だと感じた場合、追加のファイルを見るように依頼することがあります。

## チャット記録の例

[チャット記録の例のページ](https://aider.chat/examples/)では、aiderとチャットしてコードを書いて編集する方法を示しています。

## インストール

[インストール手順](https://aider.chat/docs/install.html)を参照してください。

## FAQ

詳細については、[FAQ](https://aider.chat/docs/faq.html)を参照してください。

## ユーザーからの感想

* *これまでで最高のAIコーディングアシスタント。* -- [Matthew Berman](https://www.youtube.com/watch?v=df8afeb1FY8)
* *断然、これまでで最高のAIコーディングアシスタントツールです。* -- [IndyDevDan](https://www.youtube.com/watch?v=MPYFPvxfGZs)
* *Aider ... は私のコーディング生産性を簡単に4倍にしました。* -- [SOLAR_FIELDS](https://news.ycombinator.com/item?id=36212100)
* *クールなワークフローです... Aiderの人間工学は私にとって完璧です。* -- [qup](https://news.ycombinator.com/item?id=38185326)
* *シニア開発者がGitリポジトリに住んでいるようなものです - 本当に素晴らしい！* -- [rappster](https://github.com/paul-gauthier/aider/issues/124)
* *なんて素晴らしいツールでしょう。信じられません。* -- [valyagolev](https://github.com/paul-gauthier/aider/issues/6#issue-1722897858)
* *Aiderは本当に驚くべきものです！* -- [cgrothaus](https://github.com/paul-gauthier/aider/issues/82#issuecomment-1631876700)
* *最初のいくつかの動作するバージョンを立ち上げて作成するよりもはるかに速かったです。* -- [Daniel Feldman](https://twitter.com/d_feldman/status/1662295077387923456)
* *Aiderに感謝します！コーディングの未来を垣間見ているような気がします。* -- [derwiki](https://news.ycombinator.com/item?id=38205643)
* *ただ素晴らしいです。以前は快適ゾーンの外にあると感じていたことができるようになりました。* -- [Dougie](https://discord.com/channels/1131200896827654144/1174002618058678323/1174084556257775656)
* *このプロジェクトは素晴らしいです。* -- [funkytaco](https://github.com/paul-gauthier/aider/issues/112#issuecomment-1637429008)
* *素晴らしいプロジェクト、間違いなく私が使った中で最高のAIコーディングアシスタントです。* -- [joshuavial](https://github.com/paul-gauthier/aider/issues/84)
* *Aiderを使うのが本当に大好きです...ソフトウェア開発が体験として非常に軽く感じられます。* -- [principalideal0](https://discord.com/channels/1131200896827654144/1133421607499595858/1229689636012691468)
* *複数の肩の手術から回復していて...aiderを広く使用しています。生産性を維持できました。* -- [codeninja](https://www.reddit.com/r/OpenAI/s/nmNwkHy1zG)
* *私はaider中毒です。より多くの仕事を、より短い時間で終わらせています。* -- [dandandan](https://discord.com/channels/1131200896827654144/1131200896827654149/1135913253483069470)
* *より良いものを見つけようとして$100をトークンに浪費した後、Aiderに戻りました。他のものを完全に吹き飛ばしています、競争相手はいません。* -- [SystemSculpt](https://discord.com/channels/1131200896827654144/1131200896827654149/1178736602797846548)
* *既存のコードベースでの実際の開発作業のための最高のエージェント。* -- [Nick Dobos](https://twitter.com/NickADobos/status/1690408967963652097?s=20)
