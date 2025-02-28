Question: the right side has bananas as dolphins

Reference Answer: False

Left image URL: http://2.bp.blogspot.com/-dL4sDwtqjOA/VplywZVqX1I/AAAAAAAACPQ/ags4vLsyHpo/s1600/IMG_3396_1.jpg

Right image URL: http://1.bp.blogspot.com/-QKOmKuS2H_s/Vln1yBMkBDI/AAAAAAAACKU/ZpzRZsX963k/s1600/DSC01664.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'the right side has bananas as dolphins' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'the right side has bananas as dolphins' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

