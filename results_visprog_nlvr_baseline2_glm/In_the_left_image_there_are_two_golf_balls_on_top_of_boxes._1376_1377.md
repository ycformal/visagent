Question: In the left image there are two golf balls on top of boxes.

Reference Answer: False

Left image URL: https://http2.mlstatic.com/kaddygolf-pelotas-golf-titleist-prov1-nuevas-caja-x-12-D_NQ_NP_728227-MLA25674874513_062017-F.jpg

Right image URL: https://http2.mlstatic.com/pelotas-golf-titleist-pro-v1-con-tu-logo-o-nombre-D_NQ_NP_963546-MLA25631155838_052017-F.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'In the left image there are two golf balls on top of boxes.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAA8AGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD3+iikZgqlj0AzQAtGagN0gOCACOxdf8aaZ4mbJCnjH3l/xoAs0VW85B90kfR1/wAakRnYEjBweh/+tQBLTXbahb0GeTSbyCAykZOMjmor6OSWymSJVaQr8oZ9oJ9yAcflQBmm61CW32vELaUhTukYbTk8gY/L8asafczM5S5eEMRwiNycHBOOuKx4lt1s3glhSSRH3Nm5Mm1wegye3+RU9rp6XOqJeGyMEsZKKxmLB4z3x2bk8VQFCb4p+D7e9ks5dVYTRuUZRbStyOvReaRviv4HQkPr8KEdQ8Min9Vr571KWS38V6hNEVaU3EqICTjliOgPPHanXt4Ps264gsV8vPyrCZmj/AYA7dT25qOaKK5GfUeia9pfiOw+3aReR3drvMfmIDjcOo5A9aK4X4FeR/wrxvs7Ssn26bmQAEn5ewopks9KZiMYGSTjrTJd/kvnaPlPv2p0nQH0YUS/6l/900AVlA+bgfebt7mq1xqNla3CwTSqsjY429MnAye2TVlejf7zfzNZN9pcF9eC4mgk3AKGCscOFORnigDXKr/dH5VNCoUMAMAHj8hUCsWXcy7Se1TwNvUsOhII/IUAObmRR6c1y/jL4h6H4GezTWDcg3YcxeTFv+7jOeRj7wrqF5dz+FfPv7TH/H14a/3Ln+cdAHUv8cfh9Lv8y2u238NusVOfrzRb/HH4f2asLWG9hz12WYH9a+XKKAPUdSuvhzqWpXN42v8AiCLz3LMsdimRk5IBz70kR+FaY3a14n/7Z20SfyFeX0UrIfMz6O8JfFX4deDdGOl6dLrMkJmaYtPbgtubGehAxxRXzjRTEffsn+rb6ZpJD+6c/wCyacRkEetMwXgwOpWgCARTLkBFIyTnf7/Sl2Tf88x/33/9ap90n9xf++v/AK1Juk/uD/vr/wCtQBCUl/55j/vqpLcFIirdVwD+AFO3yZxsXP8Avf8A1qQI5VhgDceeaAHx/cBPU818+ftMf8fXhr/cuf5x19C189ftMf8AH14a/wBy5/nHQB4LRRRQAUUUUAFFFFAH3/TArgYDDHbin0UAN2E9Xb8MUeWvfJ+pNOooAQKq9ABS0UUAFfPX7TH/AB9eGv8Acuf5x19C189ftMf8fXhr/cuf5x0AeC0UUUAFFFFABRRRQB//2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'In the left image there are two golf balls on top of boxes.' true or false?')=<b><span style='color: green;'>true</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>true</span></b></div><hr>

Answer: true

