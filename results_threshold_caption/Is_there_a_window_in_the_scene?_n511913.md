Question: Is there a window in the scene?

Reference Answer: Yes, there are windows.

Image path: ./sampled_GQA/n511913.jpg

Program:

```
BOX0=LOC(image=IMAGE,object='window')
ANSWER0=COUNT(box=BOX0)
ANSWER1=EVAL(expr="'yes' if {ANSWER0} > 0 else 'no'")
FINAL_RESULT=RESULT(var=ANSWER1)
```
Rationale:

<hr><div><b><span style='color: blue;'>BOX0</span></b>=<b><span style='color: red;'>LOC</span></b>(<b><span style='color: darkorange;'>image</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">, <b><span style='color: darkorange;'>object</span></b>='window')=<img style="vertical-align:middle" src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCADIASwDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwDyXTIUuridJASECkYOOtaMmlwNuVd6HPBBz/OqugjN5d/7q1uMnzt9a93NMzxtPG1YQqySUnpd9zKEIuK0Ofme20uVEvLX7RHJnDRuUYY9ulXbZNBv8C3ujHIf+Wdwdp/PpWb4oXElt9G/mK5+uH+1cf8A8/pf+BMrkj2O+fQoohueB9vZg2R+YqMaVZ90b/vo1ydlrGoacc2t3Ig/u5yp/A11M/iQWc8cOpWiTb4w/mwfI3PqOlH9rY//AJ/S/wDAmPkh2Jv7Jsv7jf8AfZpRpFl/zzb/AL7NWLS+0u/x9kvkVz/yyn+Rv8KtyW80XLxkDs3UH8aX9rY//n9L/wACYezj2M4aPY/883/77NPGi2B/5Zv/AN9mrYNODU/7Wx//AD+l/wCBMPZx7FUaFp5/5Zv/AN9mnDQdP/55P/32athqeHo/tbH/APP6X/gTD2cexS/sDTv+eT/99mnDQNN7xP8A9/DV4NTgaP7Wx/8Az+l/4Ew9nHsUR4e0w/8ALJ/+/hp3/COaZ/zyf/v4avB6cGo/tbH/APP6X/gTD2cexQ/4RzTP+eL/APfw0f8ACOaX/wA8X/7+GtHdijdR/a2P/wCf0v8AwJh7OPYz/wDhG9L/AOeMn/fw0f8ACN6Z/wA8n/7+GtINS5o/tbH/APP6X/gTD2cexmf8I3pf/PGT/v4aP+Eb0z/nk/8A38Nam6k3Gl/a2P8A+f0v/AmHs49jLPhvTf8AnlJ/38NIfDumD/llJ/38NahemFh2o/tbH/8AP6X/AIEw9nHsY9zoOnR2szrE4ZUZh+8PUCrmjnGj2v8Auf1NSXjf6Fcf9cm/kag0n/kE2v8Auf1Nb1sVXxGAbrTcrTW7v9mQlFKehfJppNJSV5BoBJpppSabigBpphpxFNOaAGGmGnkVGaAGEVBLcwRHEk0aH0LCi6m8tQq8u3QVlnTE3NIQCx5JqJSSNIU3LVGorrIu5GVh6qc0uDWDLAyA+U5X/aQ4qGLXri1TyZoxKynG4nkimncU4OO5raJHAIi6Mvnvw67ucDpxWsU+dh71x5s4pY1k3SLIXC5Ta/U/3c7hWhp739pcJGJvtIfcBEWI5HruGRXsY/DzxGZVqdPfmk9WltdvV6bGMGlBNlfxXG2+2YKdoDZOOByK5uuyn197eR4prVVYHBDE4qsVtNU5TT7bee6TBG/KsVl1X+aH/gcP/kg5l/SOW7Vs+Ix/plsfW2Q/zqaTwvdljshZVPYupqbV9MvblopZLZ1EUQj+T58478U/7Nqfzw/8Dh/mLnX9I5qt/wAN3+oLdtBDezRoI2YL95SR7GsloYUYq0rK3oUINaOhjy9SzbDzpDGw2H5eMcnNN5bV/nh/4HD/ADDnX9I17TxnbygLqFjtbvLbnH/jpratbmw1D/jyvonY/wDLNzsf8jXnnl2//PY/980qRwb1/eknI420v7Mqfzw/8Dh/mP2i/pHpMkUsJxIjJ9RSbvasuCTWbeIG0iZI8A7HlDoeP7rUz/hIYXCx3VlskcZV4G4znHKn39KyrYGrSpuq2mk7aSi99tm+zGpJuxYn1F492yMtt6noBWlpxa+hMm8ADqoUk1Y8F6DJqUr3V1gw8qE7NnqK9Et/Dtmkflx2sSr3wuK8udR3sjthRurs4tNMgkhLQ3yFlGWQ9R+HWs4sFcpuBx6HrXYat4RtZAHijMcqjhkbafqDXneqW13p11l3wCeJcY59G9PrRGoyJ0kagbFOzVCyu2uIyHXEi8MKtbgK6E7mDVtCXdTg2Kh3il3UCJS5pu40zcKN9AEmaTIqPfRmgBt4R9iuP+ubfyNQaT/yCbb/AHP6mn3R/wBDnx/zzb+RqLSSf7Ktv9z+pr0F/wAi+X+Nf+kyI+38i/SZFJg0u2vPLEJBpMe1SrCx5A4p4g9W/KgVyqVo2E1c8pB2z9aMYHAxTsFyn5DHt+dJ9mHc/lVwimEU7Cuc7cf8hOQhlVY8KEPJfAyaSe+tXgUJb72POGHFRR24urqeRuGVm3H0p0AG2MhANi4bByT/AICueXxHdTXuK5BKqsm8QiPHUKc1g3qL9pPHauxdEntNyhCMZDL3Fc7Kg8w5A/EURetxVIrZBGPMtYxsdgs6gkwhlGT6j5vw71qWpDalYBXVgDIBtkZgOOnzcj6GsmBQsccjIAPPT52jYY/4GvT6Yz6Vt2zebqemtvLgmTB80SDp/e6/nX01T/kaYj0q/wDpMjz1/DXyJrw/6QyGRef4Gfbn8GBU/pWbdaZbld0loE5++qmP9RuX+VQeI9QurPUwtvMyKUyy7cqeT1B4/KqMHiCVSA9vHnOS0LGM/kOP0r56xrc1Y7W6txus9QmRR/DKvmJ+a5H6CrMWp6pEMy2cd0g6vbPk/kM1Ti8QWMzAyko/rNFk/wDfSYNX45ba6IaN1kPYo6yH9cN+tA7jX1nSLwCO8hKsTgiaLOPxqzY6Pp0N2t5YkZ2kYR9ykGoZ0D/LIUk9Fl6/lIM/k1VX021Qh/KltWPR4nKf+hZH/j1AGbdeEb6IloHjnX0ztP61kS2V1ZyqLi3kjwRyy8fnXXo+p26gxX6TJ2F0mP8Ax4ZH61P/AGzPEn+nadIIz1khIkQ0+YXKa1uubBD1zGh/SuFuCElsWPRt4/8AHq7K01nTJoGVLuJOBhHO0j865uXR5NR0qKeKVUaFpOGHXkHrXfQ/3Gr/AIoflMl/Ev67Hr3gm3ax0O1iuIZInZQdzDgk8117GWFB5cJkZhkfMFArkNEW9fTwt5J5rziPy41z+5wOfY54Ptj3roLqF9SsZrdJpIW+7uU/On0rxW1c9SN+Uku5biKNRd2/l7ujKdw/+tXFeMIka0xIow/3SBg//rBxXfPbb8ESAx7ArxhcA8dcev0rhfHGnT3dpBHbH51lwPxoWj0M5JtHnemiSPUPKbBbYQpx1HtWz5lFxYzGCG/8gR+RJsaQHq4HPHUVVvr6G0BkmHlKDg9SATVwrxa0T+5m1XK60JcspRT85xX6lvcKN1VYJ0u4/MtpEmXv5bAkfUdaUyYOCav2y7P7mZ/2dU/nh/4HD/Ms7qN/vVTzf9qk80f3qPbLs/uYf2dU/nh/4HH/ADLZcUokHqKp+YP71JuDHhuaTrxWrT+5lRyutNqMZRbfacf8yxdTILSYbusbfyqfRYC2kWrcAFP6msed8wSc/wAJ/lXQaJ/yBLP/AK5/1NevH/kXy/xr/wBJkeU/i+RbWBR1OaeEUdFFPAoxmuABppMV1Ol+H7W40M3t5JJHvDSI6HhUHfHfPP6VzBHPHSgdhhFNIqQikIoERYpuKlxTSKAOQgnFvqtzFLwsjkGrNvZW5kO5ncBs7C3H1xTPENi0VwLtB8j/AHiOzVSs7uYSZA3EDBxWM463OqlU0sa00yxq6qCoxwCMVkx6dd3a+ZDA7rnGQO9akVld6hOqFCC3QE8n/AV1MOhwW9tFDMw3qvJHGeSf61dClzvyFWqcvqea25CCJhIsbeevO9oz9c8r+PUVvW+9tT0tpCWY+b8xKncMeq8H61h2smFhVZQG89TtW42nvztYbfxretkK6npW5CpPmnlFUnj/AGeD9RX0NT/kaYj0q/8ApMjkX8NfI5zxdj+11AxwnPU9z+X4VhKcn1/Wt3xawbVxgg4TH3yccn8vpWEvP+c14C2NRM49v0pRwcjj36fypOnt+lAH+cf4UCOos7yaLws8gnbeGO0M7HPPoRtP4HNU7fxJNCcPBGfeJjGfyHH6VPbbv+EQuD8wBZhnEmDyO/3T+OK50nBNKw7nVw69YSNmTfC57vH/AOzJg/pV2Ke2uHVredHbPVHBP/srfzrhx7f5/KnL196OULnc29lFd3yxXEUciiNWw4wep9cE/mabpeoWkWnNbysysGY5xkVZ0gbryIoDtNspO3OOp67SR+YFcVc3UsNyyqQV9CK76Cvga3+KH5TFJ2kvn+h9EieAaNYz284h3MrpKD22/wD161bYQ/JN9t3MQRlsDP8Aj9K868Daz/afgWeyIH2+wffD0JCnoRn/ADxXW2X9rXyqst3dsF6b3VVHuQqjNeLKNnZnqU25K6OqllDW/wBwKwGGwep9awRLbQ3yPeypFGzY3t0X35rYSFLeySJMkKMZY5Jrz/xnebLeUqwARfLz/tOcfyzTSuyJysrnP3mpqum3Vmv+qWYsHBzuLNx+g/Wub8Rru0uVv9w/qKt3pAsIIV+9JJub6AAD+Zp+pRQT2LJM5SJkUM2cYp4fSCNM3d8ZU9Tg7Zil1EwJB3jkHB6+tbl1r17Y6nc27FLiGOQqqzDJA/3utQnQldt9ldxzAHO0nn9Ki122lGq3E4icxO24MBx0FdWjPLs0baavaPbwyzq9sJs7T99eDg9ORVpMSpvhkSVfWNs1y83zaDZN/dnkX+RrW0mGNy25RnCEEcEc+o+tJgmXyxp8LZfHsaWSORcfP5gx0kGT+Y5pIVAkJ2leD3yPzrGv/DkejlX++0vVEErDyX/3T/Kun0P/AJAdn/1z/qa5SZWELnqu08g57V1Ph1t+g2p9AR/48a9aH+4S/wAa/wDSZHly+JehpAVEI7m+1G30+xV3mkb5goAwuM8k8DjNTgU7w35H/CUtLd3bWywtuEjEBTg5C57ZB5+nvXny7GlJJu7Oj8c3EttbWtjZyeVH5ZdkTIyqkBQfbrxXMYp+vah/aU97qZdtrAxwrnog4H+NMTd5a7/vbRn60ou7ZdWPLGIhFJin4pMVoYEeKQin4pp4oAPIguEMUqhy3Gw9D6cVz2sSWsd9FHFGIygIZQu3A44/PNWl0a4GrSXn2po45cqqr95s9R7Aev5VLq+kST2xvAS8sK4fJySvrTmm6bVjSlZTVzV8NqosGu8ZeRikWeyjqfz/AJVpSPGHPmDcx5JNM0y08iwtoQOUiG7+f86thSB8hXHqVzn3ralHlgkZ1Jc0mzx63MjRwIpkYeePkVo3GcH/AJZtzn9DW7Zps1HSF8vYcy5XyfK7d16flxWDDEWhgLQlkM4GWtBIp4PGQdx/3f8ACt+xC/b9FCBAo84AJuAH4NyPpXrVP+RpiPSr/wCkyJX8OPyOc8XH/icDknCY5cHuemOn0NYK857/AJGt3xYR/bHG77nO7A7noR1H15qDR/Duo63HNLbRottDgS3E7hI0J7bu59hzXgI1Mjp7fpQB7fp/hWzeeGr6zheUPbTKn3hBMCceuO4+lZKxO7AKjMT0wuc0wsb9qjf8IncuI2xlgWEb4/76Bx+YrniME12mj+GtSv8ASJLKO0KzyElWkjAXB6HfnI/EGnP8PzpcoGvX8VqzLuWKEb3Ptx0P1ApDSbdkcT1pyAlsYyT2rt00LSQhEemzMR/HdXJA/wC+Vx/On2GkL53nWunB9hw/2eJjgd8MTwannT2On6nVSvLReY/TP3V3ZvMAP3CrlsHBz05CkH8/yrk59Mu7iZZUixC7bRKxAXIPrXsd94R1a4FvdtI0cHmeYzPJu25AwyqPoB1rmPDNhHqOlzWd9FFFAyyPDdElCJFPds4I7YI7ivSoL/Yqv+KH5TMJwXMrO+/6EHhzTX8Mz2l0t2s8t7uR1jzt2ZAHXvuPWvYbDUrbylBVhIBh0K4Kn0rhpNYtdP0qwtXilxawFEljAcPli3UH6V6PFYWmoWUVxsDPtGH6H6GvIqLW52JqMVZW/wCHKN9fs0DCIfN6+leY/EWddPsLCzJ/eTSNPIT324H9f0r1iaGGGHYkeGz6Vwet6JF4n1G+EjbhDD5McXQ8ZJZT/eBOcdwD9CQWplPVanmN8XfUIFVyMQE4B7jmuguIopLEBlBQoCQ3NYTJjxHHFneptiA2ODgGti+Xf4dl97b/ANlFKj/DR0Zp/vtT1Ofn0yDeGjLRnPUHH88f1pMajbcJceYv92QZ/wDr1gxXE0J/dSun0Na2k381zepbzFSrA8hQD0/AVtY865JJdrLH5V5YsFDbsxHofXFW9OubOOU+XcDlQu2TgjkGqC6rDuKyRsuCR0yP0/wqYpbXaggKwPtQPQ3L+6jtlTcpYNnBHsajhmzNt45QsKzZrVLfTI9mf9a4OSSOPSrMAPnxMe8J/kP8axrfw2ehla/22l6ojkkJibk/dP8AKun8Ktu0NB/dkYf1/rXC+Y4XAY49K7PwbIX024Q/wTfzUV68P9wl/jX/AKTI8qXxfI6Lz47bEsj7FU/exnB7VixWF3pupXGInmsJzuMqfMFP+1j7v44rWuYDPFtV9jqQytjOCPaqlulw2u2TTxNESWjlkhY7JE2ng9xz0BrglHm0LhPkd0Tx6VNqNuLeByEyC3ooqyyFGKsORwa6y2ihggVIVwnr3PuT3NZ9/YLNKGThjgEjtWqocsdNxVKvOzBIpCKkdCjsp6qSDTQCxwBk1BIzaScAEn2pUVkmG9CRjlSOnvV6104yMs0gIKnIFTXcHl/vF+6a0jHqK5RiQNJ8/oQD/KrkEK4IdcqwKsD0IPamxKCoyeSM1aijw688ZHFapCHqm1WXpn72PT0oOfSpZQdxCjj2pgA/yKoR4taiMLHIzwxskm7cwlQnHbeuQP5iuitZPN1DRH37xiX5vO8wd/4uv581h6dKiJjzij7uiah5Lf8AfJGK2lVmvdFyZSWEnMhViR9V4P1r0qumaYj0q/8ApMioq8Ir0K174cm1fXBM3yWo4c7QrNz0GOv+8a6q201re38iEBbftAV+Ue4754HPetzTLFcB2GTUmoskG3HHNfKSrTvZHoRpRWpQezSZA5iUZHI6giquoTxWxZYNNij2qhkEJCmQZ+9kg456gY9a19OdZ7a4JyI1ZlUj/PrTJLTTr4zR3MaySCEruDbWX5SSMjp2rvvKVNN7nNR5IVXpdI5mbV9SluFntgbZ2cgxQE+ZL/ss2ct+ldjF4Ul1jRfMEa2iSLvVpCGkz3+UcA9uTVaa20rR1W7W2hj3IrEgbmJ46Z5qxonjOP7PcW8UXlrHLhPMOTgjn5R9KyjbaR3VeZrmpKy7/wDBIrXQdLshHcSxrK4+SSS4bdhux54H5U/UNb061ZlSTzWZR8kQyB/TvXDa5q80+r3qhjKUfALKeMDsB0rNke7mEZLMA3GCQo/xo969krFRdOylN3Z61Y+JJL/w80EEKLIN0SBzuYnsMD6iuF8KR6jLpUMZZP7PM7wyQleRk8uPcdPpmp9Gml0XQL27OY5zPstTtI/eMB83PXaAT+FO+HV2zWssNzAJLOESMz553McDP6mvTpL/AGGqr/ah+UzjSSnzJbX/AEM6BY/tcFkgwsl0rZUdVO3gfhk5r1zw1qS3ltPExw6yM6j1Qscfl/UVwdp4d0//AISYNGXEO0qYs5XJXgj6cVf0rSp9Hu4ZbGWSV4pWiEDtjK5OVB/oeM46da8t07xOmpWU5uNrW/zO4umwkp/uKW/IVxNxp8qebhmU/K5ZTg8gE/1rr3lWZfMUnZIncY4PrWPdkyXbL/CwGcVzptMlpWuecNZ3Xk/boALhHmaJ4Qufm6jA6jIJ5HIxSXtsILKSJoJBELcMEZudjKcDI78EfUVN9qa0iMiqMi72sADn/PUfjUuti4gtPNuM4dzboHwDtPzcn23k59DWlFfukdebe/i5pbpnlFw8Ek5a3haGIgYRn3EcetWdEONZtfd8foaqSwyW87wyoUkjJVlPUEcGptMbbqtqeP8AWr/OtzxSK6XbdTL6SMP1rY0v/VxEDruU/kahTSLrV/EU9jZoDIZGJJ6Ko6k+1dVp3g2/WZ7eC4t7lIpColQkK7AZZQD3HQ57iplJLRmkYSeqRnXS50x/9m4P6gGktSWEJ44jYdPYf4VJKM6ZdDjKyIT7fKBTLEZiQ+in+tYVv4bPQyv/AH2l6oxTXW+CH+W+T3Rv0Irkz0rpfBL4vrxPWJT+Tf8A169iP+4P/Gv/AEmR5L+L5HaVma89xFphmtsiSJ1cMOq4PWtSkIDAggEHqDXEBZ8M+JItXt1jJCXAGHjz0PqPauiyGTf6fqfWvJ9T0+50O9XUdOYrGDngZ2H0PtXXaH4qi1SM+ZiKRDuaP/D1Ga2hUvoxNdUa1/ZKzMwGGznj3pttZpHIWXPPBDdvoavKRcFSSDkbsjriheVY5HBwSa15VuTcMBR3X6iqdwSY5Y/4cBh3qaSRkBYHav8AeJAFYWqa/YWit59xb+YBwEBLk/QVLshotWTbojnqp2mrsRwRnpnrWdYsrvuQ5jkw4PsRmryvuOe3ahAWW+9TgGxwaQfeGfpU22rEeLabHPJb4jFyy7zwlvFMv5Md1blhFjVdCjZAp/e5HkeV27r2/DiuYtoo2i3SRRN8x+Z7OR//AB9TXTaQU/tTw+EZNo80fIWIHB4w3I+lehW/5GeJ9Kv/AKTIqHwx+X5npdqoSIY44rnPFt0bS3DEgMzBVJ6ZPSustoi6ZCOQoycDNcx8Q9I/tHwrcSW4YywYk245OOo/LNfJxXvK56TfuuxkPrkFpYNDZyecsSfMEIx7kn3P86wF1C5EMlw/zXdyP3Ua5DFT1f2HAA9s1wAdl+6zD6GkGR04+lehJ825xU5undx6nZ3F5JduqvcQW4Q7cNLzx/8ArrW8O3Gm2bXRutYs4/MZcN5nJx1xx/OvNx0NJnmpjaOxdStKp8R6kdV8OC7n+zusoZ+G2PMze+PlWr9jqtnLLDb2jNC7SKGK2axkAkA/MSa5X4cOXv7/AE9iBFeQ7CffnB/nW5ZaXpyzwSOdrsdrjzMFXHBH/fQB/Gmndmkfdp3t/Wpsa3P50On284+UySyHJ7ghR+lXPh9arH4TaePaTJcSNKD3C4GPyp/iTQZkitLvTyZ4vNcmNzyA6q3B79DUXgxtvgCZlYB1af5T+Fd1K6wVb1h+Uy+eNTktvr+hyumXkyavsS4mjiEmRGGwF5Wt/wDtO+g8USRLfO8X22MlJMEFWIOP1rFh/d60qmMHdKB+eDWrqscY8TRFkwJRbvnHoQv8xXn3fKvkdHJD200/M76z1SLUvtYg+5FIU2txIrDghx6579DVXUG+zRRyPIIxJMkZbvgnnaPWobOw+yeMvPWNhFd7kLDlScAjPpyD9apeNLy7F0YbJT5FoVFxIpA2yPyoz17dvxrPlvUuYtcsLJmRZXenWnh/V2c/6TDcIykKWOzLYx+NF7cJ4q8OTPEsivGq7kYd1GCR9Rx+FZVqWuY9WVdoEsIfr3Eg/wDiqb4W1M6bPHE5Zo528qRQOd2TtIH1JH40qMr0kj0MypOONnPfX9E/1PPtdtzFf+YVfLj5yRxu9j9MGqNm2y+t29JVP6163440ddLsZ2eFFlvcYgB+RG5HOOAe/wDk15zZeHLyeYMHRAJAqOQxVjn1A4Hua2VzxqkVe8dmehfDKwWfx7rjMit5cAIDdOWH+Fd//wAIhF/YthprMjRQyme4IGDI2WbA9ixGfYVy/wAP7c2V5rmpSo/kzNHGrx4JbA6L+LV6Hp6O8DXDqQrnKJu3FR7n1+lc0/iOinbk1PJtVs7nXJr3T9P0xg9s3lmUjZvG7gNnAGMHHtWDLpg0mUWxu4biURFpPKziNs/dJPU8/rXd+PvEV0bi40y3l8kpbl5PLb5snpz24rzLTW+Rvfd/IGpqX9mzry5r69T73RkHpW94Nfbrbr/egb9CDWCela/hV9niKAf3ldf/AB3/AOtXtR/3B/41/wCkyPGfxfI9DoooriEI6q6MrAFSMEHoRXH6toc+mTfbNPL+UOSF6p/iK7GkNFgTMLT/AByIbONJdwkUYZSuVPuD1FOn+IJRGFtbDcf4mzx+dOn8M6ZNKZPLkQk5IR8D8qnt9E060IaO1UsP4n+Y/rVc8+4Wic/Jfa/r75XzPLP8X3VH4n+lWIfCaiFmuLgtKQcBOAD7k8mum7Uhqd9x37GP4T1Qsn9nzHE0PyqD1K8j9M11FnJvKKeuea4jVbU6brNtqsXEZmUyAdj3/MV12msDdDHQbjWtN9CWjcBDg+4qVZMrzjNRRYaJCO4pev3gc1uiDxG0kiRPmkhVs9754W/IDFdf4bgF74k8MRyMzRs0vzGYSggAnhu/0PIrlbJrkQARC7K7j/qo4nX8m5rsvCbu3ifw1FKHUgXJG+ERkEocHA4PQcjrXoVf+RpiPSr/AOkyNIfBH5fmj19ojaXkyQcJ5anJ5x2qpfaPOggjsI2lMr7HzzgEcsa04lWW4hlY5SWHacHoR1/Q1qWEqxs0bZLxNsY/Xofxr5dRu7M77u2h5jq/wDsNQja6h1E6feSAfuY4g8W7nJxkEZ46cA59eOJPgjwZ4d1qHQPEOq39/q88iwuNMQLFaFuhYkEu3IOAK991jxXpGizKL28Rbj+CBAZJW+iLk1xWu3f2qe51/TdCl0i6ulWGTUpVUXRXGBtGT5fHGcZPHTFdnNGOjORQlLWx4Jqvhi50TVNU028kjE1jK0Zw6AvjkMATnBBB49awdvPUfnXqp8KQFZ1F/dnz2LSGTZIzE9SSy5z+NZkvw/tEjZkvbpmPCrgdajmQrHNeE75tP1yKVWwBy3PYEV0/iW2ih152jYhJmEyHHGG6/qDVf/hCf7OYXYvzMkfLxtHjcvcZzxxmup8QNa69pmjRQlYrxYGIZ4yFZMgAk+/WmkmdEKjS5ehDLqV9p2m27RyjYWgJB+ZD8rDkdunauk8ADT774fy2dxgTM8+Ox9eD3rldShubXQrUXMDR7mjT1VwrN0P4ipfDtyIPAk+8HaXkAYcFSSB/WvQou2CrX7w/KZUoqpKHL5/oSXHh26h1jzILkOqsG2v16Vr+I9Kv4dU0+fZEQpdMBuu2QMP0aubtvEV9FeESSR3MYyMycNgL6jrXR+JtfnltLY/ZowwnxzIe8Iz/ACFcD5eQtKosRbXVnUXupnS9SiguIzBNIS0bP9xiDwD+ntXn+p2rrq0FrLIsl7O/nTlMtgk4XJ+pJ+mK6vV7iPxEmiz3QntUFq7GWJRIAzKpXI4+XOc1n+G/EVnJqMs93BJvhLHzGQNuI+VenufTtTULu7M3W5adktepzenhP7RvIFZsG3l2gDrjDD/0GlhuNK0zTFu7WGSa+dHWbIyF+Y8g9sDGRyelTW+sWmjG/u5WTzoo52RWXqxUhR09SK4TTNSeK7h8+T93u+c7c/8AAvrXNQsqaPSzaq1i5J97/oej2Osx+IbbydQhWaRBuMzLxKBgAj+6Rn/CrE2nH7MrRpsjThFHGazdMms4dQvYrWfzEmjiclcBCec7cdBkg49Tiupt7uCfTVUkZTIPsa2m5RhdPU8yTjKpa1lbRFDw5cLpMcsMrYSV96jHCsOMfliuqtPENlpeiz3F1cIkUTM+S3IFee67rekaarPJcyecRwkLct+Feaazr11rUwDkpbp/q4hjj3OOprCMXIcqiib0/iC717U7y6gtsSXBZnduy44H4AVW0pWCuGbJHP6GrXh6Ly7ZBjlv6qag0ziW4X0X+tFb+HI6srd8bS9UZR6Vd0B/L8RWJ9ZNv5giqJPFT6a/l6vZP6Tp/MV60f8AkXv/ABr/ANJkeU/i+R6lmjNJRmuMQtJRRQAhpCaDTTQAE0maCaTNAGfrdt9q0meMDLAbh+FHhK/NzZyMx+eIBDn37/pV48jmsrR4FtrnUY4ifJEqhRjo2Mn69qqHxB0O6tP+PSHHPGfrzUigBeTzTNPANlGB2yP1p+a6ktDM8Jj+z7f3gtM5/wCWtvIx/Na6vQ2dNV8OGzaMSZkCeSWxuPGMNyPp/jXNWzYQASOvJ+7qCw/+OkVv27zJdaE6u5kVXZGeUSdOnzDqP1r0qn/I0xHpV/8ASZFL+HH5HquneKLOO/u9IvblYbu1kKyQscGJgeoz1Xvn3waqeIPFmj3cVxaXd/JaSxpg3dpK3y+h3LwDnoD9K4bxDoR8Y+Mf+EmhvbGDSLwRveztcIptGCBZFZCd24EHGBzkVi+OtbtNQvri30UNHpAn8wZGGuHxgyP/AEHYe5NfNumr7nUqr7GBNrtxBrM95pMtxZRs+Y180uwHT5mPUnqfc1eufHHiS/txbz6rK0YOcKoXJ9yBXNv2pFODV8qepmpySsmdNaa1qTwys9/NuX7v7xF/Rhk/hXRaFqd7f+GNTlectdQltj4GR8mR/I1w1rIY1fnGR0yo/n/SrmnNeGxvo4LpoYsIZIlbBlJO0AY59e9DQrmro8uqeKdQi0+6uma0z5s+AF+QeuK1b/Vbn+0jPG0Z3KMIRwFHAA9OKu+BbJLXw3qF5JGwmm3ruC/dVV6fnWGRHLNbudyByAW6YGcD+VG0kddFJ0pLr/X/AAD0V9fs7nw/bW17brEjmMsH+7gmQjnscgflWBpOkXr/AA+jvbQrJG906NHnDDBz360moQSx+GlQEPlrc/TIdsfrTdC1K5g8BrFBMAgu2V43XI57ivRg08DWv3h+UxUoSjVhyb3f6HNxQyG+2zW0sWT83BHU89a2b+T7dqEFkwkOJSZQpzhmwCAR/dUY/P0rs/D+vWM3hxluojHJJ9oceYm9flQ45x2z6VL4f0jQdT0LUJrGOKK8I8sSxucqGAPC5+v1rglHomOnW1cpLVGRqviW1h0qazsQZ5CxjWTosJXjOe42k+1YcF7B4a03M9wn2g4kETDBJH3AfTklj9AOtb9vp2iQ67PZ3VrBa3E6kxL5zP5fpg9xkf5xXmvjP7NcGC6to0C/cZkGATj888Zz703exm3FN2KniXUJZJEt92VZRI7d3J/p3q43h6aO0FzHIHwqsU288jNY+vDN7D/17r/WvQtPIa2Q/wB6CI/+O4rmpfw4nXmsm8bUv3OU07VbS0jmFxLJBPBloxGhb7QpI/dnsCDzn0z3AqO68WzSjFtAIDzuLSFgR2HAFUvEsIi1yYKMBlVvzFZOK3i2lY86Tu9SW6uZL24a4mKmRzztUKPwAqbT7eKaZQzncD93HGPr6/hUlxaxR6VZTr9+Qvv59D9abp2BeLzjg0mB1+lYHkgYwCg/Uj0qhaZTUbhPZh+tT6a+JIwMkA5zz2f6+9MRMa/On+0386wr/BL0PRyr/fKX+JGIelETbLiJ/wC66n9RSyDDMPQkVE3AJ9K9Zf8AIvl/jX/pMjzPt/I9aJ5P1ozUcbb4kb+8oP6VneIXlTSGaFd0nmJgfjXGSjWpK5/Ur2ddX0NknZIpzl4wcB87e3f71dAASOhoAQ0hpxUjqMU08UANNNzTjTM0ABqKylSUySRnOJCAPUjj+lPZgASTgDmodI2vZI8SfIwz7n3qobgzq9JYm0IbHDnp9BU5YAkEVU0hiY5lyOGBH5f/AFqtuQHOfWulbGZ4OlzBEAsk+xgen2NJP1JzXS6bLFLdaE8TKy4lBKxCPJ75A4z7jrVTS/DVrqVkl1NO6szEFQR2ra/4R+1jjt1trqS38jdhkOWJPU5rvr1qdPNa7qOybqK++6kunqWk3TVvI4XVdj683ll2+fb8+M5z2I6ii6BFuQwwRjrXS3fhq2gfzhcuzA7txTnND6SLyDKXM8y7fm3LwK4HhsJ/z/X/AIDL/Irml2OI+8aXbjvXbDwraY/1sn4RUqeFLbaN0smfaKn9Xwn/AD/X/gMv8hXl2OVs7lbaOUMZNzjA2BT+e4H9K1PDE1vFqry3BG2KFpAPVhjb+prY/wCEWtl6STf9+hVa80ZbVEeOWTJcL8ygYzn0+lH1fCf8/wBf+Ay/yLhzSkkonpVtrunWnw+lCSYYhwf3Z5y5B7Vxeo2F/wCZ81mXR1UqU9CTg1TksbsxadYLf3Dm4QSPDu+VAeeB+tOaeYXaR3Go6oD8o3qwbH6iqWGwjkv36/8AAZf5HQ3UjBtR6+R0GoTCfREfOx2niQoeCNsR7VD4bszceB7htm8w3bSAewC5/SrEnhuDUbO3kHiDULguY2KSKMrlWwcE+2PxrsvBvhJLXRZ4IrmVv9IcZZODkL2rSosPTws6UKnM5OL2a25u68yYVppxqNbP/L/I4fQ5HfR7iFGDC3W5OO4BTj+tS+FXmt2vHjXZItpvTjPIJ5/z61RhjuNIvdVtp4nRWt54RIPukjkfmMj8a1vB4c6nKAwKC1IJHu4/wNeS3qjtg04T8rfmZzXz6j4jsLmNAJNkatg5GfM7e3Nch4igmFkqKu4LOQ20ZP8AFj+td5c2SaZq2ixy20dsUxDI0QIEjrg7jnuap3TW1gnmsxEkrwyNgE4ysn8yCappqxzurFxlbS/+Z5/rVtPJewFIZGHkoMqpPrXaaRKRDCspCj7NGBnjBHXPvTG1GwznZIfolQtqVn2hlP4AVyx9pGKjpoduJq4GvWlVbmm/KP8A8kZHiW0SbUFlVLiRigB8pQRxnvWN/Z8h6Wl2fwH+FdU2qW4+7bSfi1RNqq/w2/5tVJ1ey+8wccv/AJp/cv8A5Iw3truSyitvsNxsiYspzzzTI9NvI2DJZTAj1cf4VtHVn7QL+ZqJtWm7Ig/Ojmq9l9//AAA5cv8A5p/cv/kiK0/tWE7RaIATnLt05rRlVk8QTybTtIJyOnbvWedVuT0KflSR31xLOgaQ7WIBAHFTNVJRadjow1bA4erGqnN8rvsv/kijdMqXUq553kfrVV5MMVxUl6p/tKb3YN+gqvLkSHpjNevH/kXy/wAa/wDSZHjW9/5Homh+ILO/SGzUulwsYG114bA5wR9KXxVO8OhsIpNkryKqkHHuf0BrlrG1XTv7F1ZJGIlmKyg4wvOOPwzW54vEkhihGCqL5o/8eB/TFcTfusLLmRyV1q1xdrZqzFfskapHtOMEfxfXgflS3Ot6leKFnvJWUcBQcD9KzWJExXIA5OTUkSh2TPRsc1L2NFboWE1C7iGEuplHtIasL4g1aJQF1CfA6Atn+dQ31l9jl8vO7BIJ9x/+sVuaR4WTUtNiumn2b85Xy84wSPWklqDatc2/DmtTask63AQPFtwVGMg55P4its9a4zwvm08QXVqe6Mv4qw/+vXZd60i9DKSsxk2BDJnptOfyrK8Na3p76bBC8wt5FG0rK2M/Q1Pr9z9k0a4kz8zLsX6txXE6dj7M+QCAeeM96uG5L2PY9LuYMv8Av4uVBz5i88/X3qzJd2okP+kwf9/V/wAa8YuUTagEad/4RVMxg/wR/wDfNb82liDVQJGu2N7lV9BNgfoKXc/ae5H/AG2NMzS5rV5tjW7uo/w/yK5I9hGMp/5eZ/xkJrct9Fjl05pReXgYKxCiTjOM+lYZrqtInj+wbZJEUcfeYDtSebYz/n5+X+Q1CPY5EGXAP2ibn/bNLmX/AJ+Z/wDvs0g4JX0OKlSGRhlUJFH9rYz/AJ+fl/kL2cexH+9P/LzP/wB9mrNlYHULyC1+0yhpH5JbICgcn+dNFrMf4R+Yre8NwJFd3L3DxJ5drIylj3IxQs1xj/5efl/kXCEVLYoW2m215rl1FDeXJt7eORhJ5nzYVcDnHrgfSqc2nBLtEW5kblRndzXTaPDBcxay9pEJIoodrNGvPJJH8q52cRx3uWiZSWHBHQkU/wC1cbzL33t2X+R1qnS9m7rW5oalogsLKG5F1ebwIcHzcgblJOOOMVseHtEbUbKSX+2dUjxMVxHcEDGBz9eabqbQz6K7xSFcC3kVSe2Np/nVzwncSRx3MWxWAkV8465Hr+FL+1sYpfxH+H+RSw9OVJu3U5tbO1XUpLXUb7UPLfdtZJd2cHkNn2rrNA8BaVe311CNT1FFjTgxShCcORzx9D+Ncpq+yLVPMXKuszjBORyea6W5vF07xDaySLxI8yzMOyErj8iM/nThm+Msm6n5E1sLBTcYre1vwMzXNCtrfVHjTUNSnt0ufs8czz7j5ijlTxwRWT4i03TraZBZ393c5UFTK2TgMynsMdOPxrpPE32y1ngkUP8AYFl85Bn5VkOAc+mcZz0rHmsDd32rSyvtS1gO1e+0DCY/LP403m+M/nf4f5GccLBa76f8D8zmfsw/56SfnTTbj++/51PTTU/2tjP+fn5f5HNyR7EBgH99/wA6EtjLMsSM29jgZNPYin2hje4IMgRguVYEZU560f2rjP8An5+X+Qckewn9nHgtMFHqTUTW8CHDXsY9wc10O6z+zIlw0THaN4JB5/OoLuDTpbbEKQK+RyFA4o/tbG/8/Py/yHyQ7GIbazRSyXiNgZYKO9QZjwhjclsjcM9B3x71YnjgMLiPbu2nPY4qkDFEHO4AdM0v7Wxv/Pz8v8h+zj2EnLJPzghuVJ5OO36VNb6RdajDLNA0AWNiG8yUKemenXpUR1CM7EFurlRjcx/+tU1lcC7ulh8lIwc89a5sRmGJrx5asrpa9DSNOK2NkQW0nh63059Tty7Ts9vKisVwOucgEck8mrWsXaXlxaeRPbs8cbRzbpAAQR2z1rPe0CgKZBhSQvy9PpzTHt0J5df++P8A69cXt0a+wZp+EhpZsrkXdvYvcJMpV7hFYlSBkDP0NZPikWX9vzfYBGISiH90AF3Y5wB0qlaoPtkkZbHGemc4NJfqFmTBzleuMd6ftL+6NU7PmKs1+19KzPGqHGeCeeAP6Vq6Pp11dW8ktvLMoO6JgjAAggZHLCueT5bhh7kVrWA3K6k4xg9M1cpcupnGPMrFkQXGj65CodopG6MwVjhgR0zj9a1H1TU1jZm1GLcP4VCZ/QGsC9URSIwOR16ehrQXg8SH8hUOpZXK9ldj9Z1K6v7COOYpsjYMcDlj05qtpig2EjYb7+CRTb4/6K3zE5I7D1qHTpZEidVYhfMJIrejPm1Ma0OXQu3a7VQHOOvSqfHpVmWR5Au45x0qvjk/KDXRcwNEWzH+I1ILQnqT+dXAABTwBgVw3Z02RTFkO9SLZrnoDVsD0pwHpSuwK62q5xin/ZVznaBU9OB5oGQhcFVJOSaltrpbS4lkeJpd9swVQM8g5JPtimSYDK3oazrq+a2tppgdv7kxp6ncw/wNWmENJa7HXeDtVi0nwfqTS20j/aZSwaPAIwAAKoyeI9PN+f8AQ52BYdYwTnA964a18Qalawm3W6YwMCDC4DL+Xap4dSgluA8haE7gTjkVqrpmnNTnBp7tnqOp6j4evdCcSRpDI0dtkNGUIXvyOOuK1PBugabdW15JYXsikunMThgfl7iuNaNb3Q5HinEhayG0gZBaMjI/IGl8Jy/Z7u4baTIUR1eFtpABI+vcUOXvK5oqP7uVn2I/FWj31vfzrsS5QO/zxDDde4/wpmqn7TY2140wBAWOQ913qDn81b86qTeIdQj1RvOdpwrndHKcMPmycH/Guqu59G1LQyi+ULl5Ytwf5WysZJ789etJRThoVKpOFZX12/yLGqFjYPbo8JhhiQ7pHAVlJwq479MmuU1QC3SLzpWhluxtnAOVTHCIR3/vEnrmui1e0ttV8O6TNbSRm7tpNkpU5LRgkEHseQPzNYEkgfWoRdJ9pF2PJli2/KBxhh6EZH5Gm1ZXMk+Z8vU5x0aNyjjDKcEVG1WbsrG7wu4MsMhiBPV1HQ++OmfpVRjUnPKPK7Mr3XML/Q4rMLEDg1pTgsu0d+KhFgm0FyVJOMBWbA9TigkjiCvY3DlFLRgEMR6mr+ji2TTWmkAM+8qp8zB7dqpi2ZI5UwdrLnhuDyMVHLYFYoHi/eM6B2UIcockFffAAP40tHoUm1qjQvLq3Ccvh+RjeD2rJuLlJI9qKc/SrVhZlFlllUAkFEV19e+PWoryySCNZYnyuACD60JJBdsfOLD+yrJoIZVvd0guWZvlI42YHbvmk05iupx8YXPr1qGRM6bDOAMmYxk/QA/1pbMt9tgKgnnBPpSqLQqmzpbnzXuUhgjDyOeAW21RsZbrUnkS3tQzRjLAygd8d6m1JpldHgcpKPuMDgg8VW0iWbSbl52XzS6FSM475zWNKnCSuzarUlF2REsVyusCFYR9oZmQx7xjOM9elO1WG7txF9qt1iyTtIcNn8qbd6g39sLfrGFKyq+wnPbHWp9Z1c6haoj26IUfIYMSRxitVCO5nzyuvM59zi5z6nNaemrcTTNFbRCVyuSpYLwPc020Nv5F0s1ssrsn7tz1Q881LoNz9n1eA5wsh8ts+h/+vim0nZMV2r2Halb3cKoLq3EW4MFIcNn8qs29rqM1vHLHZBkdQQ3mqMitDxPta0gZWBKy44PqP/rVY8PzCTRLcEjKbk6+hNP2Ub2J9rO3MYGoQ3kMK/aLYRIzYB8wNz+FQ6c3My+4I/z+FbXig/6Lbj/pof5VgWbbZ2Hqoq4xUXZESk5as1JV4BH5VWbIbjNWid0QbmoCenOPwrYzN0NkdaeCOKKK4ToHBqiWR8biQR2GKKKyqtq1hocLhlA3IOaUXDb8BR+JoorP2kh2GNIZzsGAv8R/pWR4ljKpbMp+XldvofWiirpybqIUl7pgCnUUV3mJYtb66sZhLazyRODnKnA/EdD+NX9P8R3Wn3STCOKTbkEY25B6jjj9KKKVrlxnKPws0L3VbPU7xb6IFGJ/eQv95eMZB/iH+cVs6/YxpbieFkkhW4RQCozjy+xooqXotDsoSc2nLyOn8IziHRUeTykiDS5EgG0rk5B9v5VhawHjkF3EGglUm4gw4YY/i2nuuAD+NFFUtY2Im3Go5I5DxFqttqGqrc2MbRrtBct/E5649qtWel6lqNotzaWFxNC2cOiZGR1GaKKLHLOTbuyleQTWUwS6ieFwekgxQohnAL8kDgq+2iioe4IR2BDYxgKQMUyGYWc6zE7uc4JxRRSB7EF1qayO42JguTgkmqUt2Zk8ts7P7qgAUUVRKLpCP4WmdBgR6imPYNG3/wARVS2u5YXSJWHls4yMD1oookaQNvUZCIldfvBSRn1ArEGqXHfYfqtFFY0fhNa3xDWuGuVZnCgjH3Rilknkl5ds+w4FFFaErZDVZlzhiPXFAA/GiikUiTe2MMcg+tTWKbkl6fK9FFCZMkFy0eFVZQzZ6A5qCFttyh9ciiitImMjZyfKOOlVS3PXFFFbmZ//2Q=="></div><hr><div><b><span style='color: blue;'>ANSWER0</span></b>=<b><span style='color: red;'>COUNT</span></b>(<b><span style='color: darkorange;'>bbox</span></b>=<img style="vertical-align:middle" src="data:image/jpeg;base64,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">)=<b><span style='color: green;'>3</span></b></div><hr><div><b><span style='color: blue;'>ANSWER1</span></b>=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if ANSWER0 > 0 else 'no'")=<b><span style='color: red;'>EVAL</span></b>(<b><span style='color: darkorange;'>expression</span></b>="'yes' if 3 > 0 else 'no'")=<b><span style='color: green;'>yes</span></b></div><hr><div><b><span style='color: red;'>RESULT</span></b> -> <b><span style='color: blue;'>ANSWER1</span></b> -> <b><span style='color: green;'>yes</span></b></div><hr>

Answer: Yes
