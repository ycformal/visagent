Question: Does the soccer player next to the other soccer player look small?

Reference Answer: yes

Image path: ./sampled_GQA/n244826.jpg

Original program:

```
BOX0=LOC(image=IMAGE,object='soccer player')
IMAGE0=CROP_NEXTTO(image=IMAGE,box=BOX0)
BOX1=LOC(image=IMAGE0,object='soccer player')
ANSWER0=VQA(image=IMAGE0,question='Does this soccer player look small?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Does the soccer player next to the other soccer player look small?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAA4AGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwByxoOgGfeszX9VOkWKSRRiWaWQRxofX1rQLN/CBkepxWHrpMgVvJ88xsEaNCCVU8scfTABrgXdmmFpKrVUG7I1tMlmutMhnuDH5r7gyrnAxVwqCOgNV7Vg6vsW4j2LGPLmZThSPlIIA4wKx/FO+W2traKaVJ2lDgRN1UdSfzGPejRs0xGG5MR7GOu23mjf2+uB+Ncte2zR65JMf9IAMZ8sAFgp6nnoRj9RW2t6pAgVsyRIisGfGeMZ565x1rnv7OX+3ru9vNrK021FYllXjjdtYMMcdsEZ5q4Qc9EVh74Su3UT08tzasJLfUoHuYkkEQkKDc2eR+v51cFmh6ZA9M0+Kwh03S0gEizXczmfeqOuF4BXJwDj2FJHEyEnPPv2onHldjjqy5puXcQWaLz5knHvThbx9yzH3an4JON/48UpBHXH51mZibB6k/iaryQRZJYNjvzSyE88Sr9FqsEYk7lkI+nNFgHfYrd+fIP4tRSCEAdZfyNFMZdCSn7zR9OwrjfFENzLrtvDHG8jGAbNgxyWPpXWk3n8L2499jH+tZeuTTwaXNdSzwAwDem1GB3dgOe9OFr6m1Gq6c+ZF3w9BfDSGa7tntzuaH5xyGQ5AI656j8aj1OO2gu7O7vpSsSM0e7psLKdpIHUBgtUtB8WXGqx6i06RxrcOspK5YJJ7euQTVbxBHcX2mskMplcOGWMKEBwfU02kpWOh1msRGcpfM0rqTUrzTzPBIl5eSEINjoVA/vfQDnGKyNQmtYY1tbrUrZxB8jl2CtuPLKDtbjpwRx61p+FoJJbK4WWRItQgXzUtgmTKP4ipB+9gZwPwrP0nSIdQvJNWmhA3MxjVhlTu+82Dx7VcGqfxDxMlKc5xejd+2/9bHUQyWE9rbS6Vult0TZuKkKz/wAQBIGRz1Ap7IOMD6ZHIrN0q8hsry90hXaQOqzoR/yyYcEH6g/yq3LeRoG6Fl7NxUTleVzkqJRsk7olK47sT7UbTxgn8s1U/tCPaSEAbvgU6O5ilU7/AC8fXkfWouZEks0ajYWT356VWaWM5HnRE9+vFK0dpv3eWcnvg4/SnmOIgp5cePcGgCvi2YktIufoaKmEUoGF+zgdv3ZP9aKLjKt3qc8UbKDbZP8AEZQK5LVbq6unSJpExv3jB3AkA4H51pS+HJZSGbUMndnCRgc0o8KwvtMmpXGN3QgLz+dbR5V1NKdRwlzI0NFjtbTTo4IxEo2hi4GSxIyc571fuJTDDuWMMndUAOfwrI/4RSAAFby7YdPlerNro0dqmFlvJMdN5BAz6ZqWo3vciTcndmPJda1FrVnPPCqRySBUiHSPHOOP4sckiurS4kKYWMAY9Kr29tLHPE4WZvKJKbnGBnrxipZ4bh3Zo0jXJyeTj8MHih2expUqc6StaxBbaPcTXN/eFMyDBVgoI8vH3dw5yDzzxz2qT7I7sBsUeoL/AP1qlsLa9sry4uEmRFuE2SxouA4xjkkn+VWpIpHIAZB7EZzSk07WMmVVstrFsEqB0BzTlWUEf6Mdo4+YipDFIw+aXA7BacsO0cNx+INTqAxBcnIaNV9CGzUiCQjDjHupp2AMZP60Dd/ezSbAU5HHJ9+BRRk/5NFSBmrbMcFZenU5NSi1mCnMufQelFFaDK5hnjOFY89SU/wojW7VsLcgE8neD/hRRVJJgS/Zr9jzOoB/u9qt20UsYIkn3jHQ0UVBJNIjbCUYE+54qvtuVBwqN65Y0UUWQFYicMQsZwewkpVglBwSqr6Fj/OiimkAILzja8br/vE1N/pbJ1RT270UUmMALsDjy/wbFFFFSB//2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Does the soccer player next to the other soccer player look small?')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes

