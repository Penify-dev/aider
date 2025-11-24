
# aider es programación en pareja con IA en tu terminal

Aider es una herramienta de línea de comandos que te permite programar en pareja con LLMs (Modelos de Lenguaje Grande), para editar código almacenado en tu repositorio git local.
Aider editará directamente el código en tus archivos fuente locales y [hará commit de los cambios en git](https://aider.chat/docs/faq.html#how-does-aider-use-git) con mensajes de commit sensatos.
Puedes iniciar un nuevo proyecto o trabajar con un repositorio git existente.
Aider es único en que te permite solicitar cambios en [bases de código preexistentes y más grandes](https://aider.chat/docs/repomap.html).
Aider funciona bien con GPT-4o, Claude 3 Opus, GPT-3.5 y admite [conexión a casi cualquier LLM](https://aider.chat/docs/llms.html).

<p align="center">
  <img src="assets/screencast.svg" alt="demostración de aider">
</p>

<p align="center">
  <a href="https://discord.gg/Tv2uQnR88V">
    <img src="https://img.shields.io/badge/Join-Discord-blue.svg"/>
  </a>
</p>

- [Primeros pasos](#primeros-pasos)
- [Características](#características)
- [Uso](#uso)
- [Videos tutoriales](https://aider.chat/docs/install.html#tutorial-videos)
- [Comandos en el chat](#comandos-en-el-chat)
- [Consejos](#consejos)
- [Instalación](https://aider.chat/docs/install.html)
- [Conexión a LLMs](https://aider.chat/docs/llms.html)
- [Tablas de clasificación de LLM](https://aider.chat/docs/leaderboards/)
- [Voz a código](https://aider.chat/docs/voice.html)
- [Ejemplos de transcripciones de chat](https://aider.chat/examples/)
- [Preguntas frecuentes](https://aider.chat/docs/faq.html)
- [Discord](https://discord.gg/Tv2uQnR88V)
- [Blog](https://aider.chat/blog/)


## Primeros pasos

Consulta las [instrucciones de instalación](https://aider.chat/docs/install.html) para más detalles, pero puedes comenzar rápidamente así:

```
$ pip install aider-chat

# Para trabajar con GPT-4o
$ export OPENAI_API_KEY=tu-clave-va-aquí
$ aider 

# Para trabajar con Claude 3 Opus:
$ export ANTHROPIC_API_KEY=tu-clave-va-aquí
$ aider --opus
```


## Características

* Chatea con aider sobre tu código ejecutando `aider <archivo1> <archivo2> ...` desde la línea de comandos con un conjunto de archivos fuente para discutir y editar juntos. Aider permite que el LLM vea y edite el contenido de esos archivos.
* Aider puede escribir y editar código en los lenguajes más populares: python, javascript, typescript, php, html, css, etc.
* Aider funciona bien con GPT-4o, Claude 3 Opus, GPT-3.5 y admite [conexión a casi cualquier LLM](https://aider.chat/docs/llms.html).
* Solicita nuevas características, cambios, mejoras o correcciones de errores en tu código. Pide nuevos casos de prueba, documentación actualizada o refactorizaciones de código.
* Aider aplicará las ediciones sugeridas por el LLM directamente a tus archivos fuente.
* Aider [hará commit automáticamente de cada conjunto de cambios en tu repositorio git local](https://aider.chat/docs/faq.html#how-does-aider-use-git) con un mensaje de commit descriptivo. Estos commits frecuentes y automáticos proporcionan una red de seguridad. Es fácil deshacer cambios o usar flujos de trabajo git estándar para gestionar secuencias más largas de cambios.
* Puedes usar aider con múltiples archivos fuente a la vez, para que aider pueda hacer cambios de código coordinados en todos ellos en un solo conjunto de cambios/commit.
* Aider puede [proporcionar al LLM un mapa de todo tu repositorio git](https://aider.chat/docs/repomap.html), lo que le ayuda a entender y modificar bases de código grandes.
* También puedes editar archivos manualmente usando tu editor mientras chateas con aider. Aider notará estas ediciones externas y se mantendrá actualizado con las últimas versiones de tus archivos. Esto te permite alternar entre el chat de aider y tu editor, para programar colaborativamente con un LLM.
* Puedes agregar archivos de imagen a tu chat si estás trabajando con un modelo OpenAI con capacidad de visión (GPT-4o, GPT-4 Turbo, etc).


## Uso

Ejecuta `aider` con los archivos de código fuente que deseas editar.
Estos archivos se "agregarán a la sesión de chat", para que el LLM pueda ver su contenido y editarlos según tus instrucciones.

```
aider <archivo1> <archivo2> ...
```

Sé selectivo y solo agrega los archivos que el LLM necesitará editar.
Si agregas un montón de archivos no relacionados, el LLM puede abrumarse y confundirse (y cuesta más tokens).
Aider compartirá automáticamente fragmentos de otros archivos relacionados con el LLM para que pueda [entender el resto de tu base de código](https://aider.chat/docs/repomap.html).

También puedes simplemente lanzar aider en cualquier lugar de un repositorio git sin nombrar archivos en la línea de comandos. Descubrirá todos los archivos en el repositorio. Luego puedes agregar y eliminar archivos individuales en la sesión de chat con los comandos de chat `/add` y `/drop` descritos a continuación.
Si tú o el LLM mencionan cualquiera de los nombres de archivo del repositorio en la conversación, aider preguntará si te gustaría agregarlos al chat.

Aider también tiene muchas otras opciones que se pueden configurar con interruptores de línea de comandos, variables de entorno o mediante un archivo de configuración.
Consulta `aider --help` para más detalles.


## Comandos en el chat

Aider admite comandos desde dentro del chat, que todos comienzan con `/`. Aquí están algunos de los comandos en el chat más útiles:

* `/add <archivo>`: Agrega archivos coincidentes a la sesión de chat, incluidos archivos de imagen.
* `/drop <archivo>`: Elimina archivos coincidentes de la sesión de chat.
* `/undo`: Deshace el último commit de git si fue hecho por aider.
* `/diff`: Muestra el diff del último commit de aider.
* `/run <comando>`: Ejecuta un comando de shell y opcionalmente agrega la salida al chat.
* `/voice`: Habla con aider para [solicitar cambios de código con tu voz](https://aider.chat/docs/voice.html).
* `/help`: Muestra ayuda sobre todos los comandos.

Consulta la [documentación completa de comandos](https://aider.chat/docs/commands.html) para más información.


## Consejos

* Piensa en qué archivos necesitan ser editados para hacer tu cambio y agrégalos al chat. Aider puede ayudar al LLM a descubrir qué archivos editar por sí solo, pero el enfoque más eficiente es agregar tú mismo los archivos necesarios al chat.
* Los cambios grandes se realizan mejor como una secuencia de pasos pequeños y reflexivos, donde planificas el enfoque y el diseño general. Guía al LLM a través de los cambios como lo harías con un desarrollador junior. Pide una refactorización para preparar, luego pide el cambio real. Dedica tiempo a solicitar mejoras de calidad/estructura del código.
* Usa Control-C para interrumpir de forma segura al LLM si no está proporcionando una respuesta útil. La respuesta parcial permanece en la conversación, por lo que puedes referirte a ella cuando respondas al LLM con más información o dirección.
* Usa el comando `/run` para ejecutar pruebas, linters, etc. y mostrar la salida al LLM para que pueda corregir cualquier problema.
* Usa Meta-ENTER (Esc+ENTER en algunos entornos) para ingresar mensajes de chat multilínea. O ingresa `{` solo en la primera línea para comenzar un mensaje multilínea y `}` solo en la última línea para terminarlo.
* Si tu código está generando un error, comparte la salida del error con el LLM usando `/run` o pegándola en el chat. Deja que el LLM descubra y corrija el error.
* Los LLMs conocen muchas herramientas y bibliotecas estándar, pero pueden equivocarse en algunos detalles finos sobre APIs y argumentos de funciones. Puedes pegar fragmentos de documentación en el chat para resolver estos problemas.
* El LLM solo puede ver el contenido de los archivos que específicamente "agregas al chat". Aider también envía un [mapa de todo tu repositorio git](https://aider.chat/docs/repomap.html). Por lo tanto, el LLM puede pedir ver archivos adicionales si siente que es necesario para tus solicitudes.

## Ejemplos de transcripciones de chat

[La página de transcripciones de ejemplo](https://aider.chat/examples/) muestra cómo puedes chatear con aider para escribir y editar código.

## Instalación

Consulta las [instrucciones de instalación](https://aider.chat/docs/install.html).

## Preguntas frecuentes

Para más información, consulta las [Preguntas frecuentes](https://aider.chat/docs/faq.html).

## Palabras amables de los usuarios

* *El mejor asistente de codificación con IA hasta ahora.* -- [Matthew Berman](https://www.youtube.com/watch?v=df8afeb1FY8)
* *Sin duda, esta es la mejor herramienta de asistente de codificación con IA hasta ahora.* -- [IndyDevDan](https://www.youtube.com/watch?v=MPYFPvxfGZs)
* *Aider ... ha cuadruplicado fácilmente mi productividad de codificación.* -- [SOLAR_FIELDS](https://news.ycombinator.com/item?id=36212100)
* *Es un flujo de trabajo genial... La ergonomía de Aider es perfecta para mí.* -- [qup](https://news.ycombinator.com/item?id=38185326)
* *Es realmente como tener a tu desarrollador senior viviendo directamente en tu repositorio Git - ¡verdaderamente increíble!* -- [rappster](https://github.com/paul-gauthier/aider/issues/124)
* *Qué herramienta tan increíble. Es asombrosa.* -- [valyagolev](https://github.com/paul-gauthier/aider/issues/6#issue-1722897858)
* *¡Aider es algo tan sorprendente!* -- [cgrothaus](https://github.com/paul-gauthier/aider/issues/82#issuecomment-1631876700)
* *Fue MUCHO más rápido de lo que yo habría sido para ponerme en marcha y hacer las primeras versiones funcionales.* -- [Daniel Feldman](https://twitter.com/d_feldman/status/1662295077387923456)
* *¡GRACIAS por Aider! Realmente se siente como un vistazo al futuro de la codificación.* -- [derwiki](https://news.ycombinator.com/item?id=38205643)
* *Es simplemente increíble. Me está liberando para hacer cosas que sentía que estaban fuera de mi zona de confort antes.* -- [Dougie](https://discord.com/channels/1131200896827654144/1174002618058678323/1174084556257775656)
* *Este proyecto es estelar.* -- [funkytaco](https://github.com/paul-gauthier/aider/issues/112#issuecomment-1637429008)
* *Proyecto increíble, definitivamente el mejor asistente de codificación con IA que he usado.* -- [joshuavial](https://github.com/paul-gauthier/aider/issues/84)
* *Me encanta absolutamente usar Aider ... Hace que el desarrollo de software se sienta mucho más ligero como experiencia.* -- [principalideal0](https://discord.com/channels/1131200896827654144/1133421607499595858/1229689636012691468)
* *He estado recuperándome de múltiples cirugías de hombro ... y he usado aider extensivamente. Me ha permitido continuar siendo productivo.* -- [codeninja](https://www.reddit.com/r/OpenAI/s/nmNwkHy1zG)
* *Soy un adicto a aider. Estoy haciendo mucho más trabajo, pero en menos tiempo.* -- [dandandan](https://discord.com/channels/1131200896827654144/1131200896827654149/1135913253483069470)
* *Después de desperdiciar $100 en tokens tratando de encontrar algo mejor, he vuelto a Aider. Supera a todo lo demás por completo, no hay competencia en absoluto.* -- [SystemSculpt](https://discord.com/channels/1131200896827654144/1131200896827654149/1178736602797846548)
* *Mejor agente para trabajo de desarrollo real en bases de código existentes.* -- [Nick Dobos](https://twitter.com/NickADobos/status/1690408967963652097?s=20)
