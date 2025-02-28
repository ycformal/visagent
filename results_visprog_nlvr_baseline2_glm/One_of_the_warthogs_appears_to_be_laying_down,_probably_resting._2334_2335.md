Question: One of the warthogs appears to be laying down, probably resting.

Reference Answer: True

Left image URL: http://www.paesieimmagini.it/Kenya/Imm_Kenya/Kenya08-0020.jpg

Right image URL: http://2.bp.blogspot.com/-_muudxsj7I4/T7p_OYFJ_MI/AAAAAAAAAGk/bXsLUpfsXMs/s1600/images-1.jpeg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'One of the warthogs appears to be laying down, probably resting.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'One of the warthogs appears to be laying down, probably resting.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

