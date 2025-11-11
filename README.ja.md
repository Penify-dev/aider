
# aider - ターミナルで使えるAIペアプログラミングツール

Aiderは、ローカルのgitリポジトリに保存されたコードを編集するために、LLM（大規模言語モデル）とペアプログラミングができるコマンドラインツールです。
Aiderはローカルのソースファイル内のコードを直接編集し、適切なコミットメッセージで[gitコミット](https://aider.chat/docs/faq.html#how-does-aider-use-git)を行います。
新しいプロジェクトを始めることも、既存のgitリポジトリで作業することもできます。
Aiderは、[既存の大規模なコードベース](https://aider.chat/docs/repomap.html)への変更を依頼できる点で他と異なります。
AiderはGPT-4o、Claude 3 Opus、GPT-3.5で良好に動作し、[ほぼすべてのLLMへの接続](https://aider.chat/docs/llms.html)をサポートしています。

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
- [音声コーディング](https://aider.chat/docs/voice.html)
- [チャットの例](https://aider.chat/examples/)
- [よくある質問](https://aider.chat/docs/faq.html)
- [Discord](https://discord.gg/Tv2uQnR88V)
- [ブログ](https://aider.chat/blog/)


## はじめに

詳細は[インストール手順](https://aider.chat/docs/install.html)を参照してください。
以下のように簡単に始めることができます：

```
$ pip install aider-chat

# GPT-4oを使用する場合
$ export OPENAI_API_KEY=your-key-goes-here
$ aider

# Claude 3 Opusを使用する場合：
$ export ANTHROPIC_API_KEY=your-key-goes-here
$ aider --opus
```


## 機能

* コマンドラインから `aider <file1> <file2> ...` を実行し、一緒に議論・編集したいソースファイルのセットを指定してコードについてチャットできます。AiderはLLMがこれらのファイルの内容を見て編集することを可能にします。
* Aiderは、Python、JavaScript、TypeScript、PHP、HTML、CSSなど、ほとんどの主要な言語でコードを書き、編集できます。
* AiderはGPT-4o、Claude 3 Opus、GPT-3.5で良好に動作し、[ほぼすべてのLLMへの接続](https://aider.chat/docs/llms.html)をサポートしています。
* コードに対して新機能、変更、改善、バグ修正を依頼できます。新しいテストケース、更新されたドキュメント、コードのリファクタリングも依頼できます。
* AiderはLLMが提案した編集をソースファイルに直接適用します。
* Aiderは[各変更セットを説明的なコミットメッセージと共にローカルgitリポジトリに自動コミット](https://aider.chat/docs/faq.html#how-does-aider-use-git)します。これらの頻繁な自動コミットはセーフティネットを提供します。変更を簡単に元に戻したり、標準のgitワークフローを使用して長い変更シーケンスを管理できます。
* 複数のソースファイルを一度に使用できるため、Aiderはすべてのファイルにわたって協調的なコード変更を単一の変更セット/コミットで行うことができます。
* Aiderは[gitリポジトリ全体のマップをLLMに提供](https://aider.chat/docs/repomap.html)でき、大規模なコードベースの理解と変更に役立ちます。
* Aiderとチャットしながら、エディタを使用して手動でファイルを編集することもできます。Aiderはこれらの帯域外編集に気づき、ファイルの最新バージョンを最新の状態に保ちます。これにより、Aiderチャットとエディタの間を行き来して、LLMと協力してコーディングできます。
* ビジョン対応のOpenAIモデル（GPT-4o、GPT-4 Turboなど）を使用している場合、画像ファイルをチャットに追加できます。


## 使い方

編集したいソースコードファイルを指定して `aider` を実行します。
これらのファイルは「チャットセッションに追加」され、LLMがその内容を見て、あなたの指示に従って編集できるようになります。

```
aider <file1> <file2> ...
```

LLMが編集する必要があるファイルだけを選択的に追加してください。
無関係なファイルをたくさん追加すると、LLMが圧倒されて混乱する可能性があります（そしてトークンのコストも増えます）。
Aiderは自動的に関連する他のファイルからのスニペットをLLMと共有し、[コードベースの残りを理解](https://aider.chat/docs/repomap.html)できるようにします。

コマンドラインでファイルを指定せずに、gitリポジトリ内の任意の場所でaiderを起動することもできます。リポジトリ内のすべてのファイルを検出します。その後、後述の `/add` および `/drop` チャットコマンドを使用して、チャットセッション内で個別のファイルを追加・削除できます。
会話の中であなたやLLMがリポジトリのファイル名のいずれかに言及した場合、aiderはそれをチャットに追加するかどうか尋ねます。

Aiderには、コマンドラインスイッチ、環境変数、または設定ファイルで設定できる他の多くのオプションもあります。
詳細は `aider --help` を参照してください。


## チャット内コマンド

Aiderはチャット内からのコマンドをサポートしており、すべて `/` で始まります。最も有用なチャット内コマンドは以下の通りです：

* `/add <file>`: 画像ファイルを含む、一致するファイルをチャットセッションに追加します。
* `/drop <file>`: 一致するファイルをチャットセッションから削除します。
* `/undo`: aiderが行った最後のgitコミットを取り消します。
* `/diff`: 最後のaiderコミットの差分を表示します。
* `/run <command>`: シェルコマンドを実行し、オプションで出力をチャットに追加します。
* `/voice`: aiderに話しかけて[音声でコード変更を依頼](https://aider.chat/docs/voice.html)します。
* `/help`: すべてのコマンドに関するヘルプを表示します。

詳細は[完全なコマンドドキュメント](https://aider.chat/docs/commands.html)を参照してください。


## ヒント

* 変更を行うためにどのファイルを編集する必要があるかを考え、それらをチャットに追加してください。
Aiderは、LLMがどのファイルを編集すべきかを自力で理解するのを助けることができますが、最も効率的なアプローチは、必要なファイルを自分でチャットに追加することです。
* 大きな変更は、アプローチと全体的な設計を計画する、慎重な一口サイズのステップのシーケンスとして実行するのが最適です。ジュニア開発者に対して行うように、LLMを変更に導いてください。準備のためにリファクタリングを依頼してから、実際の変更を依頼してください。コード品質/構造の改善を依頼する時間を取ってください。
* LLMが有用な応答を提供していない場合は、Control-Cを使用して安全に中断してください。部分的な応答は会話に残るため、より多くの情報や方向性を提供してLLMに返信するときに参照できます。
* `/run` コマンドを使用してテストやリンターなどを実行し、出力をLLMに表示して問題を修正させることができます。
* Meta-ENTER（一部の環境ではEsc+ENTER）を使用して、複数行のチャットメッセージを入力します。または、最初の行に `{` だけを入力して複数行メッセージを開始し、最後の行に `}` だけを入力して終了します。
* コードがエラーを投げている場合は、`/run` を使用するか、チャットに貼り付けて、LLMとエラー出力を共有してください。LLMにバグを見つけて修正させましょう。
* LLMは多くの標準ツールやライブラリについて知っていますが、APIや関数の引数に関する細かい詳細の一部を間違える可能性があります。これらの問題を解決するために、ドキュメントのスニペットをチャットに貼り付けることができます。
* LLMは、あなたが具体的に「チャットに追加」したファイルの内容のみを見ることができます。Aiderは[gitリポジトリ全体のマップ](https://aider.chat/docs/repomap.html)も送信します。したがって、LLMはあなたのリクエストに必要だと感じた場合、追加のファイルを見たいと依頼することがあります。

## チャットの例

[チャット例のページ](https://aider.chat/examples/)では、aiderとチャットしてコードを書いたり編集したりする方法を示しています。

## インストール

[インストール手順](https://aider.chat/docs/install.html)を参照してください。

## よくある質問

詳細については、[よくある質問](https://aider.chat/docs/faq.html)を参照してください。

## ユーザーからの好意的なコメント

* *これまでで最高のAIコーディングアシスタント。* -- [Matthew Berman](https://www.youtube.com/watch?v=df8afeb1FY8)
* *間違いなく、これまでで最高のAIコーディングアシスタントツール。* -- [IndyDevDan](https://www.youtube.com/watch?v=MPYFPvxfGZs)
* *Aider ... は私のコーディング生産性を簡単に4倍にしました。* -- [SOLAR_FIELDS](https://news.ycombinator.com/item?id=36212100)
* *クールなワークフローです... Aiderのエルゴノミクスは私にとって完璧です。* -- [qup](https://news.ycombinator.com/item?id=38185326)
* *本当にシニア開発者がGitリポジトリの中に住んでいるような感じ - 本当に素晴らしい！* -- [rappster](https://github.com/paul-gauthier/aider/issues/124)
* *なんて素晴らしいツールだ。信じられない。* -- [valyagolev](https://github.com/paul-gauthier/aider/issues/6#issue-1722897858)
* *Aiderは驚くべきものです！* -- [cgrothaus](https://github.com/paul-gauthier/aider/issues/82#issuecomment-1631876700)
* *立ち上げて最初のいくつかの動作するバージョンを作るのが、私が行うよりもはるかに速かった。* -- [Daniel Feldman](https://twitter.com/d_feldman/status/1662295077387923456)
* *Aiderをありがとう！本当にコーディングの未来を垣間見るような感じです。* -- [derwiki](https://news.ycombinator.com/item?id=38205643)
* *ただただ素晴らしい。以前は快適ゾーンの外にあると感じていたことを自由にできるようになりました。* -- [Dougie](https://discord.com/channels/1131200896827654144/1174002618058678323/1174084556257775656)
* *このプロジェクトは素晴らしい。* -- [funkytaco](https://github.com/paul-gauthier/aider/issues/112#issuecomment-1637429008)
* *素晴らしいプロジェクト、間違いなく私が使った中で最高のAIコーディングアシスタント。* -- [joshuavial](https://github.com/paul-gauthier/aider/issues/84)
* *Aiderを使うのが大好きです... ソフトウェア開発が体験としてとても軽く感じられます。* -- [principalideal0](https://discord.com/channels/1131200896827654144/1133421607499595858/1229689636012691468)
* *私は複数の肩の手術から回復中で... aiderを広範囲に使用してきました。生産性を維持し続けることができました。* -- [codeninja](https://www.reddit.com/r/OpenAI/s/nmNwkHy1zG)
* *私はaider中毒です。より多くの仕事をこなしていますが、より少ない時間で。* -- [dandandan](https://discord.com/channels/1131200896827654144/1131200896827654149/1135913253483069470)
* *より良いものを見つけようとしてトークンに100ドルを無駄にした後、Aiderに戻りました。他のすべてを圧倒的に上回り、競争相手は全くいません。* -- [SystemSculpt](https://discord.com/channels/1131200896827654144/1131200896827654149/1178736602797846548)
* *既存のコードベースでの実際の開発作業に最適なエージェント。* -- [Nick Dobos](https://twitter.com/NickADobos/status/1690408967963652097?s=20)
