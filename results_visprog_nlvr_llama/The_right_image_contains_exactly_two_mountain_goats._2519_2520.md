Question: The right image contains exactly two mountain goats.

Reference Answer: False

Left image URL: http://4.bp.blogspot.com/-2IubMCFt6FQ/VAccXRdoS0I/AAAAAAAAyn4/L-iITbexi54/s1600/7+(222).JPG

Right image URL: http://axarquiaviva.files.wordpress.com/2008/11/2843004647_1b0e6fb057.jpg

Program:

```
ANSWER0=VQA(image=RIGHT,question='How many mountain goats are in the image?')
ANSWER1=EVAL(expr='{ANSWER0} == 2')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='How many mountain goats are in the image?')=<b><span style='color: green;'>1</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="ANSWER0 == 2")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="1 == 2")=<b><span style='color: green;'>False</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>False</span></b></div><hr>

Answer: False

