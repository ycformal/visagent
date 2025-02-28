Question: Left and right images each contain one round pizza, the pizza on the left has a slice that is at least partly removed, and the pizza on the right is on a round platter.

Reference Answer: True

Left image URL: https://main-cdn.grabone.co.nz/goimage/325x225/3c026edefe1310567cc721c78e8b36ce628a8ff7.jpg

Right image URL: https://main-cdn.grabone.co.nz/goimage/fullsize/a873555a3ce09192f3a6ab1fe504f5e8e0bcec6e.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'Left and right images each contain one round pizza, the pizza on the left has a slice that is at least partly removed, and the pizza on the right is on a round platter.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Left and right images each contain one round pizza, the pizza on the left has a slice that is at least partly removed, and the pizza on the right is on a round platter.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

