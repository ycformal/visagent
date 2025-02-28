Question: Large yellow chandeliers hang from the ceiling inside a book store.

Reference Answer: False

Left image URL: http://68.media.tumblr.com/a176c5b0f721fa891c7f7cf45215686f/tumblr_o327o3LOvX1qzqrpyo2_1280.jpg

Right image URL: http://www.localporto.com/wp-content/uploads/beautiful-bookstore-world-porto-lello-irmao-2-565x280.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'Large yellow chandeliers hang from the ceiling inside a book store.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Large yellow chandeliers hang from the ceiling inside a book store.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

