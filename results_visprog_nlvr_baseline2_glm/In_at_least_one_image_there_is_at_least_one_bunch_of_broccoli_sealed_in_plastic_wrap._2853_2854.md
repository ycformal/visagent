Question: In at least one image there is at least one bunch of broccoli sealed in plastic wrap.

Reference Answer: False

Left image URL: http://2.bp.blogspot.com/-laLMfchDhpI/Udr_Hgf_f7I/AAAAAAAAB0M/3DvYSSRC_po/s400/006.JPGa.jpg

Right image URL: http://3.bp.blogspot.com/_M3v7dl8Ehb0/Sw0wZhglwNI/AAAAAAAAB0s/3LUo475sMYI/s1600/viti_b2_08_lunch31oct09.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'In at least one image there is at least one bunch of broccoli sealed in plastic wrap.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In at least one image there is at least one bunch of broccoli sealed in plastic wrap.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

