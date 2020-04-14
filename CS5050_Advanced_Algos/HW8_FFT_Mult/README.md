Unfortunately, I have having a little trouble getting the solution for two multiplied numbers to return correctly. 
I probably just have a simple misconception. 
The FFT and Inverse FFT code works well, but I cant figure out how to multiply the two numbers together in phase space to get the correct answer. 
I think with a little more time I could figure it out, as with all coding, im sure it’s a simple mistake.


In terms of part 2, the cause of this is in accuracy in floating point numbers. 
When you transition from R2 into phase space, you need to move onto the unit circle which implies multiplying by one side of Euler’s identity. 
That then introduces floating point error. 
So when you want to get out of phase space and back to real numbers, you take the inverse (multiply by the complex conjugate.) 
These numbers are stored as floating point numbers, so the multiplication of them increases the inaccuracy. 
The increase is proportional to the square of the error. 
If I had solved the poly multiplication problem, I could have measured the difference between the two.

Thanks!
Jacob
