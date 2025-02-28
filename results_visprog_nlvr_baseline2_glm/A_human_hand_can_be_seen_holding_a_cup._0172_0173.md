Question: A human hand can be seen holding a cup.

Reference Answer: True

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/d1/02/b6/d102b636ef3a0f1d34665582fdff15ee.jpg

Right image URL: https://ciccoloclay1.files.wordpress.com/2013/01/newhandles.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'A human hand can be seen holding a cup.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'A human hand can be seen holding a cup.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

