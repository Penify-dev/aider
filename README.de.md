# aider ist KI-Paarprogrammierung in Ihrem Terminal

Aider ist ein Kommandozeilen-Tool, mit dem Sie mit LLMs Paarprogrammierung durchführen können,
um Code zu bearbeiten, der in Ihrem lokalen Git-Repository gespeichert ist.
Aider bearbeitet den Code direkt in Ihren lokalen Quelldateien
und [committed die Änderungen mit git](https://aider.chat/docs/faq.html#how-does-aider-use-git)
mit sinnvollen Commit-Nachrichten.
Sie können ein neues Projekt starten oder mit einem bestehenden Git-Repository arbeiten.
Aider ist einzigartig darin, dass es Ihnen ermöglicht, Änderungen an [bereits bestehenden, größeren Codebasen](https://aider.chat/docs/repomap.html) anzufordern.
Aider funktioniert gut mit GPT-4o, Claude 3 Opus, GPT-3.5
und unterstützt die [Verbindung zu fast jedem LLM](https://aider.chat/docs/llms.html).

<p align="center">
  <img src="assets/screencast.svg" alt="aider screencast">
</p>

<p align="center">
  <a href="https://discord.gg/Tv2uQnR88V">
    <img src="https://img.shields.io/badge/Join-Discord-blue.svg"/>
  </a>
</p>

- [Erste Schritte](#erste-schritte)
- [Funktionen](#funktionen)
- [Verwendung](#verwendung)
- [Tutorial-Videos](https://aider.chat/docs/install.html#tutorial-videos)
- [In-Chat-Befehle](#in-chat-befehle)
- [Tipps](#tipps)
- [Installation](https://aider.chat/docs/install.html)
- [Verbindung zu LLMs](https://aider.chat/docs/llms.html)
- [LLM-Ranglisten](https://aider.chat/docs/leaderboards/)
- [Sprache-zu-Code](https://aider.chat/docs/voice.html)
- [Beispiel-Chat-Transkripte](https://aider.chat/examples/)
- [FAQ](https://aider.chat/docs/faq.html)
- [Discord](https://discord.gg/Tv2uQnR88V)
- [Blog](https://aider.chat/blog/)


## Erste Schritte

Weitere Details finden Sie in den
[Installationsanweisungen](https://aider.chat/docs/install.html),
aber Sie können so schnell loslegen:

```
$ pip install aider-chat

# Um mit GPT-4o zu arbeiten
$ export OPENAI_API_KEY=your-key-goes-here
$ aider

# Um mit Claude 3 Opus zu arbeiten:
$ export ANTHROPIC_API_KEY=your-key-goes-here
$ aider --opus
```


## Funktionen

* Chatten Sie mit aider über Ihren Code, indem Sie `aider <file1> <file2> ...` von der Kommandozeile aus mit einer Reihe von Quelldateien ausführen, die Sie gemeinsam besprechen und bearbeiten möchten. Aider ermöglicht es dem LLM, den Inhalt dieser Dateien zu sehen und zu bearbeiten.
* Aider kann Code in den meisten gängigen Sprachen schreiben und bearbeiten: Python, JavaScript, TypeScript, PHP, HTML, CSS usw.
* Aider funktioniert gut mit GPT-4o, Claude 3 Opus, GPT-3.5 und unterstützt die [Verbindung zu fast jedem LLM](https://aider.chat/docs/llms.html).
* Fordern Sie neue Funktionen, Änderungen, Verbesserungen oder Fehlerbehebungen für Ihren Code an. Fragen Sie nach neuen Testfällen, aktualisierter Dokumentation oder Code-Refactorings.
* Aider wendet die vom LLM vorgeschlagenen Änderungen direkt auf Ihre Quelldateien an.
* Aider [committed automatisch jeden Änderungssatz in Ihr lokales Git-Repository](https://aider.chat/docs/faq.html#how-does-aider-use-git) mit einer beschreibenden Commit-Nachricht. Diese häufigen, automatischen Commits bieten ein Sicherheitsnetz. Es ist einfach, Änderungen rückgängig zu machen oder Standard-Git-Workflows zu verwenden, um längere Änderungssequenzen zu verwalten.
* Sie können aider mit mehreren Quelldateien gleichzeitig verwenden, sodass aider koordinierte Code-Änderungen über alle Dateien hinweg in einem einzigen Änderungssatz/Commit vornehmen kann.
* Aider kann [dem LLM eine Karte Ihres gesamten Git-Repositorys geben](https://aider.chat/docs/repomap.html), was ihm hilft, große Codebasen zu verstehen und zu modifizieren.
* Sie können Dateien auch manuell mit Ihrem Editor bearbeiten, während Sie mit aider chatten. Aider bemerkt diese Out-of-Band-Änderungen und hält sich auf dem neuesten Stand der aktuellen Versionen Ihrer Dateien. Dies ermöglicht es Ihnen, zwischen dem aider-Chat und Ihrem Editor hin und her zu wechseln, um gemeinsam mit einem LLM zu programmieren.
* Sie können Bilddateien zu Ihrem Chat hinzufügen, wenn Sie mit einem visionfähigen OpenAI-Modell arbeiten (GPT-4o, GPT-4 Turbo usw.).


## Verwendung

Führen Sie `aider` mit den Quellcode-Dateien aus, die Sie bearbeiten möchten.
Diese Dateien werden "zur Chat-Sitzung hinzugefügt", sodass das LLM ihren
Inhalt sehen und gemäß Ihren Anweisungen bearbeiten kann.

```
aider <file1> <file2> ...
```

Seien Sie selektiv und fügen Sie nur die Dateien hinzu, die das LLM bearbeiten muss.
Wenn Sie viele nicht zusammenhängende Dateien hinzufügen, kann das LLM überfordert
und verwirrt werden (und es kostet mehr Token).
Aider wird automatisch
Snippets aus anderen, verwandten Dateien mit dem LLM teilen, damit es
[den Rest Ihrer Codebasis verstehen](https://aider.chat/docs/repomap.html) kann.

Sie können aider auch überall in einem Git-Repository starten, ohne
Dateien in der Kommandozeile zu benennen. Es wird alle Dateien im
Repository entdecken. Sie können dann einzelne Dateien in der Chat-
Sitzung mit den unten beschriebenen `/add`- und `/drop`-Chat-Befehlen hinzufügen und entfernen.
Wenn Sie oder das LLM Dateinamen des Repositorys in der Konversation erwähnen,
fragt aider, ob Sie sie zum Chat hinzufügen möchten.

Aider hat auch viele andere Optionen, die mit
Kommandozeilen-Schaltern, Umgebungsvariablen oder über eine Konfigurationsdatei gesetzt werden können.
Siehe `aider --help` für Details.


## In-Chat-Befehle

Aider unterstützt Befehle innerhalb des Chats, die alle mit `/` beginnen. Hier sind einige der nützlichsten In-Chat-Befehle:

* `/add <file>`: Übereinstimmende Dateien zur Chat-Sitzung hinzufügen, einschließlich Bilddateien.
* `/drop <file>`: Übereinstimmende Dateien aus der Chat-Sitzung entfernen.
* `/undo`: Den letzten Git-Commit rückgängig machen, wenn er von aider durchgeführt wurde.
* `/diff`: Das Diff des letzten aider-Commits anzeigen.
* `/run <command>`: Einen Shell-Befehl ausführen und optional die Ausgabe zum Chat hinzufügen.
* `/voice`: Mit aider sprechen, um [Code-Änderungen mit Ihrer Stimme anzufordern](https://aider.chat/docs/voice.html).
* `/help`: Hilfe zu allen Befehlen anzeigen.

Weitere Informationen finden Sie in der [vollständigen Befehlsdokumentation](https://aider.chat/docs/commands.html).


## Tipps

* Überlegen Sie, welche Dateien bearbeitet werden müssen, um Ihre Änderung vorzunehmen, und fügen Sie sie zum Chat hinzu.
Aider kann dem LLM helfen, selbst herauszufinden, welche Dateien bearbeitet werden sollen, aber der effizienteste Ansatz ist es, die benötigten Dateien selbst zum Chat hinzuzufügen.
* Große Änderungen werden am besten als eine Abfolge von durchdachten, mundgerechten Schritten durchgeführt, bei denen Sie den Ansatz und das Gesamtdesign planen. Führen Sie das LLM durch Änderungen, wie Sie es bei einem Junior-Entwickler tun würden. Bitten Sie zuerst um ein Refactoring zur Vorbereitung, dann um die eigentliche Änderung. Nehmen Sie sich die Zeit, um Verbesserungen der Codequalität/-struktur zu bitten.
* Verwenden Sie Strg-C, um das LLM sicher zu unterbrechen, wenn es keine nützliche Antwort liefert. Die teilweise Antwort bleibt in der Konversation, sodass Sie darauf verweisen können, wenn Sie dem LLM mit weiteren Informationen oder Anweisungen antworten.
* Verwenden Sie den `/run`-Befehl, um Tests, Linter usw. auszuführen und die Ausgabe dem LLM zu zeigen, damit es Probleme beheben kann.
* Verwenden Sie Meta-ENTER (Esc+ENTER in einigen Umgebungen), um mehrzeilige Chat-Nachrichten einzugeben. Oder geben Sie `{` allein in der ersten Zeile ein, um eine mehrzeilige Nachricht zu beginnen, und `}` allein in der letzten Zeile, um sie zu beenden.
* Wenn Ihr Code einen Fehler auslöst, teilen Sie die Fehlerausgabe mit dem LLM, indem Sie `/run` verwenden oder sie in den Chat einfügen. Lassen Sie das LLM den Bug finden und beheben.
* LLMs wissen über viele Standard-Tools und Bibliotheken Bescheid, können aber einige der feinen Details zu APIs und Funktionsargumenten falsch verstehen. Sie können Dokumentations-Snippets in den Chat einfügen, um diese Probleme zu lösen.
* Das LLM kann nur den Inhalt der Dateien sehen, die Sie ausdrücklich "zum Chat hinzufügen". Aider sendet auch eine [Karte Ihres gesamten Git-Repositorys](https://aider.chat/docs/repomap.html). Das LLM kann also darum bitten, zusätzliche Dateien zu sehen, wenn es das für Ihre Anfragen für erforderlich hält.

## Beispiel-Chat-Transkripte

Die [Beispiel-Transkript-Seite](https://aider.chat/examples/) zeigt, wie Sie mit aider chatten können, um
Code zu schreiben und zu bearbeiten.

## Installation

Siehe die [Installationsanweisungen](https://aider.chat/docs/install.html).

## FAQ

Weitere Informationen finden Sie in den [FAQ](https://aider.chat/docs/faq.html).

## Nette Worte von Benutzern

* *Der bisher beste KI-Coding-Assistent.* -- [Matthew Berman](https://www.youtube.com/watch?v=df8afeb1FY8)
* *Zweifellos ist dies das bisher beste KI-Coding-Assistenten-Tool.* -- [IndyDevDan](https://www.youtube.com/watch?v=MPYFPvxfGZs)
* *Aider ... hat meine Coding-Produktivität leicht vervierfacht.* -- [SOLAR_FIELDS](https://news.ycombinator.com/item?id=36212100)
* *Es ist ein cooler Workflow... Aiders Ergonomie ist perfekt für mich.* -- [qup](https://news.ycombinator.com/item?id=38185326)
* *Es ist wirklich so, als hätten Sie Ihren leitenden Entwickler direkt in Ihrem Git-Repository - wirklich erstaunlich!* -- [rappster](https://github.com/paul-gauthier/aider/issues/124)
* *Was für ein erstaunliches Tool. Es ist unglaublich.* -- [valyagolev](https://github.com/paul-gauthier/aider/issues/6#issue-1722897858)
* *Aider ist so eine erstaunliche Sache!* -- [cgrothaus](https://github.com/paul-gauthier/aider/issues/82#issuecomment-1631876700)
* *Es war VIEL schneller, als ich es gewesen wäre, um anzufangen und die ersten funktionierenden Versionen zu erstellen.* -- [Daniel Feldman](https://twitter.com/d_feldman/status/1662295077387923456)
* *DANKE für Aider! Es fühlt sich wirklich wie ein Blick in die Zukunft des Programmierens an.* -- [derwiki](https://news.ycombinator.com/item?id=38205643)
* *Es ist einfach erstaunlich. Es befreit mich, Dinge zu tun, die ich vorher außerhalb meiner Komfortzone fühlte.* -- [Dougie](https://discord.com/channels/1131200896827654144/1174002618058678323/1174084556257775656)
* *Dieses Projekt ist hervorragend.* -- [funkytaco](https://github.com/paul-gauthier/aider/issues/112#issuecomment-1637429008)
* *Erstaunliches Projekt, definitiv der beste KI-Coding-Assistent, den ich verwendet habe.* -- [joshuavial](https://github.com/paul-gauthier/aider/issues/84)
* *Ich liebe es absolut, Aider zu verwenden ... Es lässt die Softwareentwicklung als Erfahrung so viel leichter anfühlen.* -- [principalideal0](https://discord.com/channels/1131200896827654144/1133421607499595858/1229689636012691468)
* *Ich erhole mich von mehreren Schulteroperationen ... und habe aider ausgiebig verwendet. Es hat mir ermöglicht, produktiv zu bleiben.* -- [codeninja](https://www.reddit.com/r/OpenAI/s/nmNwkHy1zG)
* *Ich bin ein aider-Süchtiger. Ich erledige so viel mehr Arbeit, aber in weniger Zeit.* -- [dandandan](https://discord.com/channels/1131200896827654144/1131200896827654149/1135913253483069470)
* *Nachdem ich 100 Dollar für Token verschwendet habe, um etwas Besseres zu finden, bin ich zurück zu Aider. Es übertrifft alles andere bei weitem, es gibt überhaupt keine Konkurrenz.* -- [SystemSculpt](https://discord.com/channels/1131200896827654144/1131200896827654149/1178736602797846548)
* *Bester Agent für tatsächliche Entwicklungsarbeit in bestehenden Codebasen.* -- [Nick Dobos](https://twitter.com/NickADobos/status/1690408967963652097?s=20)
