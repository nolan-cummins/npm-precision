This code is designed to analyze the precision of the NPM stage. However, it can also be used to track an reference point moving around the frame of a configurable size. 

Currently, the script runs as many videos as the client PC can handle in parallel, and assumes the reference point to be within a box of width and height 20% that of the frame size, plus 50 pixels in all directions. 

This may or may not change in the future, as it suits my purposes.

Figure 1. (x,y) precision of NPM

![4-2 pix to um FIXED](https://github.com/user-attachments/assets/b130a908-590c-4af8-8a93-aa815cb4b885)


Figure 2. Regression for steps to um conversion.

![Steps to um Regression 4-2 pix um](https://github.com/user-attachments/assets/6e35a276-83e2-4e26-8e63-bbc2c23cc801)


Figure 3. Example data for 3000 step-size precision measurements.

![3000 step](https://github.com/user-attachments/assets/257ace2e-4602-496e-a61c-99d649d277d4)

