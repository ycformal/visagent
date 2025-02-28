Question: The right image shows three bottles of beer lined up.

Reference Answer: True

Left image URL: https://www.foodifancy.com/wp-content/uploads/2012/02/dass_beer-and-glass.jpg

Right image URL: https://s-media-cache-ak0.pinimg.com/originals/bc/ea/b6/bceab62f71a2253c6044a36cdd9027f9.jpg

Original program:

```
The right image shows three bottles of beer lined up.
Program:
ANSWER0=VQA(image=RIGHT,question='Are there three bottles of beer lined up?')
ANSWER1=EVAL(expr='{ANSWER0}')
FINAL_ANSWER=RESULT(var=ANSWER1)
```
Program:

```
ANSWER0=VQA(image=IMAGE,question="Is 'The right image shows three bottles of beer lined up.' true or false?")
FINAL_RESULT=RESULT(var=ANSWER0)
```
Rationale:

<hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>VQA</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAAxAGQDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD3+imTOYoJJAu4qpIGcZwK5/wj4juvEdlPNdWAs3jZQE37sgqG/rik5JOw1FtXOjorzjTtQl/4WHJK2o3DWUtzIkcZDeXkoABnp1Bx9a6XXvEk+j6tYWUViJ0uSNz79uzLqv8AXP4VEasZJtPZ2LlTkml5XOiPAqqt1iFHlaJN4yMtj+dTytthdvRSa88+IttFf2tjZfa7e1mgJcPcRF1IZShAIBwR16elaGZ38crtOUYLjaGBBqh4nu7mw8Mand2ThLmG2d4mYAgMBx1p2k3cF5Bbz2774miKBgpXJU46Hp3rJ+JF6tj4A1eQvtZ4hEnqWZgox+dJ7FR+JGD8M/E2u69faimrSlo4o0MasqghskMflA44FTfE7xHrXh9tL/smUqs3m+aqhSxxtA+8D/eNcn8ILtrbxXcWdxcO5ubIvH5hzllYEgfgSfwq78YLk3OvaVp0Uzo8dvJK+w4IDMMf+gGuP2j+rc99beZ6Dpv67yW69l2+49F8IX15qXhPTry/cPdyxZlZQACckdvpXn3/AAmPib/hZX9lfaP9A/tLysbE2+Vu27emc++a634ZXq3fga0Xdukt5JYZM9QQ5Iz+BB/GvN/tCHxHPr4kbyhqHmgA8bRNuzj6d6qvV5Iwfdozw9NylUVtk+iPeKKQEEZByDRXWcJzPj7V10nwpdHLCS4HkoV6gnr+n868w8JeJrrR/Elzp32ErJeWOY0hO9dyD7xHrjP6V6/4i8waeGiRXcOpAYZHUZrmpIJ4tatVit3C+RcPvYksHYHgE9BnoKiVO8lK+xrGrywcLbnMpaax5MUixT/LL5qx+Tkqc8E8ZIzWJ4h8TXOt+KtRkFi6CyjSJg/3omUgtt985r1C2W8WJLn7Ohu2jWIy4GSoP1x1/WqMf2o61qbGBHWK8aSE7sHO3HOCMjr1/oK5aNBU4ON9/I6HXc5qVtjo9K1JdX8NQ3ibstFlgeuR1/z71dKQXCK5jjkVgCCyg5Hb+dOsDIbOMyqFkKjcAOhxWJquk3cVwH0u6MCMkjPE7sU3YGMAHjPNdhxvc2FEa3MMMaqu0F9qjAA6fzNeY/HHVhHp2l6Ogy00xuXPoqDaB+LP+len2FgljCQGeSV8GSSRizMfqe3tXk/xlt459W08ME3i1bBYf9NBwMCpmm4tF05KM1J9DifD2p/2N4w0jUMHyoZUWXn+Bx5bH8N2fwq94t1RdW+Iupz4PlRObdOeojGwn8W3ViTG3uNct2t7dLeNTEhjBY7j5i8jI9P5VsalbRReJ9RvHsluIftNyCgVhz5rdwP85rglSaw3s2z1o4mnLG+2S0NvwJ4jbR9B8SWxUl2hFxb89XOIcfmYz+dZloIjpPk5JYv5ecnpjbUXg22VH1FbpVKm1U4fOAPtMeByKv30umwlYY2s1y4IK8Y5+laTwNTE0ocsvhZhDMKOGq1OaPxL+kexeE79tR8L2EzriVY/KlGejp8jfqtFQeCFQeFoPL27TJKcr0JLtk0V3uLi7M8xSUtUQeOfD1/4k0ZLXTbtLedZQxMjMoK9+V5rzy5+G/jO3uf7QjvobhoreSIW8F5IruWGPlLgKCM96+fv+Ek1z/oM6h/4FSf40f8ACSa5/wBBnUP/AAKf/GpaGnY94j8PeOUt1iGk6xuUg/NqUWODnrup6fCnxm2pXl6dSsEF4xkaN7iUshI6EhcEj1FeCf8ACR65/wBBnUP/AAKf/Gj/AISTXP8AoM6h/wCBUn+NJRSG5tn2j4W0q70Pw5b2V7MlxdRgl2iztJ7AFuemOtN1GLUtRkQQxSWsaA5JcZbPbgmvjD/hJNc/6DOof+BUn+NH/CSa5/0GdQ/8CpP8aok+4rS4uJVAuLV4WA5YlSCfbBJrj/HMds96jy2cM8iW2VaSPcV+ft+NfJw8Sa5n/kM6h/4FSf417Vb/ABBufDHgfww89jLqDXenszTSTNnImYYzg5ODUVFeJdP4ixpslh/bhWTQ7dxEYvlSL52JPX9Qfwq74+gt7TesaR2+9mlMkeAz5Zif1GfxrC0v4qm61NdmjNvlZUULK2clgOPlp3iD4mQwapd2N1oGZIJZIS8knzcOR021zKL5Tqt7+y+9HW+D7CK58MzSrY2ouHRYlk2fNId6t8344/EVhy2jWmo2st5abbcMGcyRbgFzg5H4H6Unhv4gA6VdvbaOwjtY1mk2OcD96i8/L7k/hVNvirHeXaA6f5X7zlfMJB5/3a6KeJlRpuNt/I554J16il/L5o9y0NLePSYltVjWHLFRH93kk8UVn+CbxL7wvBPFbfZ4jJII07bQ5AI9jRVx1SuZtWdj4hooopiCiiigAooooAB1FfYvwr/5JN4f/wCuDf8AobUUUAddb/60Uy7/ANcaKKAJrX/j3aov4qKKALo+6PpRRRQB/9k=">,&nbsp;<b><span style='color: darkorange;'>question</span></b>='Is 'The right image shows three bottles of beer lined up.' true or false?')=<b><span style='color: green;'>false</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER0</span></b> -> <b><span style='color: green;'>false</span></b></div><hr>

Answer: false

