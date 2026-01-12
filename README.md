# Fast Print
Efficiently prints approximate values of extremely large numbers.
It is accurate to about 9 or 10 base 10 digits since its limited by floating point accuracy

### Approach

For a given a you want to convert to base k digit by digit you first take the log base k in as much accuracy as desired.
Then there are two operations to read each digit out of the log which are described below.
Its important to note that you must handle zeroes by checking that the floor of the log changes by at most one per digit read.
The reason this is faster is because you only handle very small numbers and never "look at the sun" by viewing the whole number.
This only becomes faster in python around 10^(10^5) which is enourmous.

_reading MSD from logk_a_

      head_digit(logk_a) = floor(k^(logk_a - floor(logk_a)))

_removing MSD from logk_a_
  
      behead(logk_a) = logk(1 - k^(floor(logk_a) - logk_a) * k^(logk_a - floor(logk_a)))
