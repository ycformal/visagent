Question: The rodent in the image on the right is situated on a piece of pink material.

Reference Answer: False

Left image URL: http://cf.ltkcdn.net/small-pets/images/std/193083-342x228-Teddy-Guinea-Pig.jpg

Right image URL: https://i.pinimg.com/736x/f3/cb/09/f3cb09b72daf457a5ebac7b994d049ff--pig-stuff-stuffed-animals.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The rodent in the image on the right is situated on a piece of pink material.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The rodent in the image on the right is situated on a piece of pink material.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

