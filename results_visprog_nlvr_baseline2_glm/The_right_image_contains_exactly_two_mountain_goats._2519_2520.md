Question: The right image contains exactly two mountain goats.

Reference Answer: False

Left image URL: http://4.bp.blogspot.com/-2IubMCFt6FQ/VAccXRdoS0I/AAAAAAAAyn4/L-iITbexi54/s1600/7+(222).JPG

Right image URL: http://axarquiaviva.files.wordpress.com/2008/11/2843004647_1b0e6fb057.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The right image contains exactly two mountain goats.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The right image contains exactly two mountain goats.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

