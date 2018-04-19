# Demo script for WiltingPriesemann toolbox
# MR estimation according to Wilting & Priesemann, 2018

# This script generates a branching process, emulates
# subsampling, # and demonstrates MR estimation for 
# the full and sub sampled activities


import WiltingPriesemann as WP
import pylab as plt

# Define parameters
# All variable names as in Wilting & Priesemann, 2018
length = 10000
m = 0.98
activity = 100
k_max = 150
alpha = 0.01

# Generate branching process
A_t = WP.simulate_branching(length, m, activity)

# Emulate subsampling
a_t = WP.simulate_binomial_subsampling(A_t, alpha)

# Perform MR estimation
mr_A = WP.MR_estimation(A_t, k_max)
mr_a = WP.MR_estimation(a_t, k_max)

# Plot results
fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

ax1.plot(A_t, '-k')
ax1.axhline(y=activity, linestyle=':', color='red')
ax1.text(0.5, 1, r'Branching process, $m=' + str(m) + r'$', transform=ax1.transAxes, ha='center', va='top')
ax1.set_xlabel(r'Time $t$')
ax1.set_ylabel(r'Activity $A_t$')

ax2.plot(mr_A['k'], mr_A['r_k'], '.k', label=r'Data')
ax2.plot(mr_A['k'], mr_A['fitfunc'](mr_A['k'], *mr_A['p_opt']), '-r', label=r'MR estimation')
ax2.text(3, mr_A['r_k'][0], r'$\hat{m}_\mathrm{C}=' + str(mr_A['naive_branching_ratio']) + r'$', ha='left', va='center')
ax2.text(k_max / 2 + 2, mr_A['r_k'][k_max / 2], r'$\hat{m}=' + str(mr_A['branching_ratio']) + r'$', ha='left', va='center', color='r')
ax2.set_xlabel(r'Time lag $\delta t$')
ax2.set_ylabel(r'Autocorrelation $r_{\delta t}$')

ax3.plot(a_t, '-', color='0.4')
ax3.axhline(y=activity, linestyle=':', color='red')
ax3.text(0.5, 1, r'Subsampled branching process', transform=ax3.transAxes, ha='center', va='top')
ax3.set_xlabel(r'Time $t$')
ax3.set_ylabel(r'Subsampled activity $a_t$')

ax4.plot(mr_a['k'], mr_a['r_k'], '.', color='0.4', label=r'Data')
ax4.plot(mr_a['k'], mr_a['fitfunc'](mr_a['k'], *mr_a['p_opt']), '-r', label=r'MR estimation')
ax4.text(3, mr_a['r_k'][0], r'$\hat{m}_\mathrm{C}=' + str(mr_a['naive_branching_ratio']) + r'$', ha='left', va='center')
ax4.text(k_max / 2 + 2, mr_a['r_k'][k_max / 2], r'$\hat{m}=' + str(mr_a['branching_ratio']) + r'$', ha='left', va='center', color='r')
ax4.set_xlabel(r'Time lag $\delta t$')
ax4.set_ylabel(r'Autocorrelation $r_{\delta t}$')

plt.show()