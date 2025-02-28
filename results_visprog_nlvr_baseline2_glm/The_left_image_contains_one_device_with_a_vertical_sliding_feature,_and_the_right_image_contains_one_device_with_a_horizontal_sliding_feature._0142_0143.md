Question: The left image contains one device with a vertical sliding feature, and the right image contains one device with a horizontal sliding feature.

Reference Answer: True

Left image URL: http://images.mobilefun.co.uk/graphics/productgalleries/15700/b.jpg

Right image URL: http://www.tuvie.com/wp-content/uploads/sony-ericsson-xperia-x1-slider-phone1.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The left image contains one device with a vertical sliding feature, and the right image contains one device with a horizontal sliding feature.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The left image contains one device with a vertical sliding feature, and the right image contains one device with a horizontal sliding feature.' true or false?')=<b><span style='color: green;'>no</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>no</span></b></div><hr>

Answer: False

