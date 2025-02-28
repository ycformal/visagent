Question: There is no more then two items with with labels seen

Reference Answer: False

Left image URL: https://images-eu.ssl-images-amazon.com/images/I/31exgZSAHSL.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/dc/48/2f/dc482f39bdbd6ab31185a27e782cf49e.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There is no more then two items with with labels seen' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There is no more then two items with with labels seen' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

