# -*- coding: utf-8 -*-
"""
Created on Wed May  2 13:00:25 2018

@author: kahl
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 10:34:22 2017

@author: kahl
"""

import json
import numpy as np
import matplotlib.pyplot as plt
# <--- IMPORT PACKAGES


# READ DATA FILES --->

file = open("C:/Users/kahl/Documents/Data/review_observation_json.txt",'r')
observation_data = json.loads( file.read() )
file.close()

file = open("C:/Users/kahl/Documents/Data/review_truestate_json.txt",'r')
state_data = json.loads( file.read() )
file.close()

file = open("C:/Users/kahl/Documents/Data/review_filterstate_json.txt",'r')
filter_data = json.loads( file.read() )
file.close()

# <--- READ DATA FILES

# RANGE TO PLOT --->
n_observations = len(observation_data["time"])
t_step = np.linspace(1,n_observations, num = n_observations)

# <--- RANGE TO PLOT









# PLOT --->

# observation data
fig_obs= plt.figure()
ax1 = fig_obs.add_subplot(311)
ax2 = fig_obs.add_subplot(312, sharex = ax1)
ax3 = fig_obs.add_subplot(313, sharex = ax1)

ls = ':'
col1 = 'g'
col2 = 'r'
col3 = 'b'

ax1.scatter(observation_data["time"], observation_data["y1"], 
                  color = col1, linestyle = ls, label = 'y1')
ax2.scatter(observation_data["time"], observation_data["y2"], 
                  color = col2, linestyle = ls)
ax3.scatter(observation_data["time"], observation_data["y3"], 
                  color = col3, linestyle = ls)

ax3.set_xlabel('time step')
plt.title('Observed Data', y = 3.0)

plt.setp(ax1.get_xticklabels(), visible = False)
plt.setp(ax2.get_xticklabels(), visible = False)

plt.subplots_adjust(hspace=.0)

plt.legend(
        ncol = 3,
        fancybox = True,
        shadow = True,
        loc = 'upper center',
     #   bbox_to_anchor = (0.7, 1.0)
        )

fig_obs.savefig('C:/Users/kahl/Documents/Review/figures/review_observation.png')
plt.close(fig_obs)

# state data

fig_state= plt.figure()
ax1 = fig_state.add_subplot(321)
ax2 = fig_state.add_subplot(322)
ax3 = fig_state.add_subplot(323)
ax4 = fig_state.add_subplot(324)
ax5 = fig_state.add_subplot(325)
ax6 = fig_state.add_subplot(326)

# plot color and linestyles
ls1 = '-'
ls2 = ':'
col1 = 'b'
col2 = 'r'

line1, = ax1.plot(t_step, state_data["x1"], 
                  color = col1, linestyle = ls1)
line11,= ax1.plot(t_step, filter_data["x1"], 
                  color = col2, linestyle = ls2)
line2, = ax2.plot(t_step, state_data["x2"], 
                  color = col1, linestyle = ls1)
line21,= ax2.plot(t_step, filter_data["x2"],
                  color = col2, linestyle = ls2)
line3, = ax3.plot(t_step, state_data["x3"], 
                  color = col1, linestyle = ls1)
line31,= ax3.plot(t_step, filter_data["x3"],
                  color = col2, linestyle = ls2)
line4, = ax4.plot(t_step, state_data["x4"], 
                  color = col1, linestyle = ls1)
line41,= ax4.plot(t_step, filter_data["x4"],
                  color = col2, linestyle = ls2)
line5, = ax5.plot(t_step, state_data["x5"],
                  color = col1, linestyle = ls1)
line51,= ax5.plot(t_step, filter_data["x5"],
                  color = col2, linestyle = ls2)
line6, = ax6.plot(t_step, state_data["x6"], 
                  color = col1, linestyle = ls1)
line61,= ax6.plot(t_step, filter_data["x6"],
                  color = col2, linestyle = ls2)

ax1.set_xlabel('time step')
ax2.set_xlabel('time step')
ax3.set_xlabel('time step')
ax4.set_xlabel('time step')
ax5.set_xlabel('time step')
ax6.set_xlabel('time step')


ax1.set_title('$x_1$')
ax2.set_title('$x_2$')
ax3.set_title('$x_3$')
ax4.set_title('$x_4$')
ax5.set_title('$x_5$')
ax6.set_title('$x_6$')


box = ax2.get_position()
ax2.set_position([box.x0, box.y0, box.width * 1.8, box.height])
plt.legend((line1, line11),
           ('true state', 'filtered state'), 
           loc = 'center right' ,
           bbox_to_anchor = (2.2, 6.0),
           fancybox = True,
           shadow = True
           )

plt.tight_layout()

fig_state.savefig('C:/Users/kahl/Documents/Review/figures/FilterState.png')
plt.close(fig_state)


# <--- PLOT