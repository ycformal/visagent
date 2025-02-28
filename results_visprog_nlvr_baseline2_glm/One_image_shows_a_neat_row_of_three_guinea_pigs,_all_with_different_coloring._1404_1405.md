Question: One image shows a neat row of three guinea pigs, all with different coloring.

Reference Answer: False

Left image URL: https://img00.deviantart.net/05d0/i/2009/220/c/3/hamster_lol_o_o_by_xxchillixx.jpg

Right image URL: https://tikushamster.files.wordpress.com/2008/07/img_4154.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'One image shows a neat row of three guinea pigs, all with different coloring.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One image shows a neat row of three guinea pigs, all with different coloring.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

