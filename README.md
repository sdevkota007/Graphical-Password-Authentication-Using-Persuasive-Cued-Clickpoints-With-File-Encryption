# Graphical-Password-Authentication-Using-Persuasive-Cued-Clickpoints-with-File-Encryption

The basic foundation of the project is based on an IEEE paper: "Persuasive Cued Click-Points: Design, implementation, and
evaluation of a knowledge-based authentication mechanism" published by Sonia Chiasson,Member, IEEE,Elizabeth Stobert, Alain
Forget, Robert Biddle,Member, IEEE and P. C. van Oorschot,Member, IEEE. 
A graphical password authentication system works by having the user select the images, in a specific order. The Persuasive
Technology guides and encourages the user to select stronger passwords (i.e. click-points), but not entirely impose system
generated passwords. The proposed system consists of two modules; user registration and user login. The registration phase, in
which user registers a unique username and the graphical password in the database, is followed by user login phase. During login,
the user is asked to provide the username and correct graphical password. Upon successful verification of the user profile from
the database, the user is now able to encrypt/decrypt his files. The cryptographic algorithm used to provide security to the
files is the AES encryption, where the 16-bit key for cipher is generated from the SHA-256 hashing algorithm implemented on the
user click-points.


### Application Screenshots

[![html dark](https://github.com/sdevkota007/Graphical-Password-Authentication-Using-Persuasive-Cued-Clickpoints-With-File-Encryption/blob/master/screenshots/main%20window.JPG)
[![html dark](https://github.com/sdevkota007/Graphical-Password-Authentication-Using-Persuasive-Cued-Clickpoints-With-File-Encryption/blob/master/screenshots/login.JPG)
[![html dark](https://github.com/sdevkota007/Graphical-Password-Authentication-Using-Persuasive-Cued-Clickpoints-With-File-Encryption/blob/master/screenshots/registration%20(step%201%20of%202).JPG)
[![html dark](https://github.com/sdevkota007/Graphical-Password-Authentication-Using-Persuasive-Cued-Clickpoints-With-File-Encryption/blob/master/screenshots/registration%20(step%202%20of%202).JPG)
[![html dark](https://github.com/sdevkota007/Graphical-Password-Authentication-Using-Persuasive-Cued-Clickpoints-With-File-Encryption/blob/master/screenshots/image%20selection.JPG)
[![html dark](https://github.com/sdevkota007/Graphical-Password-Authentication-Using-Persuasive-Cued-Clickpoints-With-File-Encryption/blob/master/screenshots/home.JPG)


### HTML (Vim)

[![ALT dark](https://github.com/altercation/solarized/raw/master/img/screen-html-dark-th.png)](https://github.com/altercation/solarized/raw/master/img/screen-html-dark.png)
[![html light](https://github.com/altercation/solarized/raw/master/img/screen-html-light-th.png)](https://github.com/altercation/solarized/raw/master/img/screen-html-light.png)
