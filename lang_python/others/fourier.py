from scipy import linalg as LA
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load image
img = cv2.imread("wall11.jpg", 0)

# Add Gaussian noise
#mean = 0
#var = 0.01
#sigma = var**0.5
#gaussian = np.random.normal(mean, sigma, img.shape)
#noisy_img = np.clip((img + gaussian*255), 0, 255).astype(np.uint8)


# Add uniform noise
low = -4
high = 4
uniform = np.random.uniform(low, high, img.shape)
noisy_img = np.clip((img + uniform), 0, 255).astype(np.uint8)
plt.imshow(noisy_img, cmap='gray')
plt.axis('off')
plt.show(block=False)

# DFT approach
dft = cv2.dft(np.float32(noisy_img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
for k in [1000,2000,3000,4000,5000,6000,7000,8000,9000]:
    rows, cols = noisy_img.shape
    mask = np.zeros((rows, cols, 2), np.uint8)
    mask[:k, :k] = 1
    dft_shift_masked = dft_shift * mask
    idft_shift = np.fft.ifftshift(dft_shift_masked)
    reconstructed_img = cv2.idft(idft_shift)
    reconstructed_img = cv2.magnitude(reconstructed_img[:, :, 0], reconstructed_img[:, :, 1])
    # cv2.imwrite(f'reconstructed_dft_k{k}.jpg', reconstructed_img)

    # displaying reconstruced image
    plt.figure()
    plt.imshow(reconstructed_img, cmap='gray')
    plt.title(f'Rank {k}')
    plt.axis('off')
    plt.show(block=False)
    plt.waitforbuttonpress()  #press any key to update or close the program