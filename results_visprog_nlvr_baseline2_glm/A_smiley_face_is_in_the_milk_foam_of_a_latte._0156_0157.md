Question: A smiley face is in the milk foam of a latte.

Reference Answer: True

Left image URL: http://4.bp.blogspot.com/-QKVU84M1z9w/T0wbb4NNJxI/AAAAAAAACFw/ZSrVTlQsbYA/s400/decoracion_cafe2.JPG

Right image URL: https://bellnu.files.wordpress.com/2014/05/el-cafe-reduce-el-riesgo-de-diabetes-tipo-2.jpg

Original program:

```
Statement: A smiley face is in the milk foam of a latte.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'A smiley face is in the milk foam of a latte.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'A smiley face is in the milk foam of a latte.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

