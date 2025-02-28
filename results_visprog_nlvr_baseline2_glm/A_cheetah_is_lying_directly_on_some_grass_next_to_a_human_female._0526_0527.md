Question: A cheetah is lying directly on some grass next to a human female.

Reference Answer: True

Left image URL: https://afrotours.co.za/wp-content/uploads/2017/03/cheetah-kisses-girl-at-Ann-Van-Dyke-Cheetah-Centre.jpg

Right image URL: http://i.dailymail.co.uk/i/pix/2017/03/22/10/3E84DB0C00000578-4338262-image-a-7_1490179602612.jpg

Original program:

```
The program provided is a series of logical steps to determine if a given statement is true or false based on the content of an image. Each statement is evaluated step by step using the VQA (Visual Question Answering) function, which takes an image and a question as input and returns a boolean answer. The final answer is determined by evaluating a series of expressions that combine the individual answers. The program uses the EVAL function to evaluate the expressions and the RESULT function to return the final answer.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'A cheetah is lying directly on some grass next to a human female.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'A cheetah is lying directly on some grass next to a human female.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

