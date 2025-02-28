Question: The left image contains exactly two dispensers.

Reference Answer: True

Left image URL: https://i.pinimg.com/736x/95/f6/b7/95f6b7f0fc9e4b7d2a70db7bb90c236b--minimalist-bathroom-pinterest-instagram.jpg

Right image URL: https://ae01.alicdn.com/kf/HTB1dyWJJpXXXXckXXXXq6xXFXXXA/hand-soap-dispenser-bottle-bathroom-shampoo-and-conditioner-dispenser-wall-mounted-3-Soap-Dispenser-Free-Shipping.jpg_640x640.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The left image contains exactly two dispensers.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The left image contains exactly two dispensers.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

