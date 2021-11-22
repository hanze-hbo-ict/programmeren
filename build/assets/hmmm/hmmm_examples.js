var examples = [
  {
    name: "Even or Odd",
    code: "# Even or Odd\n#\n# This program will take a integer as input from the user,\n# then print 0 if the input is even and 1 if the input is odd\n#\n# Register Usage\n#   r1 -> User Input\n#   r2 -> Modulus value (i.e., 2)\n#   r3 -> Result of input % 2\n#   r4 -> Output value\n#\n0 read  r1        # Read the user's input      \n1 setn  r2 2      # We'll mod by 2 to check for odd/even\n2 mod   r3 r1 r2  # Compute input % 2 and store in r3\n3 jnez  r3 6      # If r3 == 1 (i.e., input is odd) jump\n4 setn  r4 0      # Otherwise, set our output value to 0...\n5 jumpn 7         # ...and jump to the output instruction\n6 setn  r4 1      # Set output to 1 (since input is odd)\n7 write r4        # Print output to the user\n8 halt            # And exit\n"
  },
  {
    name: "Area of Triangle",
    code: "#\n# Calculate the approximate area of a triangle.\n#\n# First input: base\n# Second input: height\n# Output: area\n#\n\n0  read  r1       # Get base\n1  read  r2       # Get height\n2  mul   r1 r1 r2 # b times h into r1\n3  setn  r2 2\n4  div   r1 r1 r2 # Divide by 2\n5  write r1\n6  halt\n"
  },
  {
    name: "Iterative Factorial",
    code: "#\n# Calculate N factorial.\n#\n# Input: N\n# Output: N!\n#\n# Register usage:\n#\n#  r1  N\n#  r2  Running product\n#\n\n0  read  r1       # Get N\n1  setn  r2 1\n2  jeqzn r1 6     # Quit if N has reached zero\n3  mul   r2 r1 r2 # Update product\n4  addn  r1 -1    # Decrement N\n5  jumpn 2        # Back for more\n\n6  write  r2\n7  halt\n"
  },
]
