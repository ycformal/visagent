Question: An image shows a group of three pet rodents in a container, and all share the same fur coloration

Reference Answer: True

Left image URL: https://www.wikihow.com/images/thumb/0/05/Care-for-Dwarf-Hamsters-Step-6-Version-3.jpg/aid390547-v4-728px-Care-for-Dwarf-Hamsters-Step-6-Version-3.jpg

Right image URL: http://hamstertalk.webstarts.com/uploads/WW.jpg

Original program:

```
Statement: An image shows a group of three pet rodents in a container, and all share the same fur coloration.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'An image shows a group of three pet rodents in a container, and all share the same fur coloration' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'An image shows a group of three pet rodents in a container, and all share the same fur coloration' true or false?')=<b><span style='color: green;'>same</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>same</span></b></div><hr>

Answer: same

