# Image-Editor-Web-App-in-Python

The upload html file is the welcome page of the application, that provides the following functionalities:
1. Upload an Image (only of JPG, JPEG & PNG format is allowed)
2. Display the URL of the image that is being uploaded
3. Button on click display's the properties of the image being uploaded such as :
    Creation Date
    Modification Date
    File size
    Image Resolution
    Average mean RGB
4. Button on click to delete the image

Procedure followed for hosting this Jar on AWS EC2 instance:
1. Selected a free tier instance on AWS console website(linux)
2. Transformed the public key into ppk private key and logged into the EC2 instance
3. Installed and configured Python, Flask on the server
4. Transfered the final .py file and html file onto EC2 instance using pscp linux commands
5. Final python file is executed using python *.py command
6. The hosted URL is tested for performing all the required functionalities
