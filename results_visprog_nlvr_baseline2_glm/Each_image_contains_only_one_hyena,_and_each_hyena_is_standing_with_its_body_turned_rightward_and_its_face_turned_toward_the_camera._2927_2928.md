Question: Each image contains only one hyena, and each hyena is standing with its body turned rightward and its face turned toward the camera.

Reference Answer: False

Left image URL: https://s-media-cache-ak0.pinimg.com/600x315/f8/8f/e8/f88fe8a0a514eda5635fb56646a6afd2.jpg

Right image URL: http://www.teepr.com/wp-content/uploads/2015/08/1412348243376_wps_20_Biting_Spotted_Hyena_Imag.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'Each image contains only one hyena, and each hyena is standing with its body turned rightward and its face turned toward the camera.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image contains only one hyena, and each hyena is standing with its body turned rightward and its face turned toward the camera.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

