Question: One of the vases has a design painted on it.

Reference Answer: True

Left image URL: https://s-media-cache-ak0.pinimg.com/originals/f4/55/59/f45559d395764b302a8ec5653bd7099e.jpg

Right image URL: https://farm5.static.flickr.com/4042/4678741524_5b61e9e5f0_b.jpg

Original program:

```
The program is designed to determine if one of the vases in the image has a design painted on it. It does this by asking the user if there is a vase in the image and if there is a design on the vase. If the user answers yes to both questions, the program will return true. If the user answers no to either question, the program will return false. Therefore, the statement is true.
####
True
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

