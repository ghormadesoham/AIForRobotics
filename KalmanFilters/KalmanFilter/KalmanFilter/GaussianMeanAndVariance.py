#1-D Kalman Filter
# Write a program to update your mean and variance
# when given the mean and variance of your belief/prior/X 
# and the mean and variance of your measurement(Z).
# This program will update the parameters of your
# belief function.
#measurement step /sense
def update(mean1, var1, mean2, var2):
    new_mean = mean(mean1,var1,mean2,var2)
    new_var = variance(var1,var2)
    return [new_mean, new_var]

def mean(mean1,var1,mean2,var2):
    m = ( 1/(var1 + var2 ) )*(var2*mean1 + var1*mean2);
    return m

def variance(var1,var2):
    v =  1/(1/var1 + 1/var2 ) ;
    return v

#motion 
def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2;
    new_var = var1 + var2;
    return [new_mean, new_var]


#question in class 
measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0.
sig = 10000.

#Please print out ONLY the final values of the mean
#and the variance in a list [mu, sig]. 

# Insert code here
for i in range(len(measurements)):
    [mu,sig] = update(mu,sig,measurements[i],measurement_sig)
    [mu,sig] = predict(mu,sig,motion[i],motion_sig)
print ([mu, sig])
