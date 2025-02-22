Question: There is only one pillow in the right image.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/6a/b1/e7/6ab1e797e6b0a3d4d7b70bda3443ac97--stacked-books-bookshelf-ideas.jpg

Right image URL: https://rlv.zcache.com/purple_stacked_monogram_throw_pillow-rdc1244c0ecb54ea48e4bd061fd777774_6s309_8byvr_324.jpg?square_it=true

Original program:

```
ANSWER0=VQA(image=RIGHT,question='How many pillows are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} == 1')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=RIGHT,question='How many pillows are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} == 1')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many pillows are in the image?')=<b><span style='color: green;'>1</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 == 1")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="1 == 1")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

