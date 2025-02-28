Question: At least one image shows a canoe with no part touching the water and no water in the scene.

Reference Answer: True

Left image URL: http://www.pilotfamily.com/canoe/mods/10.jpg

Right image URL: https://i.pinimg.com/736x/f6/e9/13/f6e91353f06be27948492f754f500073--canoeing-kayak.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'At least one image shows a canoe with no part touching the water and no water in the scene.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'At least one image shows a canoe with no part touching the water and no water in the scene.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

