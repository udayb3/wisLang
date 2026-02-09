from scipy import linalg as LA              #SVD Transform
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
img = cv2.imread("wall11.jpg", 0)

#Add Gaussian noise
mean = 0
var = 0.01
sigma = var**0.5
gaussian = np.random.normal(mean, sigma, img.shape)
noisy_img = np.clip((img + gaussian*255), 0, 255).astype(np.uint8)


 #Add uniform noise
#low = -4
#high = 4
#uniform = np.random.uniform(low, high, img.shape)
#noisy_img = np.clip((img + uniform), 0, 255).astype(np.uint8)

plt.imshow(noisy_img, cmap='gray')
plt.axis('off')
plt.show(block=False)
# Perform SVD
U, S, VT = LA.svd(noisy_img)

# Define list of ranks to use
ranks = [50,100,150,200,250]

# Loop over ranks and plot reconstructed image
for i, rank in enumerate(ranks):
    # Truncate SVD matrices
    U_rank = U[:, :rank]
    S_rank = np.diag(S[:rank])
    VT_rank = VT[:rank, :]
    
    # Reconstruct image
    # img_recon = U_rank @ S_rank @ VT_rank
    img_recon = np.dot(U_rank, np.dot(S_rank, VT_rank))

    
    # cv2.imshow('Reconstructed Image', img_recon)

    # Plot reconstructed image
    plt.figure()
    plt.imshow(img_recon, cmap='gray')
    plt.title(f'Rank {rank}')
    plt.axis('off')

    plt.show(block=False)
    plt.waitforbuttonpress()    #press any key to update or close the program
# Show Original image
# cv2.imshow('Original Image', img)