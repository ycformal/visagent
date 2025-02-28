Question: At least 1 person is wearing colorful graduation robes.

Reference Answer: False

Left image URL: https://sc02.alicdn.com/kf/HTB13LHYJpXXXXa5XpXXq6xXFXXXy/221594253/HTB13LHYJpXXXXa5XpXXq6xXFXXXy.jpg

Right image URL: http://indianproduct.com/tasselnfringe/cg/phdSC1s.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'At least 1 person is wearing colorful graduation robes.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'At least 1 person is wearing colorful graduation robes.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

