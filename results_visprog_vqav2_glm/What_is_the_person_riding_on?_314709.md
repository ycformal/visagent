Question: What is the person riding on?

Reference Answer: skis

Image path: ./sampled_GQA/314709.jpg

Program:

```
ANSWER0=VQA(image=IMAGE,question='What is the person riding on?')
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCABDAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDfuPCF8knCxuP9nOKifwlflwPKBJHGGIA/GvQ0E4XD+W5/2cjNQym5wSttGT/10/wFb+0ZlyI8zl0e7s5wr+Ujg8DdmrC31zCfJkgtmcD5WyUP555rqrqNVYyXEJgJ/iRM/rtrltQsIJ5Wa0MsjejDr9DiqTvuQ1bYnt9anhZluNgbP+qlDKv5jikn1clAYopIyrZLxSE/rWU1vfxYDQS8jADLmkiU2u9rp5LeID5mQ4x9QeKdluF3sW31F5pVeCKfcvLB3JH6Vt2Hiu92iMxLLtODkZ/XP9KxYdI1C4sxNZRNJbvkhyQGx7gGqxsriACW9W7hA48zZlfzosmF2ju49av2m+ewjWDrv83NWxqLTFNrxRKx4ZpBz9K8zWdhlftbCPPVeefcelWheXZJYXUcygcZYHj2yKlwHzHqEKyLnfKsinoduD+nFSYwTXlyajA+wzXFwg6lkPU/TNdLpOvwpGUE08qDp5u0n/GocGilI62isL+27l+YoEK+6uf5Cilysdzf4FJnJ9qbux14pQaQxeDlW5HpVO40qxuj+8tkz6qNp/Srh9aBgigZlSeHbKYYzNnoPnJryrxDqVq91Pb2xS4t7WYBXYlRIVPPrwDn64r2iUqIm3ttBG3P14/OvE38FSXcLQ6dkzCby5Umbou4fOPcDOfpmrjJWd9TOUJSnHldknd/Lp8zp5NVY2yrFceWdowjDr75qtDq13J+6ut0iEYLbzn+eK17Hw3rcUiRzLpk1nEgWMoGAP8AwE9B7jrWgPB63DE3Tqif884mOB/n6VV4rQXvS1ZxOpTQNhIoIxjq23B/nWcwA5ByD616nF4U062GUjLED7zdfzFZc+gaY85ja3likA4yRg/jnFNVEJwZwDMSBnBx7VYs737KxJWTHrG+wj8a2dR8OyQsHigdE77v89KbHp9pDMI7y1mjbHDRMCp9+armTQrMq/29KnEctwy9vMbJHtwaKq3sam7kCLEqg4HQEj144oosguz2TjuAaQKMADIxSjFHeuc2AA49apahqtvpio1yk3lscb0jLBfriroPbvSEK3DAEeh5oAxBr1tdH/iXXAuJWY/OVOIh6dOD6Zqto1pHPfGRG3RRbgeOpJ5z65ra/s2y8wyLbRxyHq8Y2E/iKYlhJbMWtbqQKTkxSgMp/qKBmhRVUS3Kna9qG4+9HIMfripo5C4OY3T/AHxigCtcWG9me3meGU+jnbn3FY19p2sXDqCIpMjGSwIH6Cul6UlNOwmjmE8L3DOjtfSRsByASR/Sop/Cd3PODJewlAOqxBT+OK63PNISc4OMUczFyo5tPBenBRuDMe5JzRXS5I/hz+NFHMx8qE4/GjFNxzS/jzSAWkxR0z1xQW9OaAFpCwBwe9KG4oOD2oAO1H0pO2O1OoAb1HNITzk8CnEZpPqKACjP/wCukHoMYoyOKAFHuRRSZ9KKAAUCiimA4gcUh70UUgGt0NKScZzRRQA4jFNyQDg96KKAFzxSjpRRQAxuM49aVuBRRQAw8HA4ooooEf/Z">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='What is the person riding on?')=<b><span style='color: green;'>skis</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>skis</span></b></div><hr>

Answer: skis

