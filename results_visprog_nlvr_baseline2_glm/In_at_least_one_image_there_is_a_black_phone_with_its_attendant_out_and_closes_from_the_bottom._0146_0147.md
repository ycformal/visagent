Question: In at least one image there is a black phone with its attendant out and closes from the bottom.

Reference Answer: False

Left image URL: https://i.pinimg.com/736x/fb/6d/8f/fb6d8f11fd116f6e3915f24a89d17529--flip-phones-smart-phones.jpg

Right image URL: https://i.pinimg.com/236x/47/41/b5/4741b5b0269490ac4b4e0251a6f53eed--mobile-phones-stock-photos.jpg

Original program:

```
Solution:
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'In at least one image there is a black phone with its attendant out and closes from the bottom.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABcAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD2zU9ZjsWMUcfnXAXcV3bVQerN2rkZPFl3etIIL4gLwPssOI2PYCRwd31Aqfxt5thq2nTlv+JdfubS6QqMbyP3ZJ98FSOnSuH1Px/eLJNa6HoLIkDtEZbt9q5Bxwi8np60JSk7RQ24xV2dnputeIrScSXqCS1HMiNIJGUdzkKvb613ysHUMpBUjII718tahr/iXUZN11qk6IpDCODEMYI9h1/GvoTwRrC6z4YtZ8guqhWHp/nkfhVSpzh8SIVSE/hZ0VFFFSUFFFFABRRVPVtSh0jSbvUbg/uraJpG98DoPc9PxoAuVk+IPEFt4etLeaeOWZ7i5jtoYYQC7u5xxk9hk/hXz/D8UfFdpqstwdSZnkcs1rOoKD2Cnlce2K9B8K6le/EHxZZanqVukMGixGRIoiTG078bjnnIGcDtj3qFNPYpxseq0UUVZJkeJ9FTX/D15pzcPIm6J+6SLypH0IFfP/iie6ge21BEUfbQRP6JOnyyD8cA/jX0vXkHjbRPJ1i/tFX93dKNStPlB2ypxKoB4yV+b8K1o1HTqKSIqQU4NNHkE32u5kVSssrv0UDj8q9e+E15Ppco0u7BRZVygY9/84/M1y7TwadBBNHZ3Mv2pC8FzLGxE4GPunBJPIOMDimQ6tqSazZX6Rv9nif96BGq7QeAcAkjuME56cDFdOJdNpu95GNKrVlyxUOWCvvvr/wx9F0VW0+7W+sIblSCJFBOPXvVmuE6QooooAK8++LOrmy0K1sYwHe6nUlCeGVTnn2zj8q9Brzz4keDNR8QNFqGny+ZJbx7fsxGDwScr6n2PpUy2HHc8nuZrXU0CyQq7RMGk3Jyqg9Vb68V7n4A0dtI8LwmUf6RdEzycYxn7o/AY/HNeTeDNAutS8RRWM1q4jR/NuiVKhFHYg85Y5GK9/jQRxhR2qKcFFaDkx1FFFakhXLeOrN30VNTgTdc6bILhR/eXo6/iK6mmyRpLE8bqGRwVYHuD1oA8HnETXkWn3b3M9jA/wBpsI7VSXljZflUnk7QGI4wOBmrkGkXF9HEEtoLC3TJD4Ekrc+gO3Ix3Jq1NG/hO3+w6hdm5i8+WC0tLdS0mxTuUMByQVYegHvTGm8UajD5elWEGj23QPLhpQP90cL/ADp88krIaijptL13/hF7KKC9MUdiGVEM0v708AdBwSfavQa8fsPDUViEnvZWvNUAy13Nyxb1UHIUZ9PSvT9G1A6hYq0mBcR4WUD19foetSgZo0UUUxBWdrWrQ6NpzXUimR2ZYoYVOGmlY4VB7k/lye1cb4n+Mvhrwn4gudF1CDUWurfbvMMKsvzKGGCWHYiubu/jl8P7+9s7y607VpZrNi9uWgUiNjxuA34z79qAPUNA0mTTreWe8kE2pXj+ddyjoWxgKv8AsqOAPbPUmtevJD+0R4Ox8ttq2fe3T/4umn9ojwj/AM+2qj/t3T/4ugD12ivI/wDhojwh3tdV/wC/Cf8AxdFAHrlFFFAHmvxH0SSxvbfxXYRZlhxHdADlk6Z/p+VSafrUM+nwnfuiYAhgvJXj078c+4Neg3FvFdW0lvOgeKRSjqehB6ivGPsc3hTxLNoUzE28jGWxkPcH+H8cfmKTGjtZvKuBG8WWcqGcdMHJH0IB7VHp01zpGps7xSGP7s3fcOckfTH+c1FbXLW6osZDgDc2ORk9x+GKuCT7QWEgLOx4xxySTn/OKQzs0dXRXUhlYZBHQilrn9AvvLc6fKQOrQ8547r+HUex9q6CqJPkL43f8lb1n6Qf+iUrz2vQvjd/yVvWfpB/6JSvPaACiiigAooooA+/6KKKACuY8b+FR4m0jbARHqFufMtpOnP93Poa6eigDx/QtSe5iKXKmO5hcx3EJHKyDqD9ev510SE7dp44JwGzgen4Z96p+OtLTR9dtvEUBKQ3RFveIi5JYDKSAeoxg/QVnf2/D5eyOeHjnKhmf64/hqStzdu5hBCJUdYp1IMIUfMXHQ/Tnn2OK6bRvEFvqzvbghbqJAzqOnPp+PavObW21XWZcWcDxxnhp5xjj+Z/QV2Ol6fbeHrJhG++c/PJM3ViP6U0DPm/43f8lb1n6Qf+iUrz2vQPjY2/4sawwzysB5/64pXn9MkKKKKACiiigD7/AKKKKACiiigCjq+l2+s6XPYXI+SVcBh1VuzD3Brxq7gufCHiq0a82s9u2Gbb8s8D8NjPoefYgivc6z9T0TTNYEX9o2MN15Tbo/NXO00Acn/wki3Mot7JGuJeyQjd/LoK3NL0i5kdbrU8AjlLcHIB9WPc+3Stm0srWxhENpbQ28Q6JEgUfkKnoHc+Qvjd/wAlb1n6Qf8AolK89r0L43f8lb1n6Qf+iUrz2gQUUUUAFFFFAH//2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In at least one image there is a black phone with its attendant out and closes from the bottom.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

