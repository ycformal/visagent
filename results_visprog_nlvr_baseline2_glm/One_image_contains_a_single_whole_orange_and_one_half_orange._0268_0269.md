Question: One image contains a single whole orange and one half orange.

Reference Answer: False

Left image URL: http://clipart-library.com/images/riLxGgqqT.png

Right image URL: http://images.all-free-download.com/images/graphiclarge/delicious_fruit_03_hd_pictures_166657.jpg

Original program:

```
The statement is True.
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is "{statement.replace('(','').replace(')','')}" true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAwAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD5/oq5pel3WsahFZWce+aQ9zgKO5J7AV67oXws0O3Crq4uL2X+NkkMUY9AMcn65rmxGMo4f+Izoo4WrW+BHi1dZoHw48TeIrdbizsVjt3GUluZViDfTPJHvivUZ/hX4Whvbe9sjcr5R3G0ncPHIR0BPUc/XNdB9rYOqwpLLJGv+qjXLE+leZic6hFqNBczf9W9TtoZXKUXKppb+rnhusfDfxVockYvNLcxyMEWaJ1dMn1IPH44pmu6AuheHrMSOHubiYtIR0AC8Ae3Jr1jUbLxVeTm6vtLvfIA+VAu4IPoOc+9c7f6VaeIZ4Hu2kWC13Dyj8ozxkt36DpxW9PGzk05q3c8ms1CemxxXw4Ur8SfDeQRnUITz/vV9h6rqy6dEAq+ZM3Rc8D618leD7pL/wCL+izwJth/tKERqB91AwC/oBXvmvay/wDaNwrcjeQB9KvMcXLD0Lx0kzvy/CvE1LW2NSTxRerKpdmXccKFTK5/Lj8a2rDxCrr/AKUVC/31/qK4GDWYwSJBvB7GpG1ZWCoo2oPzrwKWZVafvOd/Jns1csUvd5LEWu+Nb7UrqSOCV7e0yVSNDgsPVj/SpvDDXl9qdvCksuC25trEYUdSTWDqFjeS6hLPYWcs0RQSSMi5CHv/ACziu/8ABWraEsK2ls8iXbj5muFAL+wI4x7V14Tmr1VOrLf+rI+ar0pUqrhLodtRRRX0xJ8lfCmzjZdSvCMyIY4ge4U7if5D8q9aWSJUQDOMc14h8NNbfTddksmhllt75Aj+WhYow+62B25IPsfavd9K0eK42m7uwDu/1EfXaBkkn8O1fJZ1h5PE37r8j6XLq9NYVKXS5DfvLJp809lbb/IQs+DwAO/vVGzeWM5Vv3hwWZeMmumiWLM4gIWJoJFEOOeVIAHrXHWt55eFcFJMDcjjBU46Edq8eHvQ50elQlzpxS2Oni1WaFEEs7DjI+nesrxJYQX1jLfbkSWJC8kmBh48fMG9eM1LDMkyKCzBh3Hel1S4gtdCvp5jiKK0kLn1+Q1VKrP2tPlk73Rw4vDRlCSkrHkHhjWLW6+J3h600u3jt7FdRh5RAplO4cnvj0Fe0eLtK8jUJJRny5SWU/XtXz18OP8AkpPhz/sIQ/8AoQr601vSJb+Ixr0/rX2uLwca1HkW6PEy3E/VavN0PJ2iMdW9O07U9TGbS0Lx7sGViFUevJ/pWheeCNfMp8q6UR/7SA10Npbva6ZbWkMoL2yhWAIBJ6sfzzXhPLpQ1qrTyPqJ5rCUP3Wr8+hXsJzZvFaghkUYYrxuJ6mq1/pdjPc5kD2855E0IAEg7Ejof0NNSKbah6+WCDtPOAeP0rUsZjO0cM9v5qE5Iwcg+xrmXPFOGzvpdaHn4mhTn70lfubui3l9FpkcUqSXpT5VnXCll7bgT1FFbsUSQxLHGgRAOAO1FfWUqVSMFGUtT5uXLf3VoeEfD+Xw5q3heJdAt4LPUYYwt7bZ/euw/jBPLqf06V1ej212mqKTE6K0bxhmXgEjA618pwzy20qywSvFIvKujFSPoRWr/wAJd4i3xO2t37GJg6brhiAQcjgmvKr5Nz1vaxl956FHMHCl7No+lnmkhlIYMHB5BOOaNX8nW9r3UaxSrjbNEuG9OfUfWuP0D4peHNfijOt3B0vUyAJmKFoZW/vAj7ufQ1uT+KPCVjEZbrxPp8kQXhbZjK5P+6K8CpgMZSbpxTs399j1IYyg7VL2aILpRoFjJfX86JZRkKbjB25PQeua8q8c/EH+3bc6Vpm9NPyDLIww0xHQY7L396f8QviOPFEEWkaXDJb6RA/mfvD+8nf+82Og9BXntfQZblUaVq1Ze/8AkedjcyqVrwW35ml4f1d9A8QWGrxxLK9nOsyxscBipzgmvXv+Gk9W/wChfsv+/wC/+FeH0V7h5R7e/wC0jqjqQ3h6yIP/AE3eqP8AwvmUzea3hXT2f1M7mvHqKTSe5SlKOzPaJP2hLuUAP4X0446fvnGKWH9oa+tyDF4bslx0/wBIkOK8Wopcsb3sHPK1rnuH/DSmrf8AQv2X/f8Af/CivD6Kok//2Q==">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is ')=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: True

