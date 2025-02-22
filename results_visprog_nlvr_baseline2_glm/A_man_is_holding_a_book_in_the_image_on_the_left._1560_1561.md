Question: A man is holding a book in the image on the left.

Reference Answer: True

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/09/39/4b/09394b7b4c68df9a61e82a68058884d9.jpg

Right image URL: https://i.pinimg.com/736x/1d/19/b4/1d19b492a8b76f74f50911ad5c454443--mens-pajamas-polo-ralph-lauren.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='Is a man holding a book in the image?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='Is a man holding a book in the image?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is a man holding a book in the image?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

