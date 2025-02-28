Question: Two skunks stand on a piece of wood in one of the images.

Reference Answer: False

Left image URL: https://www.gannett-cdn.com/-mm-/58175c2bdb4c634ba02a05c6f397272afc6f67e6/c=242-0-1678-1080&r=x393&c=520x390/local/-/media/2015/05/15/KXTV/KXTV/635672984974741620-skunk2.jpg

Right image URL: https://i.ytimg.com/vi/VsUOAHVL96g/hqdefault.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'Two skunks stand on a piece of wood in one of the images.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Two skunks stand on a piece of wood in one of the images.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

