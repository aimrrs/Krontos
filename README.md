# Krontos-Hackathon-
Pincode based serviceability allows merchants to define the pincodes where they can deliver their products &amp; services. Merchants define the pincodes they serve and buyer apps verify whether a particular pincode (of buyer) can be served. This requires an optimal data structure for storing the pincode by merchant to verifiy in near real-time.

Since there are many approaches to slove this particular problem, we choose to create our own data structure.

Krontos - data structure

AIM : To create a matrix using 2D list consisting of None values. The dimensions of the matrix is M x N, where N - is the number of merchants and N - number of pincodes available overall. Update to the matrix as either True or False (1 or 0) by verifying each code weather it is available for shipping of its merchant.

Sample dataset (input file) format:

MERCHANT1, PINCODE1, PINCODE2, PINCODE3, PINCODE4, PINCODE5, PINCODE6 \n
MERCHANT2, PINCODE1, PINCODE2, PINCODE3, PINCODE4, PINCODE5, PINCODE6 \n
MERCHANT3, PINCODE1, PINCODE2, PINCODE3, PINCODE4, PINCODE5, PINCODE6 \n
MERCHANT4, PINCODE1, PINCODE2, PINCODE3, PINCODE4, PINCODE5, PINCODE6 \n
MERCHANT5, PINCODE1, PINCODE2, PINCODE3, PINCODE4, PINCODE5, PINCODE6 \n

This is the format for the CSV file which needs to be given as input dataset.
