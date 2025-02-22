Question: The left image contains a human wearing a heavy jacket.

Reference Answer: True

Left image URL: https://cdnd.lystit.com/photos/bloomingdales/1745841-Monarch%20Orange-1c8ca99b-.jpeg

Right image URL: https://cdnb.lystit.com/photos/2013/10/22/canada-goose-yellow-and-orange-kensington-parka-product-1-14347801-836179825.jpeg

Original program:

```
ANSWER0=VQA(image=LEFT,question='Is the person wearing a heavy jacket?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=LEFT,question='Is the person wearing a heavy jacket?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is the person wearing a heavy jacket?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="True")=<b><span style='color: green;'>True</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>True</span></b></div><hr>

Answer: True

