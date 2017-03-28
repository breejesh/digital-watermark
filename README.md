# Digital Watermark for Copyright Protection of Digital Images
The aim of this case study is to demonstrate a digital watermarking scheme using visual cryptography for copyright protection of a digital image. A binary image, called watermark, is split into two shares via a 2-out-of-2 visual secret sharing scheme. Then, one of the shares called the master share is extracted from the host image using a fixed pseudo-random points, and the other share also known as ownership share, made by relating the master share and the watermark, is held by the owner which is also given to an authorized 3rd party copyright verifier. Based on the security property of visual cryptography, the two shares on their own cannot leak any information about the watermark. The experimental results show that even after the image was modified, the invisible watermark was successfully extracted from it.

## How to run
1. 'python owernership_share_generator.py'  will generate the Ownership share for our image and watermark.
2. 'python master_share_generator.py' will generate all the Master shares for each of the sample stolen and modified images.
3. 'python watermark_generator.py' will extract watermarks using the Ownership share with each of the master shares.
4. 'python template_match_res.py' will give the accuracy of extracted watermark.
