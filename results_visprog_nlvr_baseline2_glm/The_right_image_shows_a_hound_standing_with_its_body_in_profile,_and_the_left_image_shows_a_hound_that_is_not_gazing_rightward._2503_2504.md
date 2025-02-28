Question: The right image shows a hound standing with its body in profile, and the left image shows a hound that is not gazing rightward.

Reference Answer: True

Left image URL: https://s-media-cache-ak0.pinimg.com/736x/80/ea/8a/80ea8a8f6a8bc615db357c11c8e2aea5.jpg

Right image URL: http://1.bp.blogspot.com/_jZHHRfnq9F8/TNVwE-PY6DI/AAAAAAAAL9A/tkw_BNLct7Y/s1600/Afghan+Hound+Dog.jpg

Original program:

```
The provided program is designed to evaluate the truthfulness of a statement based on the content of two images. The statement is: "The right image shows a hound standing with its body in profile, and the left image shows a hound that is not gazing rightward."
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The right image shows a hound standing with its body in profile, and the left image shows a hound that is not gazing rightward.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The right image shows a hound standing with its body in profile, and the left image shows a hound that is not gazing rightward.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

