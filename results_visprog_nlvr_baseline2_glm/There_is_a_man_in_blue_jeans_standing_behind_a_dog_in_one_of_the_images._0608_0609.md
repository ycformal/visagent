Question: There is a man in blue jeans standing behind a dog in one of the images.

Reference Answer: True

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/15/e1/15/15e115875a4a1499aa1d299b7d195d91.jpg

Right image URL: https://fossmtnfarm.files.wordpress.com/2015/07/juno_irish-marked-borzoi.jpg

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There is a man in blue jeans standing behind a dog in one of the images.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There is a man in blue jeans standing behind a dog in one of the images.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

