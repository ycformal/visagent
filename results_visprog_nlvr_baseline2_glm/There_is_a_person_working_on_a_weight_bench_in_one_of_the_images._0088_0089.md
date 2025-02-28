Question: There is a person working on a weight bench in one of the images.

Reference Answer: False

Left image URL: https://images-na.ssl-images-amazon.com/images/I/51NRJlkq2TL._SX355_.jpg

Right image URL: https://i.pinimg.com/originals/58/aa/60/58aa609e6dde5f92b2b383663529d04c.png

Original program:

```
The program is not provided for this statement.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There is a person working on a weight bench in one of the images.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There is a person working on a weight bench in one of the images.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

