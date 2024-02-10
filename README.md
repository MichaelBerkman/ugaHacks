Created By: 
Michael Berkman
Mishelle Orrego 

This is a camera that works on RasberryPi Camera. It can take HD pictures and videos.

# Guardian Eye Project

## Team Members

- Mishelle Orrego
- Michael Berkman

## Purpose

The "Guardian Eye" project aims to blend the realms of personal security and digital convenience by leveraging the compact yet powerful Raspberry Pi platform. Designed to be a vigilant observer in any setting, this device captures critical moments through a camera module, ensuring each snapshot is unique with a sophisticated file naming system. Our mission was to create a user-friendly, efficient, and reliable tool for enhancing safety and capturing life's moments without intrusion.

## Tools Utilized

- **Raspberry Pi**: The core of our project, providing the compact and versatile platform for our security camera.
- **Pi Camera Module**: For capturing high-quality images and video.
- **Python**: The primary programming language used for developing the software, including image processing and device control.
- **OpenCV**: For advanced image processing capabilities.
- **GPIO**: Utilized for interfacing with additional sensors and components.

## Challenges and Solutions

### Lighting Conditions

**Problem**: We encountered challenges in optimizing the camera's performance across various lighting conditions.

**Solution**: We implemented dynamic adjustment algorithms using OpenCV, allowing the camera to adapt to changing light levels and maintain image quality.

### User Privacy

**Problem**: Balancing functionality with user privacy concerns was paramount, especially in a device designed for personal spaces.

**Solution**: We designed the system with privacy-first principles, ensuring data is processed locally and providing users with clear controls over the camera's operation.

### User Interface

**Problem**: Creating an intuitive yet powerful user interface posed a significant challenge, given the device's compact nature and the complexity of its features.

**Solution**: We developed a minimalist, web-based interface that allows users to easily control the device and access its features without overwhelming them with technical complexities.

## Credits and Acknowledgements

We leveraged several public frameworks and APIs to bring "Guardian Eye" to life, including:

- **Raspberry Pi Foundation**: For providing extensive documentation and community support for the Raspberry Pi platform.
- **OpenCV**: For their open-source computer vision and machine learning software library, which was invaluable in image processing tasks.
- **Flask**: For creating the web server and user interface, allowing for remote control and monitoring of the device.

Our heartfelt thanks go out to the developers and communities behind these tools, without whom this project would not have been possible. Their contributions to the open-source community have made projects like ours achievable and inspiring.
