# aider - ターミナルでのAIペアプログラミング

Aiderは、ローカルのgitリポジトリに保存されたコードを編集するために、LLMとペアプログラミングができるコマンドラインツールです。
Aiderはローカルのソースファイル内のコードを直接編集し、
適切なコミットメッセージで[git commit変更](https://aider.chat/docs/faq.html#how-does-aider-use-git)を行います。
新しいプロジェクトを始めることも、既存のgitリポジトリで作業することもできます。
Aiderは[既存の大規模なコードベース](https://aider.chat/docs/repomap.html)への変更を依頼できる点でユニークです。
AiderはGPT-4o、Claude 3 Opus、GPT-3.5で良好に動作し、
[ほぼすべてのLLMへの接続](https://aider.chat/docs/llms.html)をサポートしています。

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

詳細は[インストール手順](https://aider.chat/docs/install.html)を参照してください。
以下のように素早く始めることができます：

```
$ pip install aider-chat

# GPT-4oで作業する場合
$ export OPENAI_API_KEY=your-key-goes-here
$ aider

# Claude 3 Opusで作業する場合:
$ export ANTHROPIC_API_KEY=your-key-goes-here
$ aider --opus
```


## 機能

* コマンドラインから`aider <file1> <file2> ...`を実行して、一緒に議論・編集したいソースファイルのセットを指定し、aiderとコードについてチャットできます。AiderはLLMがこれらのファイルの内容を見て編集できるようにします。
* Aiderは最も人気のある言語でコードを書いて編集できます：Python、JavaScript、TypeScript、PHP、HTML、CSSなど。
* AiderはGPT-4o、Claude 3 Opus、GPT-3.5で良好に動作し、[ほぼすべてのLLMへの接続](https://aider.chat/docs/llms.html)をサポートしています。
* コードに対する新機能、変更、改善、またはバグ修正を依頼できます。新しいテストケース、更新されたドキュメント、コードのリファクタリングを依頼することもできます。
* AiderはLLMが提案した編集をソースファイルに直接適用します。
* Aiderは[各変更セットをローカルのgitリポジトリに自動的にコミット](https://aider.chat/docs/faq.html#how-does-aider-use-git)し、説明的なコミットメッセージを付けます。これらの頻繁な自動コミットはセーフティネットを提供します。変更を元に戻したり、標準的なgitワークフローを使用して長い変更シーケンスを管理したりすることが簡単です。
* 一度に複数のソースファイルでaiderを使用できるため、aiderはそれらすべてにわたって調整されたコード変更を1つの変更セット/コミットで行うことができます。
* Aiderは[LLMにgitリポジトリ全体のマップを提供](https://aider.chat/docs/repomap.html)でき、大規模なコードベースを理解して変更するのに役立ちます。
* aiderとチャットしながら、エディタを使用してファイルを手動で編集することもできます。Aiderはこれらの帯域外編集に気づき、ファイルの最新バージョンを常に把握します。これにより、aiderチャットとエディタの間を行き来して、LLMと協力してコーディングできます。
* 視覚対応のOpenAIモデル（GPT-4o、GPT-4 Turboなど）を使用している場合、チャットに画像ファイルを追加できます。


## 使い方

編集したいソースコードファイルを指定して`aider`を実行します。
これらのファイルは「チャットセッションに追加」され、LLMがその内容を確認し、
あなたの指示に従って編集できるようになります。

```
aider <file1> <file2> ...
```

慎重に選択し、LLMが編集する必要のあるファイルだけを追加してください。
関連のないファイルをたくさん追加すると、LLMが圧倒されて
混乱する可能性があります（そしてより多くのトークンがかかります）。
Aiderは自動的に
他の関連ファイルからスニペットをLLMと共有し、
[コードベースの残りの部分を理解](https://aider.chat/docs/repomap.html)できるようにします。

gitリポジトリ内のどこでも、コマンドラインでファイルを指定せずにaiderを起動することもできます。
リポジトリ内のすべてのファイルを検出します。その後、下記の`/add`および`/drop`チャットコマンドを使用して、
チャットセッション内で個々のファイルを追加および削除できます。
あなたまたはLLMが会話中にリポジトリのファイル名を言及すると、
aiderはそれらをチャットに追加したいかどうかを尋ねます。

Aiderには、コマンドラインスイッチ、環境変数、または設定ファイルを介して設定できる
他の多くのオプションもあります。
詳細については`aider --help`を参照してください。


## チャット内コマンド

Aiderはチャット内からのコマンドをサポートしており、すべて`/`で始まります。最も有用なチャット内コマンドのいくつかを以下に示します：

* `/add <file>`: 画像ファイルを含む、一致するファイルをチャットセッションに追加します。
* `/drop <file>`: 一致するファイルをチャットセッションから削除します。
* `/undo`: aiderによって行われた最後のgitコミットを元に戻します。
* `/diff`: 最後のaiderコミットのdiffを表示します。
* `/run <command>`: シェルコマンドを実行し、オプションで出力をチャットに追加します。
* `/voice`: aiderに話しかけて[音声でコード変更を依頼](https://aider.chat/docs/voice.html)します。
* `/help`: すべてのコマンドに関するヘルプを表示します。

詳細については[完全なコマンドドキュメント](https://aider.chat/docs/commands.html)を参照してください。


## ヒント

* 変更を加えるためにどのファイルを編集する必要があるかを考え、それらをチャットに追加してください。
AiderはLLMがどのファイルを編集するかを自分で判断するのを助けることができますが、最も効率的なアプローチは、必要なファイルを自分でチャットに追加することです。
* 大きな変更は、アプローチと全体的な設計を計画する、思慮深い一口サイズのステップのシーケンスとして実行するのが最適です。ジュニア開発者に対するように、LLMに変更を説明してください。準備のためにリファクタリングを依頼し、次に実際の変更を依頼します。コードの品質/構造の改善を依頼する時間を取ってください。
* LLMが有用な応答を提供していない場合は、Control-Cを使用して安全に中断します。部分的な応答は会話に残るため、より多くの情報や指示でLLMに返信するときにそれを参照できます。
* `/run`コマンドを使用してテスト、リンターなどを実行し、LLMに出力を表示して問題を修正できるようにします。
* Meta-ENTER（一部の環境ではEsc+ENTER）を使用して、複数行のチャットメッセージを入力します。または、最初の行に`{`だけを入力して複数行メッセージを開始し、最後の行に`}`だけを入力して終了します。
* コードがエラーをスローしている場合は、`/run`を使用するか、チャットに貼り付けて、エラー出力をLLMと共有します。LLMにバグを見つけて修正させます。
* LLMは多くの標準ツールやライブラリについて知っていますが、APIや関数の引数に関する細かい詳細について間違いを犯す可能性があります。これらの問題を解決するために、ドキュメントスニペットをチャットに貼り付けることができます。
* LLMは、特に「チャットに追加」したファイルの内容しか見ることができません。Aiderは[gitリポジトリ全体のマップ](https://aider.chat/docs/repomap.html)も送信します。したがって、LLMはあなたのリクエストに必要と感じる場合、追加のファイルを見るように依頼する可能性があります。

## チャット記録の例

[チャット記録の例ページ](https://aider.chat/examples/)では、aiderとチャットしてコードを書いて編集する方法を示しています。

## インストール

[インストール手順](https://aider.chat/docs/install.html)を参照してください。

## FAQ

詳細については、[FAQ](https://aider.chat/docs/faq.html)を参照してください。

## ユーザーからの温かい言葉

* *これまでで最高のAIコーディングアシスタント。* -- [Matthew Berman](https://www.youtube.com/watch?v=df8afeb1FY8)
* *間違いなく、これまでで最高のAIコーディングアシスタントツールです。* -- [IndyDevDan](https://www.youtube.com/watch?v=MPYFPvxfGZs)
* *Aider ... は私のコーディング生産性を簡単に4倍にしました。* -- [SOLAR_FIELDS](https://news.ycombinator.com/item?id=36212100)
* *素晴らしいワークフローです... Aiderの人間工学は私にとって完璧です。* -- [qup](https://news.ycombinator.com/item?id=38185326)
* *まるでシニア開発者がGitリポジトリに住んでいるようです - 本当に素晴らしい！* -- [rappster](https://github.com/paul-gauthier/aider/issues/124)
* *なんて素晴らしいツールでしょう。信じられないほどです。* -- [valyagolev](https://github.com/paul-gauthier/aider/issues/6#issue-1722897858)
* *Aiderはとても驚くべきものです！* -- [cgrothaus](https://github.com/paul-gauthier/aider/issues/82#issuecomment-1631876700)
* *私が立ち上げて最初のいくつかの動作バージョンを作るよりもはるかに速かったです。* -- [Daniel Feldman](https://twitter.com/d_feldman/status/1662295077387923456)
* *Aiderをありがとうございます！コーディングの未来を垣間見ることができます。* -- [derwiki](https://news.ycombinator.com/item?id=38205643)
* *ただただ素晴らしいです。以前は自分の快適ゾーンから出ていると感じていたことができるようになりました。* -- [Dougie](https://discord.com/channels/1131200896827654144/1174002618058678323/1174084556257775656)
* *このプロジェクトは素晴らしい。* -- [funkytaco](https://github.com/paul-gauthier/aider/issues/112#issuecomment-1637429008)
* *素晴らしいプロジェクト、間違いなく私が使った中で最高のAIコーディングアシスタント。* -- [joshuavial](https://github.com/paul-gauthier/aider/issues/84)
* *Aiderを使うのが大好きです...ソフトウェア開発の体験がとても軽くなります。* -- [principalideal0](https://discord.com/channels/1131200896827654144/1133421607499595858/1229689636012691468)
* *複数の肩の手術から回復中で...aiderを広範囲に使用してきました。それによって生産性を維持することができました。* -- [codeninja](https://www.reddit.com/r/OpenAI/s/nmNwkHy1zG)
* *私はaider中毒者です。より短い時間でより多くの仕事を成し遂げています。* -- [dandandan](https://discord.com/channels/1131200896827654144/1131200896827654149/1135913253483069470)
* *より良いものを見つけようとトークンに100ドルを無駄にした後、Aiderに戻りました。他のすべてを完全に凌駕しており、競争は全くありません。* -- [SystemSculpt](https://discord.com/channels/1131200896827654144/1131200896827654149/1178736602797846548)
* *既存のコードベースでの実際の開発作業に最適なエージェント。* -- [Nick Dobos](https://twitter.com/NickADobos/status/1690408967963652097?s=20)
