Question: There are 3 phones on the left and two phones on the right.

Reference Answer: False

Left image URL: http://s7d2.scene7.com/is/image/SamsungUS/Pdpkeyfeature-sm-g928rzkausc-600x600-C1-062016?$product-details-jpg$

Right image URL: https://images-na.ssl-images-amazon.com/images/I/51S5gBPBHsL._SL500_AC_SS350_.jpg

Original program:

```
Statement: There are 3 phones on the left and two phones on the right.
Program:
ANSWER0=VQA(image=LEFT,question='How many phones are in the image?')
ANSWER1=VQA(image=RIGHT,question='How many phones are in the image?')
ANSWER2=EVAL(expr='{ANSWER0} == 3 and {ANSWER1} == 2')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There are 3 phones on the left and two phones on the right.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAwAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD3+sHxlq9/ofha8vtLtVur9dqQRP0Z2YKM8jpnPWt6sDxj/wAgA/8AXeH/ANDFNK7JnLli32PI4PH/AMTy6i4sLaND95hbA4/8ep914/8AiUhVra0t5I24Ba2AOe4+9WtMwCnb365pYrNjost8wyI5gi/7Pr+eR+VdbopRueEszquTiktm/uMCT41+MNHaOz1bRbAXZTedwZSQScHAYjtTH+PuvjI/sjTVPuZP8a47x1I6+LoJI1LMtqhAA929K564u53idJUKiRw5yMZI471Cgux6lOrKcFO+59W/D/xVL4x8KxarPbJbzeY8TpGSVyp6jPNdRXm3wN/5J0v/AF+TfzFek1zyVmzqi7oxdXRJ9WsoJVDxNBOxRuhIMYBx+J/OuV1rT7q31myuLK10/wDsqKOSS8SRD5jMBlQp6Dn+tdXqZ/4nlh/17XH846y9Udvs1wnlOQY2G4Yx0PvQhnljfHeWQYXwtb4YD5vtBUj/AMdqzpnxsFzdwW7eHo1eadYuZi2NzAZBwPWvOLLSA2FlhaQbRgKcGrVrpAj16wMasAtzFkMOQQ613OhC2xk5PufWa/dHOeOtFC/dFFcBqLWB4y48Ov8A9dov/QxW/XN+O38vwpcP6SRH/wAfFVD4kRNc0WjziScZK1JNqEseh/ZEYeVJJuPH3mHofbH5msnTVtda1a30y8T9xLKDI+SOB0XIPAJ/Ouh8TQWljaxQRRqio5WFF42qMV6tRpyVOx8pUwtShGdRy6NHj/jW5lj8RQmORkP2VRlWIPU1zktxNNjzZZJMdN7E4ra8buD4giP/AE7L/Nq57dXLLSTPbwd/q9P0R9OfAs5+HCf9fk38xXpVeafAr/km8f8A19zfzFel1yS3Z6MdjF1Q41yw/wCve4/nHWfqDqLeXccLtOfpirutHbrFg3byLgfrHWPfyeZBKifMzIVUDqSRxSRR5TdX+iW9i32O7jlmbAAQHKg9+R2HNT+F7vStZmtw08UN3HIpKM6jfhhyOf0rnV8H+I57cQ3Wg6o4AGN0BOP61PpfhjxTb6vZv/wj92IUmQuZLcjADDnjrxXXKba+IXP713FH08v3B9KKF+6PpRXGMWuX+IWf+ENuwoyTJEAB/wBdFrqK53xzpN7rng+/0/Tn2XsiqYWOMBlYMM/liqi7STA8T0WQ6f4ssmuIgGinCsj9ieP611HjyQG7iMfOGKjHv/8Aqrk4/ht8RFkWR4FLg5LeehJPrVu/8DfEzUGUzqHxzzLGOa9OOKpcymzzcZhZ11yx2OA8XvPbeIFRlCSC3UMrqDjk+tYEtw8ow+314QA/oK9Lk+DPjnU5hPfi3EgXbueZWJ59qD8CPFeOGtD/ANtAP61yTqxlJy7nRSounTjDsj074EnPw3T/AK/Jv5ivTDXH/DTwvdeEPCEel3rK1x5zyuUOVBY9B+AFdga5nqzpWx8veKvjX4ik1q6szZaYq2dzLFE6pIG2hivPz4OcCsJPi/4hjkWRbexDKwYHY/Uf8Crk/E//ACNesf8AX7P/AOjGrKpDPWf+GhPFv/Plo/8A34k/+Lo/4aE8WkY+xaP/AN+JP/i68mooA9fH7Rni0AAadouB/wBMZf8A45RXkFFAH//Z">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are 3 phones on the left and two phones on the right.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

