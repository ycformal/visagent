Question: An image contains one camera-facing guinea pig with white down the middle of its face, posed in an outdoor setting.

Reference Answer: False

Left image URL: https://i.pinimg.com/736x/5c/b4/93/5cb49386950700dcb704a1edaa2a1905--guinea-pig-for-sale-guinea-pigs.jpg

Right image URL: https://i.pinimg.com/736x/4f/14/30/4f1430947c100289620a7b9731716f36--guinea-pig-cages-guinea-pigs.jpg

Original program:

```
Statement: An image contains one camera-facing guinea pig with white down the middle of its face, posed in an outdoor setting.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'An image contains one camera-facing guinea pig with white down the middle of its face, posed in an outdoor setting.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'An image contains one camera-facing guinea pig with white down the middle of its face, posed in an outdoor setting.' true or false?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: False

