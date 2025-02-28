Question: There are four furry animals.

Reference Answer: True

Left image URL: http://2.bp.blogspot.com/-Oz0NlWQ67Ew/UmrcNvazsmI/AAAAAAAAiPw/zfn42iVP6sI/s640/article-0-12DB6F26000005DC-295_634x422.jpg

Right image URL: https://barneswildlifecontrol.com/wp-content/uploads/2017/10/dont-play-with-baby-skunks-300x200.jpg

Original program:

```
Statement: There are four furry animals.
Program:
ANSWER0=VQA(image=LEFT,question='How many furry animals are in the image?')
ANSWER1=VQA(image=RIGHT,question='How many furry animals are in the image?')
ANSWER2=EVAL(expr='{ANSWER0} + {ANSWER1} == 4')
FINAL_ANSWER=RESULT(var=ANSWER2)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'There are four furry animals.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAtAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwCKz0fzcs5ViOMHqK1Dp0MKRJ5YHv2qGxsLlVmlR95VgQdwB56/WtfToHa+iindSNw3JjnHU18/7W9l3OfluVm0q3s7R7u8doYsblAGC34ngVRTWdPn1KW3tYI5YovlLCRtw4PPoQcH8qqyXmreI9Xuvt+oGC1E2YNNMILGNehfPK54wOvGTxjPJpNdv4gtoVVotL+2fZJOxYep+h/nXpRwsUrM6YxpxVrXPUFsp7y3WewWN9i7pIlkDFMdx6j9ajAU4kzyBzg1i6Q0OleIdOdZ5RcJHIssKKSDEHYbifTBHX0NdrbXdpd6RcXLWiSkH5EtwCXx0IJ7YrOWHd/dZEqKbvE5+U+Yrps5PAOaw7hDZ7l3b/7xPau51KHTLfRp9XlV7GK3jMksXBbp0AHc15hD410/VL0wxafduhOCyqG2g9zjpWE8LUs3bQxlBxZesp9KnNzo/iG0ZrG92hLgKdkbDplv4Tzwa4bxL8LNd0S/Isojf2Dt+5uEIH4MCeD+hrqNQ8US+FtQhMdtHe6ZOGW+tZBuWRcjHXgMOcVV8aeK4L3w1ptpa3BZobhtsCOcmIYeJyR0ODt5759K6cM5WVtmd1JRlQV90V9AWTwj4Yvv7Qff9qZdqW7iTHrjHfGenFd54d8deHrvVbf7PqPzXoEP2d0KmMqCVLZGMnpxkdK8Lv47+xjhWRHgjk/fLCXOFVgCPwII/Or8kek3NpbNZ6fd297MwRFjuPMjZuhADDcpzg9T1rolBONmFOTg+bseq+INOtINYmVrGSQE7lZFJBBJIoql9rFjHHbG7u0KIARJMpbPTnJorzbvoZT9m5Nq/wCBt2V7BYMBLu8hU+ZuOM/zra8PX9nf6qJWgcrErbQT3A64rkbfSzP9nLzLtSUM4CFQQOigDg1v6VfW+lXcjS3SgrG7O0jDA4ztz0HWuelFxqR7XOeD1R5/4gu7nS/El1Dpl/KUc4id0yYwW+YZx27D2pdf07R9H0iC4kmu5bwqWhQfeZzz5jAnAGfQVe1pdP8AEGpi4SQ20ztkSLh1cj1weDijS7uXTfENlp1y8dzFNcRKZZYElaMM2P3e4EDqDnHavfhF3NpSRp2OuXdvY77+3iguoIwuW5Mu8ZAQjqehP5V3eg+GtUt7eKSSSC2R4tyxYycnkAk+npXmepfETxBb6rPbG5jnNtNLHDcS2sZdcEjPTjpXI3/jLxNql7HJdatcySo3yYbbtJOM4H1rRQUdxOTZ6/8AEjw5qMnhv7PZXKq9zLidicDaev6CsnRY9LttEt9CSFRsUBHxh3kP3mPcEkYwfauA0/xBrGtXiQ32oXNzFBuIRjuyf6810Vnf3sMP2y7KW0eCPMOJNh7bwOlZ11zrlHBKzTF8Vapo2lS2iahas8UysGRFBAxwfx5FeY22tf2VPPFaxQXdm0gcR3MZwcZwCAQcfMeM4NbXxAvTdvpwyCqLJ93hSSQSRXF1hh6doa/1qOHufCzrrnxLZ6veLc6rDDvdiZhbwlAw2gDv2xj8KfpmreHLC3A2XnnxTs8Mi5HGBhiM43dR9K46itnSTVrhJuTuz0qTxpokxDPLqG4AKTsHOOM9aK81orP6rTA98uJL6GNY3LGTaCYoxyo6f49Kn0SxLNcT38YlKoPLhlUFQD7dz9arNdDUZLSSaP8AfqFR5VbBkUgdfcetX7q0NpZtKkpZPlKq4yVOcdfpXlycqU9F5owUHbmXQ5q8010u724twSWG5Yo49qgcAk468HP/AOqqtvbXl1b2V1Gdsiyt80gwoTP16gg8erCu7hmWeeFbuJLiNBgo/RgBwMelMvRbRec8VqqJIdnl7jtUMecD3ojmN6jVmh7rmPHteg1GfXLi0iifeg35U7g46kjp6n8jVrSfDN5cJBclkDPIpwGBwitk5I4ySBgexr0LUdCsmsGl8v8AerlUbJITkdBnjp+p9asxpDHpFqI4EQLEF+QYzxjJroqY/wBy8f60E5uxxOr6cdM1jT5bWOONLhWQNG+PmXgLj196iEV21xLcqVjk3YbuHwOQw6L+NdjKobywVX/R1+TAxgk8/wAzVvW7KPTpBDhXOxWTauxVGAcY5z1rOOLlKCYczseTeOzEbi08rAHzgAdhkcfnmuRrsviApW5s1yMAPjj3FcbXo4Z3pI0p/CFFFFblhRRRQB//2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'There are four furry animals.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

