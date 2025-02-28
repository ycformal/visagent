Question: Each image contains an old-fashioned TV with controls on the right of its screen, and no TV has a lit screen or picture displayed on the screen.

Reference Answer: False

Left image URL: https://i.ytimg.com/vi/Xo6lsZgzgfQ/maxresdefault.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/dd/5a/2e/dd5a2e719317cc5bea533766446b13a1.jpg

Original program:

```
Statement: An image shows one bare hand with the thumb on the right holding up a belly-first, head-up crab, with water in the background.
Program:
ANSWER0=VQA(image=LEFT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER1=VQA(image=RIGHT,question='Does the image shows one bare hand with the thumb on the right holding a crab?')
ANSWER2=VQA(image=LEFT,question='Is the crab belly-first and head-ups?')
ANSWER3=VQA(image=RIGHT,question='Is the crab belly-first and head-ups?')
ANSWER4=VQA(image=LEFT,question='Is there water in the background?')
ANSWER5=VQA(image=RIGHT,question='Is there water in the background?')
ANSWER6=EVAL(expr='{ANSWER0} and {ANSWER2} and {ANSWER4}')
ANSWER7=EVAL(expr='{ANSWER1} and {ANSWER3} and {ANSWER5}')
ANSWER8=EVAL(expr='{ANSWER6} xor {ANSWER7}')
FINAL_ANSWER=RESULT(var=ANSWER8)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'Each image contains an old-fashioned TV with controls on the right of its screen, and no TV has a lit screen or picture displayed on the screen.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAhAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDwRFJNXodOnmi81U+QfxEgD9TUSW8qxRyshWOTOxjwGx1rvfhRpem6r4+gsdUtIbyCW3kKxyjcu8AHOPoDWtKmpbjqVHCN0cK0Kp1cZ+tQPsHQmvtiDwb4bgiVI9C01QvTFqhx9OKi1fw9pkegajHHZWyK1tKPlhUY+Q+1Vai9EjN1aq6HxI3XPrU8IzKfYVCw+YVNCcbjWFRcrsdFHWRIwr6Z/Z/bZ8Nrp8ZxqEx/8cSvmVm619MfAP8A5Jlef9f83/oCVnE1rbGtp3xB1/WLNrvTvCfnW4keNXa+RNxU4OAe2albxl4wX/mS4/8AwaR1g/D282eDrdc/8t5yf+/rV0/2sHvQr23OdvXYzrnx/wCK7S3lnm8DSeVEhdzHfxtgAZJwKreFfjBH4l8UW2iLpgheYtl/Nztwpbpir2q3IOjX65620o/8cNeV/C2GIePdGmCASMDls/8ATM1MpWa1LjHmT0PpeijtRWxkfDGmXECbI7u0W4iDbsZIYfj/AErpPCWt23hrxtpOtSBorSK4IkCgsVjYEH64B/SuLS5Ef3VJ+prUgcT2nmS3cES5+5sLPn6UQm4O5rKMZKyPp2T44eCEXKX11MfSO0fP6gVy3iX49afcaXd2mkaLfSvNE8QluSsSruBGcAknr7V4VmDfgXNw6AZ+VAmaY9xborKtvE5ORulJY1ftaa2RHsZPdmeY9p+d1HsGzzQhwn40xlVRxnNGcKKzk+Z3ZrH3WOLV9OfAD5vhld+9/N/6AlfLxNei+Bfi/qXgXQX0m00y0uY3uGnLyswOSFGOP92hIic7nReHfFdtoulGxu1uEdJ5SCsJZSGYkcj61q/8LB0r/n4l/wC/D/4Vjn9obUScnwzpBP8AwKj/AIaF1Ef8yxpH/j1SosltNmjqHjywuNKu4LcXUsssLomLdgMlSBknHrVL4YpInj3RkKNhSwJxxxGaYP2h9SHTwzpA/wC+qev7RmrIcp4e0tT6hnFS6bbTuXGoopq259K9qK+bf+Gktb/6AWnf9/JP8aK1MjxNetW4fu/hRRUSNqQ1/vUnpRRSNERv92mnoKKKpGUtxlFFFUZBRRRQAUUUUAFFFFAH/9k=">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'Each image contains an old-fashioned TV with controls on the right of its screen, and no TV has a lit screen or picture displayed on the screen.' true or false?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

