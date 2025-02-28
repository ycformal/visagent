Question: In at least on image there is a single hyena with black paws facing right with its face slightly forward.

Reference Answer: True

Left image URL: https://images-na.ssl-images-amazon.com/images/I/41DMU-x7VbL._SR600%2C315_PIWhiteStrip%2CBottomLeft%2C0%2C35_PIAmznPrime%2CBottomLeft%2C0%2C-5_PIStarRatingFOURANDHALF%2CBottomLeft%2C360%2C-6_SR600%2C315_ZA(5%20Reviews)%2C445%2C286%2C400%2C400%2Carial%2C12%2C4%2C0%2C0%2C5_SCLZZZZZZZ_.jpg

Right image URL: https://hyenaproject.files.wordpress.com/2016/02/06_02a-d_methods-identification_all_light_c.png

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'In at least on image there is a single hyena with black paws facing right with its face slightly forward.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In at least on image there is a single hyena with black paws facing right with its face slightly forward.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

