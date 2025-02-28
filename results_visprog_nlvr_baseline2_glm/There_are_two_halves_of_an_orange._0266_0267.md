Question: There are two halves of an orange.

Reference Answer: True

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/f2/92/b6/f292b6ab9ae03cb1d3ca2e136f32102a.jpg

Right image URL: http://wallpaperswide.com/download/orange_fruit-wallpaper-1366x768.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There are two halves of an orange.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are two halves of an orange.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

