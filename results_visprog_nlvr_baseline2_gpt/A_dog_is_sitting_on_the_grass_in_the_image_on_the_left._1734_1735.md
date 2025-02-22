Question: A dog is sitting on the grass in the image on the left.

Reference Answer: True

Left image URL: https://lh3.googleusercontent.com/jZeIlFW7hPhZBb1JY_PCDREos0Y5qK9wH3g47JpC3k3wTbMi3IjmVyeSNVVFHFXifw=h900

Right image URL: https://images6.alphacoders.com/807/thumb-1920-807388.jpg

Original program:

```
ANSWER0=VQA(image=LEFT,question='Is there a dog sitting on the grass in the image?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='Is there a dog sitting on the grass in the image?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is there a dog sitting on the grass in the image?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

