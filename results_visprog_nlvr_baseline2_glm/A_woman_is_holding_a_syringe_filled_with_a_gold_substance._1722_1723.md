Question: A woman is holding a syringe filled with a gold substance.

Reference Answer: True

Left image URL: https://st2.depositphotos.com/1518767/7635/i/450/depositphotos_76352059-stock-photo-doctor-preparing-syringe.jpg

Right image URL: https://st.depositphotos.com/2249091/4964/v/450/depositphotos_49646305-stock-video-doctor-preparing-syringe-to-inject.jpg

Original program:

```
Statement: A woman is holding a syringe filled with a gold substance.
Program:
ANSWER0=VQA(image=LEFT,question='Is a woman holding a syringe?')
ANSWER1=VQA(image=RIGHT,question='Is a woman holding a syringe?')
ANSWER2=VQA(image=LEFT,question='Is the syringe filled with a gold substance?')
ANSWER3=VQA(image=RIGHT,question='Is the syringe filled with a gold substance?')
ANSWER4=EVAL(expr='{ANSWER0} and {ANSWER2}')
ANSWER5=EVAL(expr='{ANSWER1} and {ANSWER3}')
ANSWER6=EVAL(expr='{ANSWER4} xor {ANSWER5}')
FINAL_ANSWER=RESULT(var=ANSWER6)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'A woman is holding a syringe filled with a gold substance.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAhAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD2ReKfjdTB2qVelaEDRHTtuKdEQ0rYdCuBgA8571z+t3N1dXzWNpcG3ijH7x1PzM3oPYVMpqKuOMHJ2RvbsdRSMwIxXCxXWp6Pr1r51881hM3lPGRn5j0OT0rtz1ojJS1Q5wcHZnz/APGjS7m68Qrd2ys4h+WQD+Hd0P6Vr+HrSLQ/DkUNzsUhd7NgnJPJNbvjeW1s9Ue7uc48wx9MjBA6iqckdne2S211D5mwgofauStJ81mejhoLk5o7k2l6hpcqPNHdRSIvLFecCuw0DUbLVtEhnslJjR3j3lcbhnPHtzXF6BBpFvbz26QAJK5WRTxuBGOK7vRolttDtbaNFSOMHaFGMDNKhbm0DFX5NSeSPis+4j4Naj9KoXNdZ5piyR/OaKlk++aKAOyzwKguHmdcQMoYN/EOMVHNdLFC0hOAqkk/Sq1lfwXjKY2JAXcQwx1qn2FH+Y2bMMgLMka7jnCjn8TXIanDaJqjyuW89JmKfvMZycngnBrqHvYoYzJI4VRgEn3OP5muS8QPPHqkyyWyPHIAy5/L+eayrK0bnRhpJzdyoLCa41SCJLmScPcJKyuP9WAckZ9OK7tj81cl4Z1KJJLuOcxxvkENnGQOCPwJH510wk3HIORVUo2jcjETTnZdDyf4rzhEmGcHzeP++aqafePFpNn9oU7zCuSeoOOhrnPij4qi/wCE6nsZLSRo7C6DPiQDzeFPpxTb34r6Xe/MfD00Un95Ltf1GysqlJyu0zSjifZtRtdHb6WJp9Ysw10qxGQZVcf0FekjCqFznAxXzvpnxWhsNRt7h9IkkjifeYxcBdxHTJ21op8b3h1GeWHSpfskpLCCS4DbGJycNt6e1FGDiryHiq/PJKKuj3OR+KybydVuoVJ5cMAM9MAHNeWj47xEYk0GQ/7t0B/7LTJPjjayW5j/AOEfkDbs7/tQ6en3K0km9mc8X3R6NLIN5oryl/jBCzZ/saX/AMCR/wDE0Uwsew6j/wAgq4/65mquif8AHyP+uYoopy/ixFD+DL1Rt6z/AMgif6L/AOhCq3in/W2v+6/8xRRV1vgKw/8AERzGmf6vT/8Ar/u//RVdtpv/AB4xf7tFFOHwIit/FZ8w/FP/AJKZrv8A18D/ANAWuPoorN7lLYKKKKQwooooAKKKKAP/2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'A woman is holding a syringe filled with a gold substance.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

