Question: The left image contains one device with a vertical sliding feature, and the right image contains one device with a horizontal sliding feature.

Reference Answer: False

Left image URL: http://fb1-ca.lnwfile.com/wtgps4.jpg

Right image URL: https://ae01.alicdn.com/kf/HTB18SDVHVXXXXbmXFXXq6xXFXXXl/Cheap-W910-Sony-Ericsson-W910-W910i-Slider-Mobile-Phones-2-4-inch-Screen-2MP-Camera-Original.jpg

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

