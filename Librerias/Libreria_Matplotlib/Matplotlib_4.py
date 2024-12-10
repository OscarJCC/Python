import matplotlib.pyplot as plt 

fig=plt.figure(figsize=(8,6))

ax_1=fig.add_subplot(121)
ax_1.text(0.3, 0.5, 'subplot(121)')

ax_2=fig.add_subplot(222)
ax_2.text(0.3, 0.5, 'subplot(222)')

ax_3=fig.add_subplot(224)
ax_3.text(0.3, 0.5, 'subplot(224)')

fig.suptitle("Figure with multiple Subplots")
plt.show()